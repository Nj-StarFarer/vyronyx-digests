"""Generic: download Wikimedia Commons audio files by title and convert to 16 kHz mono FLAC (first N seconds).
Public, free-licence data only. Records each file's licence and source URL. Usage:
python commons_audio.py TITLES_JSON OUT_DIR SECONDS"""
import hashlib, json, os, subprocess, sys, urllib.parse, urllib.request

API = "https://commons.wikimedia.org/w/api.php?"
UA = "vyronyx-dataset-fetch/1.0 (public data research)"


def api(params):
    q = API + urllib.parse.urlencode(dict(params, format="json"))
    with urllib.request.urlopen(urllib.request.Request(q, headers={"User-Agent": UA}), timeout=60) as r:
        return json.load(r)


def info(titles):
    out = {}
    for i in range(0, len(titles), 40):
        d = api(dict(action="query", prop="imageinfo", iiprop="url|extmetadata|size", titles="|".join(titles[i:i + 40])))
        for p in d["query"]["pages"].values():
            ii = (p.get("imageinfo") or [{}])[0]
            md = ii.get("extmetadata", {})
            out[p["title"]] = dict(url=ii.get("url"), licence=md.get("LicenseShortName", {}).get("value"),
                                   artist=md.get("Artist", {}).get("value"))
    return out


def main(titles_file, out, seconds):
    titles = json.load(open(titles_file)); os.makedirs(out, exist_ok=True)
    meta = info(titles); man = []
    for t in titles:
        m = meta.get(t, {}); row = dict(title=t, licence=m.get("licence"), url=m.get("url"))
        name = hashlib.sha256(t.encode()).hexdigest()[:16]
        raw = os.path.join(out, "raw_" + name); dst = os.path.join(out, name + ".flac")
        try:
            req = urllib.request.Request(m["url"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=600) as r, open(raw, "wb") as f:
                f.write(r.read())
            p = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-vn", "-ac", "1", "-ar", "16000", "-t", str(seconds),
                                "-sample_fmt", "s16", dst], capture_output=True, text=True)
            row.update(file=os.path.basename(dst), ok=p.returncode == 0, err=p.stderr[-200:] if p.returncode else None)
            if p.returncode == 0:
                row["sha256"] = hashlib.sha256(open(dst, "rb").read()).hexdigest()
        except Exception as e:
            row.update(ok=False, err=f"{type(e).__name__}: {e}"[:200])
        finally:
            if os.path.exists(raw):
                os.remove(raw)
        man.append(row); print(json.dumps({k: row.get(k) for k in ("title", "ok", "err")}), flush=True)
    json.dump(man, open(os.path.join(out, "manifest.json"), "w"), indent=1)
    open(os.path.join(out, "ATTRIBUTION.txt"), "w").write(
        "Wikimedia Commons recordings under their own free licences (see manifest.json: licence, url, artist).\n"
        "Converted to 16 kHz mono FLAC, first %s seconds; content otherwise unchanged.\n" % seconds)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

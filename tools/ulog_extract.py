"""Generic PX4 flight-log (ULog) extractor for public open-licence datasets.
For each listed log: download, read a few standard PX4 topics with pyulog (BSD-3-Clause), write a census row, and,
when the log has GPS fixes, save those topics as a compressed .npz. The downloaded log is deleted straight after.
Usage: python ulog_extract.py DATASET_ID mapping.json OUT_DIR [workers]
"""
import concurrent.futures as cf
import json
import os
import sys
import urllib.parse
import urllib.request

import numpy as np

TOPICS = ["vehicle_gps_position", "sensor_combined", "vehicle_attitude", "vehicle_air_data", "sensor_baro",
          "vehicle_global_position", "vehicle_local_position"]
KEEP = {
    "vehicle_gps_position": ["lat", "lon", "alt", "vel_n_m_s", "vel_e_m_s", "vel_d_m_s", "fix_type", "eph", "epv",
                             "satellites_used", "jamming_indicator", "noise_per_ms", "latitude_deg", "longitude_deg",
                             "altitude_msl_m"],
    "sensor_combined": ["accelerometer_m_s2[0]", "accelerometer_m_s2[1]", "accelerometer_m_s2[2]"],
    "vehicle_attitude": ["q[0]", "q[1]", "q[2]", "q[3]"],
    "vehicle_air_data": ["baro_alt_meter"],
    "sensor_baro": ["altitude", "pressure"],
    "vehicle_global_position": ["lat", "lon", "alt", "eph"],
    "vehicle_local_position": ["x", "y", "z", "vx", "vy", "vz", "xy_valid"],
}


def one(ds, key, out):
    from pyulog import ULog
    url = f"https://huggingface.co/datasets/{ds}/resolve/main/" + urllib.parse.quote(f"ulg_files/{key}.ulg")
    tmp = os.path.join(out, "tmp_" + key.replace("/", "__") + ".ulg")
    row = {"key": key}
    try:
        urllib.request.urlretrieve(url, tmp)
        row["bytes"] = os.path.getsize(tmp)
        u = ULog(tmp, TOPICS)
        arrs, present = {}, {}
        for d in u.data_list:
            if d.multi_id != 0 or d.name not in KEEP:
                continue
            present[d.name] = len(d.data["timestamp"])
            arrs[f"{d.name}/timestamp"] = np.asarray(d.data["timestamp"], np.int64)
            for f in KEEP[d.name]:
                if f in d.data:
                    arrs[f"{d.name}/{f}"] = np.asarray(d.data[f], np.float64 if f in ("lat", "lon", "latitude_deg", "longitude_deg") else np.float32)
        row["topics"] = present
        row["start_us"], row["last_us"] = int(u.start_timestamp), int(u.last_timestamp)
        fix = arrs.get("vehicle_gps_position/fix_type")
        row["gps_fix3"] = int((fix >= 3).sum()) if fix is not None else 0
        if row["gps_fix3"] > 0:
            p = os.path.join(out, "npz", key.replace("/", "__") + ".npz")
            os.makedirs(os.path.dirname(p), exist_ok=True)
            np.savez_compressed(p, **arrs)
            row["npz"] = os.path.basename(p)
    except Exception as e:  # reported, never hidden
        row["error"] = f"{type(e).__name__}: {e}"[:300]
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    return row


def main():
    ds, mapping, out = sys.argv[1], sys.argv[2], sys.argv[3]
    workers = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    keys = sorted(json.load(open(mapping)))
    os.makedirs(out, exist_ok=True)
    rows = []
    with cf.ThreadPoolExecutor(workers) as ex:
        for i, r in enumerate(ex.map(lambda k: one(ds, k, out), keys)):
            rows.append(r)
            if i % 100 == 0:
                print(i, r.get("key"), r.get("gps_fix3"), r.get("error", ""), flush=True)
    json.dump(rows, open(os.path.join(out, "census.json"), "w"))
    g = [r for r in rows if r.get("gps_fix3")]
    print(f"{len(rows)} logs, {len(g)} with GPS fixes, {sum(1 for r in rows if 'error' in r)} errors")


if __name__ == "__main__":
    main()

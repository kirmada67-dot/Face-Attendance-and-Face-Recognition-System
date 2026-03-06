#!/usr/bin/env python3
import csv
import os
import subprocess
import sys
from collections import defaultdict, deque
from datetime import datetime, date
import platform

input_file = "log.txt"
if len(sys.argv) > 1:
    try:
        target_date = datetime.strptime(sys.argv[1], "%Y-%m-%d").date()
    except Exception:
        target_date = date.today()
else:
    target_date = date.today()

events = []
if not os.path.exists(input_file):
    print("log.txt not found")
    sys.exit(1)

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",", 2)
        if len(parts) != 3:
            continue
        name = parts[0].strip()
        ts = parts[1].strip()
        status = parts[2].strip().lower()
        dt = None
        try:
            dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            try:
                dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
            except Exception:
                continue
        if dt.date() == target_date:
            events.append((name, dt, status))

events.sort(key=lambda x: x[1])

by_name = defaultdict(list)
for name, dt, status in events:
    by_name[name].append((dt, status))

rows = []
for name, evs in by_name.items():
    evs.sort(key=lambda x: x[0])
    pending = deque()
    for dt, status in evs:
        if status == "in":
            pending.append(dt)
        elif status == "out":
            if pending:
                login_dt = pending.popleft()
                rows.append([name, target_date.isoformat(), login_dt.strftime("%H:%M:%S"), dt.strftime("%H:%M:%S")])
            else:
                continue
    while pending:
        login_dt = pending.popleft()
        rows.append([name, target_date.isoformat(), login_dt.strftime("%H:%M:%S"), ""])

rows.sort(key=lambda r: (r[0].lower(), r[2] if r[2] else ""))

out_dir = "Daily attendance"
if not os.path.exists(out_dir):
    try:
        os.mkdir(out_dir)
    except Exception:
        pass

output_file = os.path.join(out_dir, f"attendance_{target_date.isoformat()}.csv")
if os.path.exists(output_file):
    try:
        os.remove(output_file)
    except Exception:
        pass

with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Date", "Login", "Logout"])
    for name, date_str, login, logout in rows:
        writer.writerow([name, "'" + date_str, "'" + login if login else "", "'" + logout if logout else ""])

print(f"Created {output_file} ({len(rows)} rows)")

def open_file(path):
    try:
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.call(["open", path])
        else:
            subprocess.call(["xdg-open", path])
    except Exception:
        pass

open_file(output_file)

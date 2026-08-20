import csv
from collections import Counter

filename = input("Enter Windows Event Log CSV file: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        failed = [row for row in reader if row["event_id"] == "4625"]

    print("\n===== FAILED LOGIN ATTEMPTS =====")
    if not failed:
        print("No failed login attempts found.")
    else:
        for row in failed:
            print("Time:", row["timestamp"])
            print("User:", row["username"])
            print("Source IP:", row["source_ip"])
            print("--------------------------------")

        print("\n===== REPEATED ATTEMPTS =====")
        counts = Counter(row["source_ip"] for row in failed)
        for ip, count in counts.items():
            if count >= 3:
                print(ip, "->", count, "failed attempts")
except FileNotFoundError:
    print("Error: Log file not found.")

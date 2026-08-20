import csv

AUTHORIZED = {"USB001", "USB002"}

filename = input("Enter USB activity log CSV file: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        print("\n===== USB DEVICE ANALYSIS =====")

        for row in reader:
            if row["action"].lower() == "connected":
                if row["device_id"] not in AUTHORIZED:
                    print("[UNAUTHORIZED USB]")
                    print("Time:", row["timestamp"])
                    print("Device:", row["device_name"])
                    print("Device ID:", row["device_id"])
                    print("--------------------------------")
                else:
                    print("[AUTHORIZED]", row["device_name"])
except FileNotFoundError:
    print("Error: USB log file not found.")

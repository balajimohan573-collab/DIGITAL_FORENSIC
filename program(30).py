import csv

THREAT_IPS = {"10.10.10.10", "192.168.1.50", "203.0.113.25"}

filename = input("Enter network security log CSV: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        print("\n===== SUSPICIOUS IP ADDRESSES =====")
        found = False

        for row in reader:
            if row["ip"] in THREAT_IPS:
                found = True
                print("IP:", row["ip"])
                print("Time:", row["timestamp"])
                print("Action:", row["action"])
                print("--------------------------------")

        if not found:
            print("No threat-indicator IPs found.")

except FileNotFoundError:
    print("Error: Log file not found.")

import csv

filename = input("Enter malware activity log CSV: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        print("\n===== SUSPICIOUS MALWARE ACTIVITY =====")

        for row in reader:
            behavior = row["behavior"].lower()

            if any(word in behavior for word in
                   ["encrypt", "inject", "delete", "suspicious", "connection"]):
                print("Time:", row["timestamp"])
                print("Type:", row["type"])
                print("Activity:", row["behavior"])
                print("--------------------------------")

except FileNotFoundError:
    print("Error: Malware log not found.")

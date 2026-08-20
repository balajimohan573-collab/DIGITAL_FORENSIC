import csv

filename = input("Enter investigation records CSV: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        events = list(reader)

    events.sort(key=lambda x: x["timestamp"])

    print("\n===== INCIDENT RESPONSE TIMELINE =====")
    for row in events:
        print(row["timestamp"])
        print("Source:", row["source"])
        print("Event :", row["event"])
        print("Details:", row["details"])
        print("--------------------------------")

except FileNotFoundError:
    print("Error: Investigation file not found.")

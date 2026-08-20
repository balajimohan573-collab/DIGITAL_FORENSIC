import csv

filename = input("Enter event timeline CSV file: ").strip().strip('"')

try:
    events = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            events.append((row["timestamp"], row["event"], row["details"]))

    events.sort(key=lambda x: x[0])

    print("\n===== DIGITAL FORENSIC EVENT TIMELINE =====")
    for timestamp, event, details in events:
        print("Time:", timestamp)
        print("Event:", event)
        print("Details:", details)
        print("--------------------------------")
except FileNotFoundError:
    print("Error: Event log file not found.")

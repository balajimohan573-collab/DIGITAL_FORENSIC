import csv
from collections import Counter

filename = input("Enter file activity CSV: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    print("\n===== RANSOMWARE-LIKE ACTIVITY =====")
    modifications = Counter()
    suspicious = False

    for row in rows:
        if row["action"].lower() == "modified":
            modifications[row["timestamp"][:16]] += 1

        old_ext = row.get("old_extension", "")
        new_ext = row.get("new_extension", "")

        if old_ext and new_ext and old_ext != new_ext:
            suspicious = True
            print("[EXTENSION CHANGE]")
            print("File:", row["file"])
            print(old_ext, "->", new_ext)

    for minute, count in modifications.items():
        if count >= 5:
            suspicious = True
            print("[RAPID MODIFICATION]")
            print(minute, "->", count, "files modified")

    if not suspicious:
        print("No ransomware-like activity detected.")

except FileNotFoundError:
    print("Error: File not found.")

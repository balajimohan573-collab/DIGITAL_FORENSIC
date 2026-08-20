import csv
from collections import Counter

filename = input("Enter authentication log CSV: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        failures = Counter()

        for row in reader:
            if row["status"].lower() == "failed":
                failures[row["username"]] += 1

    print("\n===== POSSIBLE PASSWORD ATTACKS =====")

    found = False
    for user, count in failures.items():
        if count >= 3:
            found = True
            print(user, "->", count, "failed attempts")

    if not found:
        print("No repeated authentication failures found.")

except FileNotFoundError:
    print("Error: Authentication log not found.")

import csv
from collections import Counter

filename = input("Enter firewall log CSV: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    print("\n===== BLOCKED CONNECTIONS =====")
    counts = Counter()

    for row in rows:
        if row["action"].lower() == "blocked":
            print(row["timestamp"], row["source_ip"], "->", row["destination"])
            counts[row["source_ip"]] += 1

    print("\n===== REPEATED UNAUTHORIZED ATTEMPTS =====")
    for ip, count in counts.items():
        if count >= 3:
            print(ip, "->", count, "blocked attempts")

except FileNotFoundError:
    print("Error: Firewall log not found.")

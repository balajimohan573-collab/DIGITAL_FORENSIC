import csv
from collections import Counter

filename = input("Enter packet log CSV: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        counts = Counter(row["destination_ip"] for row in reader)

    print("\n===== POSSIBLE DOS PATTERNS =====")
    found = False

    for ip, count in counts.items():
        if count >= 10:
            found = True
            print("[HIGH PACKET RATE]", ip, "->", count, "packets")

    if not found:
        print("No obvious DoS pattern detected.")

except FileNotFoundError:
    print("Error: Packet log not found.")

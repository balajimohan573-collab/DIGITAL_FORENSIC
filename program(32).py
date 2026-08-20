import csv
from collections import Counter

filename = input("Enter network traffic CSV: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        outbound = Counter()

        for row in reader:
            if row["direction"].lower() == "outbound":
                outbound[row["destination_ip"]] += int(row["bytes"])

    print("\n===== UNUSUAL OUTBOUND ACTIVITY =====")
    for ip, total in outbound.items():
        print(ip, "->", total, "bytes")

    if outbound:
        average = sum(outbound.values()) / len(outbound)
        print("\nThreshold:", int(average * 2), "bytes")
        for ip, total in outbound.items():
            if total > average * 2:
                print("[UNUSUAL]", ip, total, "bytes")

except FileNotFoundError:
    print("Error: Traffic log not found.")

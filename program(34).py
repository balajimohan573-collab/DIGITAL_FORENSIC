import csv
import re

filename = input("Enter domain list CSV: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        print("\n===== SUSPICIOUS DOMAINS =====")

        for row in reader:
            domain = row["domain"].lower()
            reasons = []

            if len(domain) > 40:
                reasons.append("very long domain")

            if "@" in domain:
                reasons.append("@ symbol")

            if domain.count("-") >= 3:
                reasons.append("many hyphens")

            if re.search(r"\d{5,}", domain):
                reasons.append("many consecutive digits")

            for word in ["login", "verify", "secure", "update", "account"]:
                if word in domain:
                    reasons.append("suspicious keyword")
                    break

            if reasons:
                print("Domain:", domain)
                print("Reason:", ", ".join(reasons))
                print("--------------------------------")

except FileNotFoundError:
    print("Error: Domain file not found.")

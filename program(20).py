import csv
from collections import Counter
from urllib.parse import urlparse
import re


def analyze_history(filename):

    websites = Counter()
    suspicious_urls = []

    suspicious_words = [
        "login",
        "verify",
        "password",
        "account",
        "bank",
        "free",
        "winner",
        "urgent",
        "download"
    ]

    try:
        with open(
            filename,
            "r",
            encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)

            # Show CSV columns
            print("\nCSV Columns:")
            print(reader.fieldnames)

            # Find URL column
            url_column = None

            for column in reader.fieldnames:

                if column.strip().lower() in [
                    "url",
                    "urls",
                    "link",
                    "website"
                ]:
                    url_column = column
                    break

            if url_column is None:

                print("\nError: Could not find URL column.")
                print("Please make sure your CSV contains a column named:")
                print("URL")

                return

            print("\nUsing URL column:", url_column)

            # --------------------------------
            # Read URLs
            # --------------------------------

            for row in reader:

                url = row[url_column].strip()

                if not url:
                    continue

                # Extract domain
                domain = urlparse(url).netloc

                if domain:
                    websites[domain] += 1

                reasons = []

                # Check IP address
                if re.search(
                    r"https?://\d{1,3}(\.\d{1,3}){3}",
                    url
                ):
                    reasons.append(
                        "IP address used"
                    )

                # Check @ symbol
                if "@" in url:
                    reasons.append(
                        "@ symbol found"
                    )

                # Check suspicious keywords
                for word in suspicious_words:

                    if word in url.lower():

                        reasons.append(
                            "Suspicious keyword: "
                            + word
                        )

                        break

                # Check long URL
                if len(url) > 150:

                    reasons.append(
                        "Very long URL"
                    )

                if reasons:

                    suspicious_urls.append(
                        (url, reasons)
                    )

    except FileNotFoundError:

        print("Error: File not found.")
        return

    except UnicodeDecodeError:

        print(
            "Error: CSV encoding is not UTF-8."
        )
        return

    # --------------------------------
    # Frequently visited websites
    # --------------------------------

    print("\n================================")
    print(" FREQUENTLY VISITED WEBSITES")
    print("================================")

    for domain, count in websites.most_common(10):

        print(
            f"{domain} -> {count} visits"
        )

    # --------------------------------
    # Suspicious URLs
    # --------------------------------

    print("\n================================")
    print("       SUSPICIOUS URLs")
    print("================================")

    if not suspicious_urls:

        print("No suspicious URLs found.")

    else:

        for url, reasons in suspicious_urls:

            print("\nURL:", url)

            print(
                "Reason:",
                ", ".join(reasons)
            )


# ========================================
# MAIN PROGRAM
# ========================================

print("========================================")
print("      BROWSER HISTORY ANALYZER")
print("========================================")

filename = input(
    "Enter browser history CSV file: "
).strip().strip('"')

analyze_history(filename)

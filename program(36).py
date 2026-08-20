import re

filename = input("Enter evidence text file: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8", errors="ignore") as file:
        text = file.read()

    urls = re.findall(r"https?://[^\s]+", text)
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
    domains = re.findall(r"\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b", text)

    print("\n===== EXTRACTED EVIDENCE =====")
    print("\nURLs:")
    for item in set(urls):
        print(item)

    print("\nEmail Addresses:")
    for item in set(emails):
        print(item)

    print("\nIP Addresses:")
    for item in set(ips):
        print(item)

    print("\nDomain Names:")
    for item in set(domains):
        print(item)

except FileNotFoundError:
    print("Error: Evidence file not found.")

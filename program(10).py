from email import policy
from email.parser import Parser
from email.utils import parseaddr
import re

# Sample raw email headers
raw_headers = """From: "Admin" <admin@example.com>
To: user@example.com
Reply-To: attacker@evil-example.com
Return-Path: <attacker@evil-example.com>
Subject: Urgent Account Verification
Date: Tue, 18 Aug 2026 10:30:00 +0530
Message-ID: <12345@example.com>
Received: from mail.evil-example.com (203.0.113.50)
    by mail.example.com with ESMTP;
    Tue, 18 Aug 2026 10:29:55 +0530
"""

# Parse the headers
headers = Parser(policy=policy.default).parsestr(raw_headers)

from_address = parseaddr(headers.get("From", ""))[1]
reply_to = parseaddr(headers.get("Reply-To", ""))[1]
return_path = parseaddr(headers.get("Return-Path", ""))[1]

print("=" * 55)
print("        EMAIL SPOOFING ANALYZER")
print("=" * 55)

print("\nFrom       :", from_address)
print("Reply-To   :", reply_to)
print("Return-Path:", return_path)
print("Subject    :", headers.get("Subject", "Not available"))

indicators = []

# 1. Check From vs Reply-To
if reply_to and from_address:
    if reply_to.lower() != from_address.lower():
        indicators.append(
            "From and Reply-To addresses do not match"
        )

# 2. Check From vs Return-Path
if return_path and from_address:
    if return_path.lower() != from_address.lower():
        indicators.append(
            "From and Return-Path addresses do not match"
        )

# 3. Check Message-ID domain
message_id = headers.get("Message-ID", "")

if message_id:
    match = re.search(r"@([^>]+)", message_id)

    if match:
        message_domain = match.group(1).lower()

        from_domain = from_address.split("@")[-1].lower()

        if message_domain != from_domain:
            indicators.append(
                "Message-ID domain differs from From domain"
            )

# 4. Analyze Received headers
received_headers = headers.get_all("Received", [])

print("\nReceived Headers:")

if received_headers:
    for number, received in enumerate(received_headers, 1):
        print(f"\n{number}. {received}")

        # Extract IPv4 addresses
        ip_addresses = re.findall(
            r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            received
        )

        for ip in ip_addresses:
            print("   Source IP:", ip)

else:
    indicators.append("No Received header found")

# 5. Check Authentication-Results
authentication = headers.get(
    "Authentication-Results",
    ""
)

if authentication:
    print("\nAuthentication Results:")
    print(authentication)

    if re.search(r"spf=(fail|softfail)", authentication,
                 re.IGNORECASE):
        indicators.append("SPF authentication failed")

    if re.search(r"dkim=(fail|none)", authentication,
                 re.IGNORECASE):
        indicators.append("DKIM authentication failed")

    if re.search(r"dmarc=(fail|none)", authentication,
                 re.IGNORECASE):
        indicators.append("DMARC authentication failed")

else:
    indicators.append(
        "No Authentication-Results header available"
    )

# Display results
print("\n" + "=" * 55)
print("ANALYSIS RESULT")
print("=" * 55)

if indicators:
    print("\nPossible spoofing

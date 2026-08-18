from collections import defaultdict
from datetime import datetime

LOG_FILE = "login.log"
MAX_FAILED_ATTEMPTS = 5

failed_attempts = defaultdict(list)

# Read the login log
with open(LOG_FILE, "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        # Example log format:
        # 2026-08-18 10:15:23 FAILED 192.168.1.10
        parts = line.split()

        if len(parts) < 4:
            continue

        date = parts[0]
        time = parts[1]
        status = parts[2]
        ip_address = parts[3]

        if status == "FAILED":
            timestamp = f"{date} {time}"
            failed_attempts[ip_address].append(timestamp)


print("========== BRUTE-FORCE DETECTION ==========\n")

attack_detected = False

for ip, attempts in failed_attempts.items():

    if len(attempts) >= MAX_FAILED_ATTEMPTS:
        attack_detected = True

        print("[WARNING] Possible brute-force attack detected!")
        print("IP Address :", ip)
        print("Failed Attempts :", len(attempts))
        print("First Attempt :", attempts[0])
        print("Last Attempt  :", attempts[-1])
        print("-" * 45)

if not attack_detected:
    print("No possible brute-force intrusion attempts detected.")

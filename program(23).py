import csv

SUSPICIOUS = {"powershell.exe", "cmd.exe", "wscript.exe",
              "cscript.exe", "mshta.exe", "rundll32.exe"}

filename = input("Enter process execution log CSV file: ").strip().strip('"')

try:
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        print("\n===== SUSPICIOUS PROCESSES =====")
        found = False

        for row in reader:
            if row["process"].lower() in SUSPICIOUS:
                found = True
                print("Time:", row["timestamp"])
                print("Process:", row["process"])
                print("User:", row["username"])
                print("Command:", row["command"])
                print("--------------------------------")

        if not found:
            print("No suspicious processes found.")
except FileNotFoundError:
    print("Error: Log file not found.")

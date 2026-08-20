import json
from datetime import datetime

case_id = input("Enter case ID: ")
examiner = input("Enter examiner name: ")
evidence = input("Enter evidence description: ")
hash_value = input("Enter SHA-256 hash: ")
findings = input("Enter findings: ")
conclusion = input("Enter conclusion: ")
recommendations = input("Enter recommendations: ")

report = {
    "case_id": case_id,
    "examiner": examiner,
    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "evidence": evidence,
    "sha256": hash_value,
    "findings": findings,
    "conclusion": conclusion,
    "recommendations": recommendations
}

filename = "forensic_case_report.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("\n===== DIGITAL FORENSIC CASE REPORT =====")
print(json.dumps(report, indent=4))
print("\nReport saved as:", filename)

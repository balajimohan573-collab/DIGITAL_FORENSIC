from datetime import datetime
import html


def generate_forensic_report(case_info, evidence, findings, timeline, output_file):
    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Escape text so special HTML characters don't break the report
    def safe(text):
        return html.escape(str(text))

    report = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Digital Forensic Investigation Report</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }}

        h1 {{
            text-align: center;
        }}

        h2 {{
            border-bottom: 2px solid #333;
            padding-bottom: 5px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 25px;
        }}

        th, td {{
            border: 1px solid #777;
            padding: 8px;
            text-align: left;
        }}

        th {{
            background-color: #eeeeee;
        }}

        .warning {{
            font-weight: bold;
        }}

        .footer {{
            margin-top: 40px;
            font-size: 12px;
        }}
    </style>
</head>

<body>

<h1>DIGITAL FORENSIC INVESTIGATION REPORT</h1>

<h2>1. Case Information</h2>

<table>
    <tr>
        <th>Case ID</th>
        <td>{safe(case_info["case_id"])}</td>
    </tr>

    <tr>
        <th>Investigator</th>
        <td>{safe(case_info["investigator"])}</td>
    </tr>

    <tr>
        <th>Investigation Date</th>
        <td>{safe(case_info["date"])}</td>
    </tr>

    <tr>
        <th>Evidence Source</th>
        <td>{safe(case_info["source"])}</td>
    </tr>

    <tr>
        <th>Report Generated</th>
        <td>{report_time}</td>
    </tr>
</table>


<h2>2. Evidence Examined</h2>

<table>
    <tr>
        <th>Evidence ID</th>
        <th>Description</th>
        <th>Type</th>
        <th>Hash</th>
    </tr>
"""

    for item in evidence:
        report += f"""
    <tr>
        <td>{safe(item["id"])}</td>
        <td>{safe(item["description"])}</td>
        <td>{safe(item["type"])}</td>
        <td>{safe(item["hash"])}</td>
    </tr>
"""

    report += """
</table>


<h2>3. Investigation Findings</h2>

<table>
    <tr>
        <th>Finding ID</th>
        <th>Description</th>
        <th>Severity</th>
    </tr>
"""

    for finding in findings:
        report += f"""
    <tr>
        <td>{safe(finding["id"])}</td>
        <td>{safe(finding["description"])}</td>
        <td>{safe(finding["severity"])}</td>
    </tr>
"""

    report += """
</table>


<h2>4. Investigation Timeline</h2>

<table>
    <tr>
        <th>Date/Time</th>
        <th>Event</th>
    </tr>
"""

    for event in timeline:
        report += f"""
    <tr>
        <td>{safe(event["time"])}</td>
        <td>{safe(event["event"])}</td>
    </tr>
"""

    report += """
</table>


<h2>5. Conclusion</h2>

<p>
The investigation findings were analyzed based on the available digital
evidence. The evidence, hashes, timestamps, and observed activities have
been documented in this report.
</p>

<p>
This report represents the findings obtained from the examined evidence
and should be interpreted together with the investigation methodology
and supporting forensic artifacts.
</p>


<div class="footer">
    <p>Digital Forensic Investigation Report</p>
    <p>Generated automatically by Python</p>
</div>

</body>
</html>
"""

    # Save report
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(report)

    print("Forensic report generated successfully.")
    print("Report saved as:", output_file)


# -------------------------------------------------------
# Investigation Data
# -------------------------------------------------------

case_info = {
    "case_id": "CASE-2026-001",
    "investigator": "Digital Forensic Investigation Team",
    "date": "2026-08-18",
    "source": "Computer Evidence Image"
}


evidence = [
    {
        "id": "E001",
        "description": "Forensic disk image",
        "type": "Disk Image",
        "hash": "a3f5c8d9e7b123456789abcdef123456"
    },
    {
        "id": "E002",
        "description": "System login log",
        "type": "Log File",
        "hash": "b7e4d12c9876543210abcdef98765432"
    },
    {
        "id": "E003",
        "description": "Suspicious document",
        "type": "File",
        "hash": "c9a81234567890abcdef123456789012"
    }
]


findings = [
    {
        "id": "F001",
        "description": "Multiple failed login attempts were observed.",
        "severity": "HIGH"
    },
    {
        "id": "F002",
        "description": "A suspicious file was found in the evidence.",
        "severity": "MEDIUM"
    },
    {
        "id": "F003",
        "description": "File timestamps indicated unusual activity.",
        "severity": "MEDIUM"
    }
]


timeline = [
    {
        "time": "2026-08-18 09:10:23",
        "event": "Multiple failed login attempts detected"
    },
    {
        "time": "2026-08-18 09:15:41",
        "event": "Suspicious file created"
    },
    {
        "time": "2026-08-18 09:20:12",
        "event": "Forensic evidence acquired"
    }
]


# -------------------------------------------------------
# Generate Report
# -------------------------------------------------------

generate_forensic_report(
    case_info,
    evidence,
    findings,
    timeline,
    "digital_forensic_report.html"
)

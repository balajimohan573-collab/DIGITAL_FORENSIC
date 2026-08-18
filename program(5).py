# Digital Forensic Investigation Lifecycle Report Generator

def generate_report():
    report = """
===========================================================
      DIGITAL FORENSIC INVESTIGATION LIFECYCLE REPORT
===========================================================

1. Identification
-----------------
Objective:
- Detect and identify potential digital evidence.
Activities:
- Identify affected systems and devices.
- Determine the scope of the investigation.
- Obtain legal authorization if required.

2. Preservation
---------------
Objective:
- Protect digital evidence from alteration or damage.
Activities:
- Isolate affected systems.
- Create forensic disk images.
- Maintain chain of custody documentation.

3. Collection (Acquisition)
---------------------------
Objective:
- Securely collect digital evidence.
Activities:
- Acquire data using forensic tools.
- Collect files, logs, memory dumps, and network data.
- Verify integrity using hash values (e.g., MD5, SHA-256).

4. Examination and Analysis
---------------------------
Objective:
- Examine and analyze collected evidence.
Activities:
- Recover deleted files.
- Analyze logs, metadata, and timelines.
- Identify suspicious activities and reconstruct events.

5. Reporting and Presentation
-----------------------------
Objective:
- Present findings in a clear and legally acceptable manner.
Activities:
- Document investigation procedures.
- Summarize evidence and conclusions.
- Present findings to management or in court if necessary.

===========================================================
Conclusion
===========================================================
The five-stage digital forensic investigation lifecycle ensures
that digital evidence is identified, preserved, collected,
analyzed, and reported in a systematic and legally defensible
manner. Following these stages helps maintain evidence integrity
and supports successful investigations.

===========================================================
"""

    # Display the report
    print(report)

    # Save the report to a file
    with open("Digital_Forensics_Report.txt", "w") as file:
        file.write(report)

    print("Report has been successfully saved as 'Digital_Forensics_Report.txt'.")


# Main program
if __name__ == "__main__":
    generate_report()

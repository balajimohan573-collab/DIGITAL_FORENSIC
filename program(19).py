import os


# Common extensions that can be dangerous/suspicious
SUSPICIOUS_EXTENSIONS = {
    ".exe",
    ".scr",
    ".bat",
    ".cmd",
    ".com",
    ".msi",
    ".vbs",
    ".vbe",
    ".js",
    ".jse",
    ".ps1",
    ".jar",
    ".hta",
    ".dll",
}


# Extensions commonly used to disguise files
COMMON_DOCUMENT_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".jpg",
    ".jpeg",
    ".png",
    ".txt",
    ".zip",
}


def analyze_file(filename):

    # Get all extensions in the filename
    parts = filename.lower().split(".")

    if len(parts) < 2:
        return

    extensions = [
        "." + part
        for part in parts[1:]
    ]

    final_extension = extensions[-1]

    # Check for suspicious final extension
    if final_extension in SUSPICIOUS_EXTENSIONS:

        # Check whether there is another extension before it
        if len(extensions) >= 2:

            previous_extension = extensions[-2]

            if previous_extension in COMMON_DOCUMENT_EXTENSIONS:

                print(
                    f"[DOUBLE EXTENSION] {filename}"
                )

                print(
                    f"    Possible disguise: "
                    f"{previous_extension}{final_extension}"
                )

            else:

                print(
                    f"[SUSPICIOUS] {filename}"
                )

        else:

            print(
                f"[SUSPICIOUS] {filename}"
            )


def scan_folder(folder):

    print("\n========== SCAN RESULTS ==========")

    found = False

    for root, directories, files in os.walk(folder):

        for filename in files:

            before = found

            parts = filename.lower().split(".")

            if len(parts) >= 2:

                final_extension = "." + parts[-1]

                if final_extension in SUSPICIOUS_EXTENSIONS:

                    found = True
                    analyze_file(filename)

    if not found:
        print("No suspicious files found.")


# --------------------------------------
# Main Program
# --------------------------------------

print("======================================")
print("   SUSPICIOUS FILE EXTENSION SCANNER")
print("======================================")

folder = input(
    "Enter folder path to scan: "
).strip()

if not os.path.isdir(folder):

    print("Error: Folder does not exist.")

else:

    scan_folder(folder)

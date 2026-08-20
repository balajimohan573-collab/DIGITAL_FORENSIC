import os
import json
import hashlib


BASELINE_FILE = "baseline_hashes.json"


# -----------------------------------------
# Calculate SHA-256 hash of a file
# -----------------------------------------

def calculate_hash(filepath):

    sha256 = hashlib.sha256()

    try:
        with open(filepath, "rb") as file:

            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except (PermissionError, OSError):
        return None


# -----------------------------------------
# Scan folder and create hashes
# -----------------------------------------

def scan_folder(folder):

    hashes = {}

    for root, directories, files in os.walk(folder):

        for filename in files:

            filepath = os.path.join(
                root,
                filename
            )

            # Don't hash the baseline file itself
            if os.path.abspath(filepath) == os.path.abspath(BASELINE_FILE):
                continue

            file_hash = calculate_hash(filepath)

            if file_hash:
                # Store relative path
                relative_path = os.path.relpath(
                    filepath,
                    folder
                )

                hashes[relative_path] = file_hash

    return hashes


# -----------------------------------------
# Create baseline
# -----------------------------------------

def create_baseline(folder):

    print("\nCreating baseline...")

    hashes = scan_folder(folder)

    with open(
        BASELINE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            hashes,
            file,
            indent=4
        )

    print(
        f"Baseline created for {len(hashes)} files."
    )


# -----------------------------------------
# Check for modifications
# -----------------------------------------

def check_integrity(folder):

    if not os.path.exists(BASELINE_FILE):

        print(
            "Baseline not found. "
            "Create a baseline first."
        )

        return

    # Load stored baseline
    with open(
        BASELINE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        old_hashes = json.load(file)

    # Calculate current hashes
    current_hashes = scan_folder(folder)

    print("\n========== INTEGRITY CHECK ==========")

    # -------------------------------------
    # Modified files
    # -------------------------------------

    for filepath in old_hashes:

        if filepath in current_hashes:

            if old_hashes[filepath] != current_hashes[filepath]:

                print(
                    f"[MODIFIED] {filepath}"
                )

    # -------------------------------------
    # Deleted files
    # -------------------------------------

    for filepath in old_hashes:

        if filepath not in current_hashes:

            print(
                f"[DELETED]  {filepath}"
            )

    # -------------------------------------
    # New files
    # -------------------------------------

    for filepath in current_hashes:

        if filepath not in old_hashes:

            print(
                f"[NEW FILE] {filepath}"
            )

    print("\nIntegrity check completed.")


# =========================================
# Main Program
# =========================================

print("======================================")
print("       FILE INTEGRITY MONITOR")
print("======================================")

folder = input(
    "Enter folder path: "
).strip()

if not os.path.isdir(folder):

    print("Error: Folder does not exist.")
    exit()


print("\n1. Create Baseline")
print("2. Check Integrity")

choice = input(
    "\nEnter your choice: "
)


if choice == "1":

    create_baseline(folder)

elif choice == "2":

    check_integrity(folder)

else:

    print("Invalid choice.")

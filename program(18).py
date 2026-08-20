import os
import hashlib


# -----------------------------------------
# Calculate SHA-256 hash of a file
# -----------------------------------------

def calculate_sha256(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except (PermissionError, OSError) as e:
        print(f"Error reading {file_path}: {e}")
        return None


# -----------------------------------------
# Find duplicate files
# -----------------------------------------

def find_duplicates(folder):

    hash_database = {}

    for root, directories, files in os.walk(folder):

        for filename in files:

            file_path = os.path.join(
                root,
                filename
            )

            file_hash = calculate_sha256(
                file_path
            )

            if file_hash is None:
                continue

            if file_hash in hash_database:

                hash_database[file_hash].append(
                    file_path
                )

            else:

                hash_database[file_hash] = [
                    file_path
                ]

    # Display duplicate files
    print("\n========== DUPLICATE FILES ==========")

    duplicate_found = False

    for file_hash, files in hash_database.items():

        if len(files) > 1:

            duplicate_found = True

            print("\nSHA-256:")
            print(file_hash)

            print("Duplicate files:")

            for file_path in files:
                print("  ", file_path)

    if not duplicate_found:
        print("No duplicate files found.")


# -----------------------------------------
# Main Program
# -----------------------------------------

print("========================================")
print("   DIGITAL EVIDENCE DUPLICATE FINDER")
print("========================================")

folder = input(
    "Enter evidence folder path: "
).strip()

if not os.path.isdir(folder):

    print("Error: Folder does not exist.")

else:

    find_duplicates(folder)

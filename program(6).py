import shutil
import hashlib

# Function to calculate SHA-256 hash
def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


# Input and output file names
source_file = input("Enter the source file name: ")
copy_file = input("Enter the forensic copy file name: ")

# Create bit-stream copy
shutil.copyfile(source_file, copy_file)
print("\nForensic copy created successfully.")

# Calculate hashes
original_hash = calculate_hash(source_file)
copy_hash = calculate_hash(copy_file)

# Display hashes
print("\nOriginal File SHA-256 :", original_hash)
print("Copied File SHA-256   :", copy_hash)

# Verify integrity
if original_hash == copy_hash:
    print("\nIntegrity Verification: SUCCESS")
    print("The forensic copy is identical to the original file.")
else:
    print("\nIntegrity Verification: FAILED")
    print("The copied file has been altered or corrupted.")

import hashlib

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    try:
        with open(filename, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


# Get file name from the user
filename = input("Enter the file name: ")

# Calculate the current hash moided
current_hash = calculate_hash(filename)

if current_hash is None:
    print("Error: File not found.")
else:
    print("\nCurrent SHA-256 Hash:")
    print(current_hash)

    # Enter the original hash recorded during evidence collection
    original_hash = input("\nEnter the original SHA-256 hash: ")

    if current_hash == original_hash:
        print("\n✅ Chain of Custody Verified")
        print("The file has NOT been modified.")
    else:
        print("\n❌ Chain of Custody Failed111111111111111")
        print("The file has been altered or corrupted.")
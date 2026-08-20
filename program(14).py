import hashlib
import os

# Digital evidence file
file_path = "evidence.txt"


def calculate_hashes(file_path):
    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            md5_hash.update(data)
            sha1_hash.update(data)
            sha256_hash.update(data)

    return (
        md5_hash.hexdigest(),
        sha1_hash.hexdigest(),
        sha256_hash.hexdigest()
    )


# Check whether file exists
if not os.path.exists(file_path):
    print("Evidence file not found:", file_path)

else:
    md5, sha1, sha256 = calculate_hashes(file_path)

    print("=" * 60)
    print("        DIGITAL EVIDENCE HASH ANALYSIS")
    print("=" * 60)

    print("\nFile:", file_path)
    print("File Size:", os.path.getsize(file_path), "bytes")

    print("\nMD5:")
    print(md5)

    print("\nSHA-1:")
    print(sha1)

    print("\nSHA-256:")
    print(sha256)

    print("\n" + "=" * 60)
    print("HASH COMPARISON")
    print("=" * 60)

    # Example comparison with previously recorded hashes
    original_md5 = md5
    original_sha1 = sha1
    original_sha256 = sha256

    current_md5, current_sha1, current_sha256 = calculate_hashes(
        file_path
    )

    print("\nMD5 Match     :", original_md5 == current_md5)
    print("SHA-1 Match   :", original_sha1 == current_sha1)
    print("SHA-256 Match :", original_sha256 == current_sha256)

    if (
        original_md5 == current_md5
        and original_sha1 == current_sha1
        and original_sha256 == current_sha256
    ):
        print("\nRESULT: Evidence integrity verified.")
    else:
        print("\nRESULT: Evidence may have been modified.")

import os

# File signatures (magic bytes)
FILE_SIGNATURES = {
    "jpg": {
        "start": b"\xFF\xD8\xFF",
        "end": b"\xFF\xD9"
    },
    "png": {
        "start": b"\x89PNG\r\n\x1a\n",
        "end": b"IEND\xaeB`\x82"
    },
    "pdf": {
        "start": b"%PDF",
        "end": b"%%EOF"
    },
    "zip": {
        "start": b"PK\x03\x04",
        "end": None
    }
}


def recover_files(storage_file, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    with open(storage_file, "rb") as storage:
        data = storage.read()

    recovered_count = 0

    for file_type, signature in FILE_SIGNATURES.items():

        start_signature = signature["start"]
        end_signature = signature["end"]

        position = 0

        while True:
            start = data.find(start_signature, position)

            if start == -1:
                break

            # Find the ending signature
            if end_signature:
                end = data.find(end_signature, start + len(start_signature))

                if end == -1:
                    # End signature not found
                    position = start + len(start_signature)
                    continue

                end += len(end_signature)
            else:
                # For ZIP, simulate recovery using a fixed maximum size
                end = min(start + 1024 * 1024, len(data))

            recovered_data = data[start:end]

            filename = f"recovered_{recovered_count + 1}.{file_type}"
            output_path = os.path.join(output_folder, filename)

            with open(output_path, "wb") as recovered_file:
                recovered_file.write(recovered_data)

            print(f"Recovered: {filename}")
            print(f"  Start offset : {start}")
            print(f"  End offset   : {end}")
            print(f"  Size         : {len(recovered_data)} bytes")
            print()

            recovered_count += 1

            position = end

    print(f"Recovery completed.")
    print(f"Total files recovered: {recovered_count}")


# ---------------------------------------------------
# Main program
# ---------------------------------------------------

storage_file = "storage_image.bin"
output_folder = "recovered_files"

if os.path.exists(storage_file):
    recover_files(storage_file, output_folder)
else:
    print(f"Storage image not found: {storage_file}")
    print("Create/copy a storage image as 'storage_image.bin' and run again.")

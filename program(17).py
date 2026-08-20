import os
from datetime import datetime


def get_file_metadata(file_path):

    # Get file information
    file_info = os.stat(file_path)

    # File name
    file_name = os.path.basename(file_path)

    # File size in bytes
    file_size = file_info.st_size

    # Creation time
    creation_time = datetime.fromtimestamp(
        file_info.st_ctime
    )

    # Modification time
    modification_time = datetime.fromtimestamp(
        file_info.st_mtime
    )

    # Access time
    access_time = datetime.fromtimestamp(
        file_info.st_atime
    )

    print("\n========== FILE METADATA ==========")

    print("File Name        :", file_name)
    print("File Size        :", file_size, "bytes")
    print("Creation Time    :", creation_time)
    print("Modification Time:", modification_time)
    print("Access Time      :", access_time)


# --------------------------------------
# Main Program
# --------------------------------------

file_path = input(
    "Enter the file path: "
).strip()

if os.path.isfile(file_path):

    get_file_metadata(file_path)

else:

    print("Error: File does not exist.")

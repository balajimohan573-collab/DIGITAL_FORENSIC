import os
import time

# Enter file name
file_name = input("Enter the file name: ")

if os.path.exists(file_name):

    print("\nFile Metadata")

    created = os.path.getctime(file_name)
    modified = os.path.getmtime(file_name)
    accessed = os.path.getatime(file_name)

    print("Creation Time :", time.ctime(created))
    print("Modified Time :", time.ctime(modified))
    print("Accessed Time :", time.ctime(accessed))

else:
    print("File not found.")

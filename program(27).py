import os
import stat

folder = input("Enter directory path: ").strip().strip('"')

if not os.path.isdir(folder):
    print("Error: Directory does not exist.")
    raise SystemExit

print("\n===== INSECURE FILE PERMISSIONS =====")
found = False

for root, dirs, files in os.walk(folder):
    for name in files:
        path = os.path.join(root, name)

        try:
            mode = os.stat(path).st_mode
            permissions = stat.filemode(mode)

            if mode & stat.S_IWGRP or mode & stat.S_IWOTH:
                found = True
                print("[INSECURE]")
                print("File:", path)
                print("Permissions:", permissions)
                print("--------------------------------")
        except OSError:
            print("Cannot access:", path)

if not found:
    print("No insecure permissions found.")

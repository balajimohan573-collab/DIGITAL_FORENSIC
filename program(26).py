import os

folder = input("Enter directory path: ").strip().strip('"')

if not os.path.isdir(folder):
    print("Error: Directory does not exist.")
    raise SystemExit

print("\n===== HIDDEN / SUSPICIOUS FILES =====")
found = False

for root, dirs, files in os.walk(folder):
    for name in files:
        path = os.path.join(root, name)

        if name.startswith("."):
            found = True
            print("[HIDDEN]", path)

        try:
            attributes = os.stat(path).st_file_attributes
            if attributes & 0x2:
                found = True
                print("[WINDOWS HIDDEN]", path)
            if attributes & 0x4:
                found = True
                print("[SYSTEM FILE]", path)
        except AttributeError:
            pass

if not found:
    print("No hidden or suspicious files found.")

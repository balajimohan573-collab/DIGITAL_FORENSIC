# Python Program to Identify File Type Using Magic Numbers

def identify_file_type(filename):
    # Known file signatures (magic numbers)
    file_signatures = {
        b'\xFF\xD8\xFF': "JPEG Image",
        b'\x89PNG\r\n\x1A\n': "PNG Image",
        b'GIF87a': "GIF Image",
        b'GIF89a': "GIF Image",
        b'%PDF': "PDF Document",
        b'PK\x03\x04': "ZIP Archive / DOCX / XLSX / PPTX",
        b'Rar!\x1A\x07\x00': "RAR Archive",
        b'7z\xBC\xAF\x27\x1C': "7-Zip Archive",
        b'MZ': "Windows Executable (EXE/DLL)"
    }

    try:
        with open(filename, "rb") as file:
            header = file.read(16)  # Read first 16 bytes

        found = False
        for signature, filetype in file_signatures.items():
            if header.startswith(signature):
                print("File Type Detected:", filetype)
                found = True
                break

        if not found:
            print("Unknown file type or unsupported signature.")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error:", e)


# Main Program
filename = input("Enter file name: ")
identify_file_type(filename)

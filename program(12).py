from PIL import Image
from PIL.ExifTags import TAGS

# Image file
image_path = "photo.jpg"

try:
    # Open the image
    image = Image.open(image_path)

    print("=" * 50)
    print("        EXIF METADATA ANALYZER")
    print("=" * 50)

    print("\nImage Information")
    print("-----------------")
    print("File Name :", image.filename)
    print("Format    :", image.format)
    print("Size      :", image.size)
    print("Mode      :", image.mode)

    # Extract EXIF data
    exif_data = image.getexif()

    if not exif_data:
        print("\nNo EXIF metadata found.")
    else:
        print("\nEXIF Metadata")
        print("-------------")

        for tag_id, value in exif_data.items():

            # Convert tag ID into readable name
            tag_name = TAGS.get(tag_id, tag_id)

            print(f"{tag_name}: {value}")

except FileNotFoundError:
    print("Error: Image file not found.")

except Exception as error:
    print("Error:", error)

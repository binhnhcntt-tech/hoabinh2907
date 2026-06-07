import fitz

doc = fitz.open("reports/Bai5.pdf")
page = doc[7] # Page 8
images = page.get_images(full=True)
print(f"Images on Page 8: {images}")

for img in images:
    try:
        rect = page.get_image_bbox(img[7])
        print(f"Image {img[7]} rect: {rect}")
    except Exception as e:
        print(f"Error: {e}")

import fitz

def extract():
    doc = fitz.open("reports/Bai4.pdf")
    img_num = 1
    for page in doc:
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            with open(f"assets/bai4_img{img_num}.png", "wb") as f:
                f.write(image_bytes)
            print(f"Extracted image {img_num}")
            img_num += 1

if __name__ == "__main__":
    extract()

import fitz

def extract_images():
    doc = fitz.open("reports/Bài1.pdf")
    for i in range(5):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        pix.save(f"assets/bai1_page_{i+1}.png")
    print("Snapshot complete")

if __name__ == "__main__":
    extract_images()

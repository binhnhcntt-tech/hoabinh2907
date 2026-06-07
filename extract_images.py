import fitz

def extract_images():
    doc = fitz.open("reports/Bai5.pdf")
    pages_to_extract = {
        1: "bai5_hinh1.png", # Page 2
        3: "bai5_hinh2.png", # Page 4
        5: "bai5_hinh3.png", # Page 6
        6: "bai5_hinh4.png", # Page 7
        7: "bai5_hinh5.png"  # Page 8
    }

    for p, filename in pages_to_extract.items():
        page = doc[p]
        pix = page.get_pixmap(dpi=150)
        pix.save(f"assets/{filename}")
    print("Snapshot complete")

if __name__ == "__main__":
    extract_images()

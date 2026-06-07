import fitz

def extract():
    doc = fitz.open("reports/Bai3.pdf")
    pages_to_extract = [4, 5, 6, 7, 8, 9] # Pages 5 to 10 (0-indexed)
    for p in pages_to_extract:
        if p < len(doc):
            page = doc[p]
            pix = page.get_pixmap(dpi=150)
            pix.save(f"assets/bai3_prompt_page_{p+1}.png")
            print(f"Snapshot saved for page {p+1}")

if __name__ == "__main__":
    extract()

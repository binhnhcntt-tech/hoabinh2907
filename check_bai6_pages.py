import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def check_pdf():
    doc = fitz.open("reports/Bai6.pdf")
    print(f"Total pages: {len(doc)}")
    
    # Check text of page 6, 7, 8 (1-indexed)
    for i in range(5, len(doc)):
        text = doc[i].get_text("text")
        print(f"--- Page {i+1} ---")
        print(text[:200])

if __name__ == "__main__":
    check_pdf()

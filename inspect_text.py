import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect():
    doc = fitz.open("reports/Bai5.pdf")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                text = "".join([span["text"] for line in b["lines"] for span in line["spans"]])
                if "Hình" in text or "hình" in text:
                    print(f"Page {page_num+1} - Caption: {text.strip()} at {b['bbox']}")

if __name__ == "__main__":
    inspect()

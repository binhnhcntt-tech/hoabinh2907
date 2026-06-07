import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect():
    doc = fitz.open("reports/Bai5.pdf")
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        images = page.get_images(full=True)
        if not images:
            continue
            
        print(f"\n--- Page {page_num + 1} ---")
        
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                text = "".join([span["text"] for line in b["lines"] for span in line["spans"]])
                if "Hình" in text or "hình" in text:
                    print(f"Caption: {text.strip()} at {b['bbox']}")
                    
        for img_info in images:
            xref = img_info[0]
            name = img_info[7]
            try:
                rect = page.get_image_bbox(name)
                print(f"Image xref {xref} ({name}) at {rect}")
            except Exception as e:
                print(f"Cannot get bbox for xref {xref}: {e}")

if __name__ == "__main__":
    inspect()

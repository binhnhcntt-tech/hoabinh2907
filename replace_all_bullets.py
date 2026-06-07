import fitz
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdfs = ["Bai2.pdf", "Bai3.pdf", "Bai4.pdf", "Bai5.pdf", "Bai6.pdf"]
base_dir = r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\scratch\portfolio-website\reports"

def process_pdfs():
    for pdf in pdfs:
        path = os.path.join(base_dir, pdf)
        if not os.path.exists(path):
            print(f"{pdf} not found.")
            continue
            
        doc = fitz.open(path)
        vec_count = 0
        text_count = 0
        
        for page in doc:
            # 1. Text bullets
            for char in ['•', '·', '◦', '▪', '●', '\uf0b7', '\u2022', '\u25cf', '\u25e6', '\xad']:
                instances = page.search_for(char)
                if instances:
                    for inst in instances:
                        page.add_redact_annot(inst, text="-", fontname="helv", text_color=(0,0,0), fill=(1,1,1), align=fitz.TEXT_ALIGN_CENTER)
                        text_count += 1
            
            # 2. Vector bullets
            drawings = page.get_drawings()
            for d in drawings:
                rect = d["rect"]
                w = rect.width
                h = rect.height
                if 2.0 < w < 8.0 and 2.0 < h < 8.0 and abs(w - h) < 1.5:
                    if d.get("fill") is not None:
                        # Erase it
                        page.draw_rect(rect, color=(1,1,1), fill=(1,1,1), overlay=True)
                        # Draw dash
                        y_pos = rect.y1 - (h * 0.1)
                        page.insert_text((rect.x0, y_pos), "-", fontname="helv", fontsize=11, color=(0,0,0), overlay=True)
                        vec_count += 1
                        
        if text_count > 0:
            page.apply_redactions()
            
        if vec_count > 0 or text_count > 0:
            out_path = os.path.join(base_dir, pdf.replace(".pdf", "_updated.pdf"))
            doc.save(out_path)
            print(f"{pdf}: Replaced {text_count} text bullets, {vec_count} vector bullets.")
        else:
            print(f"{pdf}: No bullets found.")
            
        doc.close()

if __name__ == "__main__":
    process_pdfs()

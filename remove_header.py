import fitz

def remove_header():
    doc = fitz.open(r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\scratch\portfolio-website\reports\Bai6.pdf")
    page = doc[0]
    
    # Redact the top part of the page from Y=0 to Y=180
    rect = fitz.Rect(0, 0, 595, 180)
    page.draw_rect(rect, color=(1,1,1), fill=(1,1,1), overlay=True)
    
    doc.save(r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\scratch\portfolio-website\reports\Bai6_updated.pdf")
    print("Header removed successfully.")

if __name__ == "__main__":
    remove_header()

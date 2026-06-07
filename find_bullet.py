import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def find_bullet():
    doc = fitz.open(r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\scratch\portfolio-website\reports\Bai6.pdf")
    for page in doc:
        text = page.get_text("text")
        # Check for common bullet characters
        for char in ['•', '·', '◦', '▪', '●', '\uf0b7', '\u2022', '\u25cf', '\u25e6']:
            if char in text:
                print(f"Found character {repr(char)} on page {page.number}")
        
if __name__ == "__main__":
    find_bullet()

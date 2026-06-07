import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\scratch\portfolio-website\reports\Bai6.pdf")
text = doc[0].get_text("text")
print(repr(text[:500]))

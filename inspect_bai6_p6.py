import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_bai6_p6():
    doc = fitz.open("reports/Bai6.pdf")
    # Print text of the page 6
    text = doc[5].get_text("text")
    print("\n--- Text on Page 6 ---")
    print(text)

if __name__ == "__main__":
    inspect_bai6_p6()

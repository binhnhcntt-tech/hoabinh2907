import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_bai6():
    doc = fitz.open("reports/Bai6.pdf")
    print(f"Total pages: {len(doc)}")
    
    # Print text of the last page
    last_page = doc[-1]
    text = last_page.get_text("text")
    print("\n--- Text on Last Page ---")
    print(text)

if __name__ == "__main__":
    inspect_bai6()

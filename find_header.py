import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def find_header():
    doc = fitz.open(r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\scratch\portfolio-website\reports\Bai6.pdf")
    page = doc[0]
    
    # Find text boxes
    instances1 = page.search_for("ĐẠI HỌC QUỐC GIA HÀ NỘI")
    instances2 = page.search_for("TRƯỜNG ĐẠI HỌC CÔNG NGHỆ")
    instances3 = page.search_for("BÁO CÁO BÀI TẬP")
    
    print(f"Inst 1: {instances1}")
    print(f"Inst 2: {instances2}")
    print(f"Inst 3: {instances3}")
    
    # Find drawings (for the horizontal line)
    drawings = page.get_drawings()
    for d in drawings:
        print(f"Drawing Rect: {d['rect']}")

if __name__ == "__main__":
    find_header()

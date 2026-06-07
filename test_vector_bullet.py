import fitz

def test_vector():
    doc = fitz.open(r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\scratch\portfolio-website\reports\Bai6.pdf")
    page = doc[0] # Let's try page 0 or page 1. Wait, Page 2 has bullets maybe? Let's search all pages
    
    count = 0
    for page in doc:
        drawings = page.get_drawings()
        for d in drawings:
            rect = d["rect"]
            w = rect.width
            h = rect.height
            # A bullet point is a small filled shape, typically 2-8 points wide/tall
            if 1 < w < 10 and 1 < h < 10 and abs(w - h) < 1.5:
                # Could be a bullet
                # Check if it has a fill color (usually black)
                if d["fill"] == (0, 0, 0) or d["color"] == (0, 0, 0):
                    print(f"Page {page.number} - Found potential bullet at {rect}, items: {len(d['items'])}")
                    count += 1

    print(f"Total potential bullets found: {count}")

if __name__ == "__main__":
    test_vector()

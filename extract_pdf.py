import fitz

doc = fitz.open("reports/Bai6.pdf")
page = doc[6] # Page 7 (0-indexed)
pix = page.get_pixmap(dpi=300)
pix.save("assets/infographic_bai6.png")
print("Image extracted successfully!")

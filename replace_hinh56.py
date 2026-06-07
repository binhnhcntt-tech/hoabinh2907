import fitz

def replace_hinh56():
    pdf_path = "reports/Bai5.pdf"
    new_image_path = r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\brain\c8517ed1-3672-4955-a032-5c5e0ddbde73\media__1780812611698.png"
    
    doc = fitz.open(pdf_path)
    page = doc[7] # Page 8
    
    # The caption is at y ~ 446.
    # We redact the area above it where the old images are.
    # A4 size is typically 595 x 842.
    # We redact from y=50 to y=440.
    rect_to_clear = fitz.Rect(50, 50, 545, 440)
    page.draw_rect(rect_to_clear, color=(1,1,1), fill=(1,1,1), overlay=True)
    
    # We insert the new image in a nice centered box above the caption.
    # Let's say x from 72 to 523, y from 72 to 435.
    img_rect = fitz.Rect(72, 72, 523, 435)
    page.insert_image(img_rect, filename=new_image_path, overlay=True, keep_proportion=True)
    
    doc.save("reports/Bai5_updated.pdf")
    doc.close()
    print("SUCCESS")

if __name__ == "__main__":
    replace_hinh56()

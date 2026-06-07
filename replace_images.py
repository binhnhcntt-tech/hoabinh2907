import fitz

def replace_images():
    pdf_path = "reports/Bai5.pdf"
    new_image_path = r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\brain\c8517ed1-3672-4955-a032-5c5e0ddbde73\media__1780812611698.png"
    
    doc = fitz.open(pdf_path)
    
    count = 0
    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images()
        for img_info in image_list:
            xref = img_info[0]
            name = img_info[7]
            if xref == 41:
                rect = page.get_image_bbox(name)
                # cover it with white rectangle just in case
                page.draw_rect(rect, color=(1,1,1), fill=(1,1,1), overlay=True)
                # insert new image
                page.insert_image(rect, filename=new_image_path, overlay=True)
                print(f"Replaced on page {page_num + 1}")
                count += 1
                
    doc.save("reports/Bai5_updated.pdf")
    doc.close()
    if count > 0:
        print("SUCCESS")
    else:
        print("FAILED: Image xref 41 not found on any page.")
    
if __name__ == "__main__":
    replace_images()

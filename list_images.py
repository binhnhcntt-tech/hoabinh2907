import fitz
import sys

def list_images(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images()
        for img_info in image_list:
            xref = img_info[0]
            print(f"Page: {page_num + 1}, xref: {xref}, info: {img_info}")

if __name__ == "__main__":
    list_images("reports/Bai5.pdf")

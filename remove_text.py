import fitz

def remove_text_from_pdf():
    try:
        doc = fitz.open("reports/Bai6.pdf")
        page = doc[0]
        
        # Search for the text
        text_to_remove = "Hà Nội, năm 2023"
        text_instances = page.search_for(text_to_remove)
        
        print(f"Found {len(text_instances)} instances")
        
        for inst in text_instances:
            # Add a white rectangle redaction annotation
            page.add_redact_annot(inst, fill=(1, 1, 1))
            
        page.apply_redactions()
        doc.save("reports/Bai6_tmp.pdf")
        doc.close()
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    remove_text_from_pdf()

import fitz

def test_replace():
    doc = fitz.open(r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\scratch\portfolio-website\reports\Bai6.pdf")
    count = 0
    for page in doc:
        # Search for bullet points
        instances = page.search_for("•")
        if instances:
            count += len(instances)
            for inst in instances:
                page.add_redact_annot(inst, text="-", fontname="helv", text_color=(0,0,0), fill=(1,1,1), align=fitz.TEXT_ALIGN_CENTER)
            page.apply_redactions()
            
    doc.save(r"C:\Users\Nguyễn Hòa Bi\.gemini\antigravity\scratch\portfolio-website\reports\Bai6_test.pdf")
    print(f"Replaced {count} bullet points.")

if __name__ == "__main__":
    test_replace()

import subprocess
import os
import fitz

def fix_bai6():
    html_path = os.path.abspath("temp_page2.html")
    pdf_path = os.path.abspath("temp_page2.pdf")
    
    html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
    body {
        font-family: 'Times New Roman', Times, serif;
        line-height: 1.5;
        margin: 2.5cm;
        font-size: 13pt;
        color: #000;
    }
    h2 {
        font-size: 14pt;
        margin-top: 0;
        text-transform: uppercase;
        font-weight: bold;
    }
    p {
        text-align: justify;
        margin-bottom: 12px;
    }
    strong {
        font-weight: bold;
    }
    ul {
        margin-top: 5px;
        margin-bottom: 15px;
        padding-left: 0;
        list-style-type: none;
    }
    li {
        margin-bottom: 8px;
        text-align: justify;
        position: relative;
        padding-left: 20px;
    }
    li::before {
        content: "-";
        position: absolute;
        left: 0;
    }
</style>
</head>
<body>
    <h2>VI. ĐỀ XUẤT GIẢI PHÁP CHO CÁC THÁCH THỨC ĐẠO ĐỨC</h2>
    <p>Để giải quyết triệt để các rủi ro và thách thức về mặt đạo đức khi sử dụng Trí tuệ nhân tạo (AI) trong môi trường học thuật, cần có sự phối hợp đồng bộ từ nhiều phía:</p>
    
    <p><strong>1. Đối với sinh viên và người sử dụng:</strong></p>
    <ul>
        <li>Cần chủ động trang bị <em>"tư duy phản biện số"</em> (Digital Critical Thinking) để tự đánh giá và chắt lọc thông tin do AI tạo ra, tránh việc tiếp nhận thụ động dẫn đến sai lệch kiến thức.</li>
        <li>Luôn tuân thủ nguyên tắc minh bạch: Bất kỳ nội dung nào có sự can thiệp và hỗ trợ của công cụ AI đều cần được trích dẫn và khai báo rõ ràng trong báo cáo hoặc bài luận.</li>
    </ul>

    <p><strong>2. Đối với cơ sở giáo dục và trường đại học:</strong></p>
    <ul>
        <li>Nhà trường không nên cấm đoán cực đoan mà cần xây dựng và ban hành bộ quy chuẩn rõ ràng về việc sử dụng AI, hướng dẫn sinh viên biến AI thành <em>"trợ lý học tập"</em> thay vì công cụ gian lận.</li>
        <li>Thay đổi phương thức đánh giá thi cử: Tập trung nhiều hơn vào các bài thi vấn đáp (VIVA), thuyết trình bảo vệ dự án hoặc các bài tập tư duy phân tích sâu, nơi AI không thể thay thế được năng lực lập luận của con người.</li>
        <li>Nên đưa các khóa học ngắn hạn về đạo đức AI và kỹ năng Đặt câu lệnh (Prompt Engineering) vào chương trình ngoại khóa hoặc chính khóa.</li>
    </ul>

    <p><strong>3. Đối với các nhà phát triển và cung cấp dịch vụ AI:</strong></p>
    <ul>
        <li>Minh bạch hóa các thuật toán và bộ dữ liệu huấn luyện (Training Data) để đảm bảo không vi phạm bản quyền hay chứa đựng các định kiến ngầm (bias) về chủng tộc, giới tính.</li>
        <li>Thiết lập các màng lọc kiểm duyệt thông tin nghiêm ngặt nhằm giảm thiểu hiện tượng "ảo giác AI" (AI Hallucinations) và ngăn chặn việc tạo ra các thông tin giả mạo.</li>
    </ul>
</body>
</html>"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--print-to-pdf=" + pdf_path,
        "--no-pdf-header-footer",
        "file:///" + html_path.replace("\\", "/")
    ]
    
    subprocess.run(cmd, check=True)
    
    doc_main = fitz.open("reports/Bai6.pdf")
    # Delete page 7 (index 6)
    doc_main.delete_page(6)
    
    # Append the new page at the end
    doc_temp = fitz.open(pdf_path)
    doc_main.insert_pdf(doc_temp, from_page=0, to_page=0)
    
    doc_main.save("reports/Bai6_updated2.pdf")
    doc_main.close()
    doc_temp.close()
    print("SUCCESS")

if __name__ == "__main__":
    fix_bai6()

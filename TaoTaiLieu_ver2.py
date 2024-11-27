import os
from anthropic import Anthropic
import json
from dotenv import load_dotenv
load_dotenv()

def read_user_personas(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Không tìm thấy file user personas"

def get_business_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None

def generate_business_plan(client, yeucau):
    prompt = f"""
    Là chuyên gia tư vấn chiến lược kinh doanh, hãy tạo kế hoạch kinh doanh chi tiết cho dịch vụ: {yeucau}

    Yêu cầu chung:
    - Phân tích phải cụ thể, có số liệu minh họa và các chỉ số KPI rõ ràng
    - Đánh giá dựa trên thực tế thị trường Việt Nam
    - Mỗi mục cần có ít nhất 3-4 điểm phân tích chi tiết
    - Tập trung vào tính khả thi và khả năng thực thi
    
    Cấu trúc phân tích theo các mục sau:

    I. Cơ sở lý thuyết
    - Định nghĩa và đặc điểm của mô hình kinh doanh
    - Phân loại và đặc trưng dịch vụ
    
    II. Tiêu chí đánh giá
    - Phân tích tài chính (chi phí, doanh thu, lợi nhuận)
    - Phân tích thị trường và đối thủ
    - Đánh giá nguồn lực cần thiết
    - Các rủi ro chính
    
    III. Quy trình triển khai
    - Các bước chuẩn bị và thực hiện
    - Phương pháp đánh giá và lựa chọn
    - Kế hoạch hành động
    
    IV. Yếu tố bổ trợ
    - Yêu cầu pháp lý
    - Chiến lược marketing
    - Quy trình vận hành
    

    Yêu cầu format:
    - Trình bày theo đúng cấu trúc đề cương
    - Sử dụng bullet points cho các điểm chi tiết
    - Đánh số thứ tự rõ ràng cho các mục
    - Thể hiện số liệu dưới dạng bảng khi cần thiết
    """

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=8192,
            temperature=0.7,
            system="Bạn là chuyên gia tư vấn chiến lược kinh doanh với hơn 15 năm kinh nghiệm trong việc xây dựng và phát triển kế hoạch kinh doanh tại Việt Nam. Bạn am hiểu sâu sắc về thị trường và có khả năng phân tích, đánh giá chi tiết các mô hình kinh doanh.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Lỗi khi gọi API: {str(e)}"
def save_business_plan(content, output_path="TaiLieuTongQuan.txt"):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Đã lưu kế hoạch kinh doanh vào {output_path}")
    except Exception as e:
        print(f"Lỗi khi lưu file: {str(e)}")

def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Không tìm thấy API key")
        return
    
    client = Anthropic(api_key=api_key)
    business_info = get_business_info("yeucau.json")
    yeucau=read_user_personas('yeucau2.txt')
    if business_info:
        business_plan = generate_business_plan(client, yeucau)
        save_business_plan(business_plan)
    else:
        print("Không thể đọc thông tin input")

if __name__ == "__main__":
    main()
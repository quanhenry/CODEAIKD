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
    1. Định nghĩa mô hình kinh doanh dịch vụ
    - Giải thích rõ khái niệm và bản chất của mô hình dịch vụ này
    - Liệt kê và phân tích chi tiết các đặc điểm quan trọng
    - Phân tích các yếu tố cấu thành cốt lõi của mô hình

    2. Phân loại dịch vụ kinh doanh
    - Phân tích các dịch vụ hữu hình liên quan, ví dụ cụ thể
    - Phân tích các dịch vụ vô hình đi kèm, ví dụ cụ thể
    - Đề xuất các dịch vụ kết hợp tạo giá trị gia tăng

    II. Tiêu chí đánh giá
    1. Phân tích tài chính
    - Ước tính chi tiết chi phí đầu tư ban đầu (có số liệu cụ thể)
    - Dự toán chi phí vận hành hàng tháng/năm
    - Dự báo doanh thu và lợi nhuận trong 3 năm đầu
    - Tính toán thời gian hoàn vốn dự kiến

    2. Phân tích thị trường
    - Đánh giá quy mô thị trường hiện tại và tiềm năng (có số liệu)
    - Phân tích chi tiết 3-5 đối thủ cạnh tranh chính
    - Xác định xu hướng phát triển trong 3-5 năm tới
    - Đánh giá các rào cản gia nhập ngành

    3. Đánh giá nguồn lực
    - Xác định yêu cầu về năng lực tài chính
    - Phân tích nhu cầu nhân sự (số lượng, chuyên môn)
    - Liệt kê công nghệ và trang thiết bị cần thiết
    - Đề xuất xây dựng mạng lưới đối tác chiến lược

    4. Phân tích rủi ro
    - Nhận diện và đánh giá các rủi ro tài chính chính
    - Phân tích các rủi ro pháp lý cần lưu ý
    - Đánh giá rủi ro trong vận hành
    - Xác định các rủi ro thị trường tiềm ẩn

    III. Quy trình lựa chọn
    1. Thu thập thông tin
    - Phương pháp nghiên cứu thị trường chi tiết
    - Cách thức khảo sát đối thủ cạnh tranh
    - Phương pháp phân tích khách hàng mục tiêu

    2. So sánh và đánh giá
    - Xây dựng ma trận so sánh các tiêu chí (có thang điểm)
    - Phương pháp cho điểm và đánh giá
    - Cách tính trọng số cho các tiêu chí

    3. Ra quyết định
    - Ma trận SWOT chi tiết
    - Các tiêu chí đánh giá tính khả thi
    - Quy trình lựa chọn phương án tối ưu

    IV. Kế hoạch triển khai
    1. Lập kế hoạch kinh doanh
    - Các mục tiêu cụ thể (SMART)
    - Kế hoạch phân bổ nguồn lực chi tiết
    - Lộ trình thực hiện theo timeline

    2. Quản trị rủi ro
    - Ma trận nhận diện rủi ro
    - Phương pháp đánh giá tác động
    - Các giải pháp phòng ngừa cụ thể

    3. Đo lường hiệu quả
    - Hệ thống KPI chi tiết cho từng mảng
    - Quy trình đánh giá định kỳ
    - Phương pháp điều chỉnh chiến lược

    V. Các yếu tố bổ trợ
    1. Khung pháp lý
    - Danh mục giấy phép cần có
    - Các quy định ngành nghề liên quan
    - Chi tiết nghĩa vụ thuế phải thực hiện

    2. Marketing và bán hàng
    - Chiến lược định vị thương hiệu
    - Kế hoạch marketing chi tiết (online/offline)
    - Chính sách bán hàng và khuyến mãi

    3. Quản trị vận hành
    - Quy trình cung ứng dịch vụ chi tiết
    - Hệ thống quản lý chất lượng
    - Quy trình chăm sóc khách hàng

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
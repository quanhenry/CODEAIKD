import os
from anthropic import Anthropic
import json
from dotenv import load_dotenv
load_dotenv()

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Không tìm thấy file tai lieu"

def get_business_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None

def generate_business_plan(client,idea_documents, business_info):
    prompt = f"""
    Dựa vào thông tin:
    THÔNG TIN Ý TƯỞNG KINH DOANH:
    Yêu cầu của khách hàng: {business_info['idea']}
    Vốn sẵn có: {business_info['capital']}
    Địa điểm kinh doanh: {business_info['business_location']}
    Đơn vị tiền tệ: {business_info['currency']}
    Tên dự án {business_info['name_startup']}
    
    Tài liệu Thiết kế và phát triển sản phẩm:
    {idea_documents}

    Hãy tạo tiếp quy trình vận hành chi tiết theo cấu trúc sau:
    
    IV. XÂY DỰNG QUY TRÌNH VẬN HÀNH

    1. Thiết lập quy trình sản xuất/cung ứng

    1.1. Xác định các bước sản xuất hiệu quả

    Lập sơ đồ quy trình sản xuất tổng thể
    Phân tích từng công đoạn sản xuất
    Xác định thời gian cho mỗi bước
    Tính toán công suất sản xuất
    Lập kế hoạch sản xuất
    Kiểm soát chất lượng
    Quản lý tồn kho nguyên vật liệu
    Quản lý thành phẩm

    1.2. Tối ưu hóa quy trình

    Phân tích điểm nghẽn
    Cải tiến quy trình liên tục
    Áp dụng công nghệ tự động hóa
    Giảm thiểu lãng phí
    Tối ưu thời gian sản xuất
    Tiết kiệm nguyên vật liệu
    Nâng cao năng suất
    Đảm bảo an toàn lao động

    2. Quản lý chuỗi cung ứng

    2.1. Tìm kiếm và quản lý nhà cung cấp

    Xây dựng danh sách nhà cung cấp tiềm năng
    Đánh giá năng lực nhà cung cấp
    Đàm phán và ký kết hợp đồng
    Theo dõi hiệu suất giao hàng
    Quản lý quan hệ đối tác
    Xử lý khiếu nại và tranh chấp
    Đánh giá định kỳ
    Phát triển nhà cung cấp

    2.2. Thiết lập tiêu chuẩn lựa chọn

    Tiêu chuẩn chất lượng sản phẩm
    Năng lực sản xuất
    Độ tin cậy giao hàng
    Giá cả cạnh tranh
    Điều khoản thanh toán
    Chính sách bảo hành
    Chứng nhận và giấy phép
    Uy tín trên thị trường

    2.3. Đảm bảo chất lượng và thời gian

    Quy trình kiểm tra chất lượng
    Lịch trình giao hàng
    Kế hoạch dự phòng
    Quản lý hàng tồn kho
    Xử lý hàng lỗi/hỏng
    Theo dõi thời gian vận chuyển
    Đánh giá độ hài lòng
    Cải tiến liên tục

    2.4. KPI cho nhà cung cấp

    Tỷ lệ giao hàng đúng hẹn
    Tỷ lệ sản phẩm đạt chuẩn
    Thời gian xử lý đơn hàng
    Khả năng đáp ứng đơn gấp
    Chi phí vận chuyển
    Tỷ lệ hoàn thành đơn hàng
    Thời gian xử lý khiếu nại
    Mức độ hợp tác

    3. Đào tạo nhân viên

    3.1. Đào tạo về sản phẩm

    Kiến thức sản phẩm
    Quy trình sản xuất
    Tiêu chuẩn chất lượng
    Cách sử dụng và bảo quản
    Xử lý sự cố
    Chính sách bảo hành
    Điểm khác biệt sản phẩm
    Phản hồi khách hàng

    3.2. Tài liệu đào tạo

    Sổ tay nhân viên
    Tài liệu kỹ thuật
    Video hướng dẫn
    Bài kiểm tra đánh giá
    Case studies
    Tài liệu tham khảo
    Cập nhật kiến thức mới
    Thư viện số

    3.3. Quy trình làm việc và SOP

    Quy trình vận hành chuẩn
    Hướng dẫn công việc chi tiết
    Checklist kiểm tra
    Biểu mẫu báo cáo
    Quy trình xử lý sự cố
    Quy định an toàn
    Quy tắc ứng xử
    Đánh giá tuân thủ

    3.4. Kỹ năng cần thiết

    Kỹ năng chuyên môn
    Kỹ năng vận hành thiết bị
    Kỹ năng quản lý thời gian
    Kỹ năng giải quyết vấn đề
    Kỹ năng làm việc nhóm
    Kỹ năng báo cáo
    Kỹ năng an toàn lao động
    Kỹ năng kiểm soát chất lượng

    3.5. Kỹ năng mềm

    Giao tiếp hiệu quả
    Xử lý tình huống
    Quản lý stress
    Tư duy tích cực
    Thích nghi thay đổi
    Khả năng học hỏi
    Tổ chức và sắp xếp
    Tinh thần trách nhiệm

    3.6. Đánh giá và phát triển

    Đánh giá định kỳ
    Theo dõi tiến bộ
    Kế hoạch phát triển cá nhân
    Chương trình mentoring
    Cơ hội thăng tiến
    Chế độ đãi ngộ
    Ghi nhận thành tích
    Đào tạo nâng cao
    
    LƯU Ý:
    - Phân tích chi tiết và cụ thể cho từng mục
    - Đưa ra các số liệu và chỉ số KPI cụ thể khi cần thiết
    - Tập trung vào tính khả thi và khả năng thực thi
    - Format kết quả theo đúng cấu trúc đã cho
    - Chỉ trả về nội dung kế hoạch, không giải thích thêm
    """
    
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=8000,
            temperature=0.7,
            system="Bạn là chuyên gia tư vấn chiến lược kinh doanh với nhiều năm kinh nghiệm trong việc xây dựng và phát triển kế hoạch kinh doanh.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text
    except Exception as e:
        return f"Lỗi khi gọi API: {str(e)}"

def save_business_plan(content, output_path="4_quy_trinh_van_hanh.txt"):
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
    idea_documents = read_file('3_Thiet_ke_va_phat_trien.txt')
    if business_info or idea_documents:
        business_plan = generate_business_plan(client,idea_documents, business_info)
        save_business_plan(business_plan)
    else:
        print("Không thể đọc thông tin input")

if __name__ == "__main__":
    main()
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

def generate_business_plan(client,business_plan, business_info):
    prompt = f"""
    Dựa vào thông tin:
    THÔNG TIN Ý TƯỞNG KINH DOANH:
    Yêu cầu của khách hàng: {business_info['idea']}
    Vốn sẵn có: {business_info['capital']}
    Địa điểm kinh doanh: {business_info['business_location']}
    Đơn vị tiền tệ: {business_info['currency']}
    Tên dự án {business_info['name_startup']}
    
    Tài liệu Kế hoạch kinh doanh:
    {business_plan}

    Hãy tạo tiếp Thiết kế và phát triển sản phẩm chi tiết theo cấu trúc sau:
    
    III. THIẾT KẾ VÀ PHÁT TRIỂN SẢN PHẨM

    1. Phát triển mẫu thử

    1.1. Tạo mẫu thử hoặc bản mẫu sản phẩm

    Xây dựng prototype phiên bản alpha
    Tạo bản mẫu tối thiểu có tính năng cốt lõi (MVP)
    Phát triển các phiên bản thử nghiệm khác nhau
    Tối ưu hóa quy trình sản xuất mẫu
    Đánh giá chi phí sản xuất mẫu

    1.2. Sử dụng công nghệ tiên tiến

    Ứng dụng công nghệ mới nhất trong ngành
    Tích hợp các giải pháp tự động hóa
    Sử dụng phần mềm thiết kế chuyên nghiệp
    Áp dụng quy trình kiểm soát chất lượng hiện đại
    Triển khai hệ thống quản lý dữ liệu

    1.3. Tiêu chí mẫu thử hoặc bản mẫu sản phẩm đạt chuẩn

    Đáp ứng các tiêu chuẩn kỹ thuật ngành
    Tuân thủ quy định an toàn và pháp lý
    Đảm bảo tính ổn định và độ bền
    Phù hợp với yêu cầu người dùng
    Khả năng sản xuất hàng loạt
    Chi phí sản xuất tối ưu
    Thời gian sản xuất hợp lý

    1.4. Kiểm tra và nhận phản hồi từ người dùng

    Xây dựng kế hoạch thử nghiệm chi tiết
    Thiết kế bộ câu hỏi khảo sát
    Thu thập dữ liệu định lượng và định tính
    Phân tích hành vi người dùng
    Đánh giá mức độ hài lòng
    Ghi nhận các vấn đề gặp phải
    Tổng hợp ý kiến cải tiến

    1.5. Tổ chức nhóm thử nghiệm

    Lựa chọn đối tượng thử nghiệm phù hợp
    Phân chia nhóm theo đặc điểm người dùng
    Xây dựng kịch bản thử nghiệm
    Thiết lập môi trường thử nghiệm
    Đào tạo nhóm thử nghiệm
    Giám sát quá trình thử nghiệm
    Thu thập phản hồi có hệ thống

    2. Điều chỉnh và cải tiến

    2.1. Dựa vào phản hồi

    Phân loại các loại phản hồi
    Ưu tiên các vấn đề cần giải quyết
    Đánh giá tính khả thi của đề xuất
    Lập kế hoạch cải tiến
    Theo dõi tiến độ thực hiện
    Đánh giá hiệu quả sau cải tiến

    2.2. Xác định điểm cần cải tiến

    Phân tích dữ liệu phản hồi
    Xác định các điểm yếu cần khắc phục
    Đề xuất giải pháp cải tiến
    Ước tính nguồn lực cần thiết
    Lập lộ trình cải tiến
    Thiết lập KPI đánh giá
    Xây dựng quy trình kiểm soát chất lượng mới

    2.3. Quy trình cải tiến liên tục

    Thiết lập hệ thống theo dõi chất lượng
    Định kỳ đánh giá và cập nhật
    Tổ chức họp review định kỳ
    Cập nhật tài liệu kỹ thuật
    Đào tạo nhân viên về quy trình mới
    Đo lường hiệu quả cải tiến
    Tối ưu hóa quy trình sản xuất

    2.4. Kiểm soát phiên bản

    Quản lý các phiên bản sản phẩm
    Lưu trữ tài liệu thiết kế
    Theo dõi lịch sử thay đổi
    Đánh giá hiệu quả từng phiên bản
    Lập kế hoạch nâng cấp
    Quản lý rủi ro khi thay đổi
    Đảm bảo tính tương thích
    
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

def save_business_plan(content, output_path="3_Thiet_ke_va_phat_trien.txt"):
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
    idea_documents = read_file('2_ke_hoach_kinh_doanh.txt')
    if business_info or idea_documents:
        business_plan = generate_business_plan(client,idea_documents, business_info)
        save_business_plan(business_plan)
    else:
        print("Không thể đọc thông tin input")

if __name__ == "__main__":
    main()
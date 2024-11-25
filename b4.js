require("dotenv").config();
const fs = require("fs").promises;
const Anthropic = require("@anthropic-ai/sdk");

async function readFile(filePath) {
  try {
    const data = await fs.readFile(filePath, "utf-8");
    return data;
  } catch (error) {
    return "Không tìm thấy file tai lieu";
  }
}

async function getBusinessInfo(filePath) {
  try {
    const data = await fs.readFile(filePath, "utf-8");
    return JSON.parse(data);
  } catch (error) {
    return null;
  }
}

async function generateBusinessPlan(client, ideaDocuments, businessInfo) {
  const prompt = `
    Dựa vào thông tin:
    THÔNG TIN Ý TƯỞNG KINH DOANH:
    Yêu cầu của khách hàng: ${businessInfo.idea}
    Vốn sẵn có: ${businessInfo.capital}
    Địa điểm kinh doanh: ${businessInfo.business_location}
    Đơn vị tiền tệ: ${businessInfo.currency}
    Tên dự án ${businessInfo.name_startup}
    
    Tài liệu Thiết kế và phát triển sản phẩm:
    ${ideaDocuments}

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
    `;

  try {
    const response = await client.messages.create({
      model: "claude-3-5-sonnet-20240620",
      max_tokens: 8000,
      temperature: 0.7,
      system:
        "Bạn là chuyên gia tư vấn chiến lược kinh doanh với nhiều năm kinh nghiệm trong việc xây dựng và phát triển kế hoạch kinh doanh.",
      messages: [{ role: "user", content: prompt }],
    });
    return response.content[0].text;
  } catch (error) {
    return `Lỗi khi gọi API: ${error.message}`;
  }
}

async function saveBusinessPlan(
  content,
  outputPath = "4_quy_trinh_van_hanh.txt"
) {
  try {
    await fs.writeFile(outputPath, content, "utf-8");
    console.log(`Đã lưu kế hoạch kinh doanh vào ${outputPath}`);
  } catch (error) {
    console.error(`Lỗi khi lưu file: ${error.message}`);
  }
}

async function main() {
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    console.log("Không tìm thấy API key");
    return;
  }

  const client = new Anthropic({ apiKey });

  try {
    const businessInfo = await getBusinessInfo("yeucau.json");
    const ideaDocuments = await readFile("3_Thiet_ke_va_phat_trien.txt");

    if (businessInfo || ideaDocuments) {
      const operationPlan = await generateBusinessPlan(
        client,
        ideaDocuments,
        businessInfo
      );
      await saveBusinessPlan(operationPlan);
    } else {
      console.log("Không thể đọc thông tin input");
    }
  } catch (error) {
    console.error("Lỗi trong quá trình thực thi:", error.message);
  }
}

main().catch(console.error);

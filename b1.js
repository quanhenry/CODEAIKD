// npm install dotenv @anthropic-ai/sdk
require("dotenv").config();
const fs = require("fs").promises;
const Anthropic = require("@anthropic-ai/sdk");

async function readUserPersonas(filePath) {
  try {
    const data = await fs.readFile(filePath, "utf-8");
    return data;
  } catch (error) {
    return "Không tìm thấy file user personas";
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

async function generateBusinessPlan(client, businessInfo) {
  const prompt = `
    Dựa vào thông tin:
    THÔNG TIN Ý TƯỞNG KINH DOANH:
    Yêu cầu của khách hàng: ${businessInfo.idea}
    Vốn sẵn có: ${businessInfo.capital}
    Địa điểm kinh doanh: ${businessInfo.business_location}
    Đơn vị tiền tệ: ${businessInfo.currency}
    Tên dự án ${businessInfo.name_startup}

    Hãy tạo kế hoạch chiến lược kinh doanh chi tiết theo cấu trúc sau:
    
    I. XÁC ĐỊNH Ý TƯỞNG KINH DOANH

    0. Phân tích sơ bộ ý tưởng kinh doanh

    Tóm tắt ý tưởng cốt lõi
    Đánh giá tính độc đáo/sáng tạo
    Xác định giá trị mang lại
    Dự kiến mô hình kinh doanh
    Phân tích sơ bộ tính khả thi
    Xác định nguồn lực cần thiết
    Dự kiến thời gian triển khai

    1. Nghiên cứu thị trường

    1.0. Tổng quan thị trường

    Quy mô thị trường hiện tại
    Tốc độ tăng trưởng ngành
    Các đối thủ cạnh tranh chính
    Rào cản gia nhập ngành
    Các quy định pháp lý liên quan
    Xu hướng công nghệ mới
    Dự báo phát triển thị trường

    1.1. Xác định nhu cầu của khách hàng

    a. Các vấn đề chưa được giải quyết

    Khảo sát pain points hiện tại
    Phân tích nguyên nhân gốc rễ
    Đánh giá mức độ cấp thiết
    Xác định tần suất gặp phải
    Chi phí giải quyết hiện tại
    Tác động đến người dùng
    Cơ hội kinh doanh tiềm năng

    b. Các xu hướng thị trường

    Xu hướng công nghệ mới
    Thay đổi hành vi người dùng
    Xu hướng tiêu dùng xanh
    Ảnh hưởng của mạng xã hội
    Tác động của đại dịch
    Thay đổi nhân khẩu học
    Dự báo xu hướng tương lai

    1.2. Phân tích hành vi mua sắm

    a. Các hành vi mua sắm của khách hàng

    Thời điểm mua sắm
    Địa điểm mua sắm ưa thích
    Tần suất mua sắm
    Giá trị đơn hàng trung bình
    Phương thức thanh toán
    Ảnh hưởng của quảng cáo
    Yếu tố quyết định mua hàng

    b. Phân tích các hành vi mua sắm

    Động cơ mua hàng
    Quá trình ra quyết định
    Người ảnh hưởng đến quyết định
    Các rào cản mua hàng
    Mức độ trung thành thương hiệu
    Hành vi sau mua hàng
    Tỷ lệ mua lại

    c. Khoảng trống thị trường

    Nhu cầu chưa được đáp ứng
    Phân khúc bị bỏ quên
    Cơ hội từ công nghệ mới
    Thị trường ngách tiềm năng
    Khu vực địa lý chưa khai thác
    Điểm yếu của đối thủ
    Cơ hội từ xu hướng mới

    d. Xu hướng công nghệ và tiêu dùng

    Công nghệ mới trong ngành
    Thay đổi thói quen tiêu dùng
    Ảnh hưởng của số hóa
    Xu hướng thanh toán mới
    Tác động của AI/ML
    Xu hướng tiêu dùng bền vững
    Dự báo công nghệ tương lai

    2. Đánh giá tiềm năng

    2.1. Phân tích tính khả thi

    a. Phân tích tính khả thi

    Khả thi về mặt kỹ thuật
    Khả thi về tài chính
    Khả thi về nhân sự
    Khả thi về pháp lý
    Khả thi về thị trường
    Thời gian triển khai
    Rủi ro tiềm ẩn

    b. Lợi thế cạnh tranh

    Công nghệ độc quyền
    Kinh nghiệm đội ngũ
    Mạng lưới đối tác
    Chi phí cạnh tranh
    Chất lượng sản phẩm
    Dịch vụ khách hàng
    Thương hiệu/Uy tín

    c. Tiềm năng phát triển

    Khả năng mở rộng thị trường
    Cơ hội phát triển sản phẩm mới
    Tiềm năng xuất khẩu
    Khả năng số hóa
    Cơ hội hợp tác chiến lược
    Tiềm năng tăng trưởng doanh thu
    Khả năng thu hút đầu tư

    2.2. Đánh giá nguồn lực hiện có

    a. Nguồn lực hiện có

    Nguồn vốn sẵn có
    Đội ngũ nhân sự
    Cơ sở vật chất
    Công nghệ/thiết bị
    Mạng lưới đối tác
    Kinh nghiệm ngành
    Tài sản trí tuệ

    b. USP (Unique Selling Proposition)

    Điểm độc đáo của sản phẩm
    Giá trị cốt lõi
    Lợi ích khác biệt
    Định vị thương hiệu
    Thông điệp marketing
    Chiến lược định giá
    Kênh phân phối đặc thù

    c. Phân tích thị phần

    Thị phần hiện tại
    Đối thủ cạnh tranh chính
    Tốc độ tăng trưởng thị phần
    Phân bố địa lý
    Kênh phân phối
    Chiến lược marketing
    Dự báo thị phần

    3. Xác định đối tượng khách hàng

    3.1. Phân khúc khách hàng mục tiêu

    a. Xác định phân khúc

    Tiêu chí phân khúc
    Đặc điểm nhân khẩu học
    Hành vi tiêu dùng
    Nhu cầu đặc thù
    Khả năng chi trả
    Kênh tiếp cận
    Mức độ trung thành

    b. Điều chỉnh sản phẩm/dịch vụ

    Tính năng sản phẩm
    Mức giá phù hợp
    Kênh phân phối
    Chiến lược marketing
    Dịch vụ hậu mãi
    Chương trình khuyến mãi
    Hỗ trợ khách hàng

    3.2. Xây dựng chân dung khách hàng

    a. Chân dung khách hàng mục tiêu

    Thông tin cá nhân
    Nghề nghiệp/Thu nhập
    Sở thích/Thói quen
    Pain points
    Động cơ mua hàng
    Quy trình ra quyết định
    Kênh tiếp cận thông tin

    b. Thiết kế sản phẩm theo nhu cầu

    Tính năng cốt lõi
    Giao diện sử dụng
    Trải nghiệm khách hàng
    Dịch vụ đi kèm
    Giá trị cảm xúc
    Điểm khác biệt
    Phương thức giao hàng
    
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
      max_tokens: 8192,
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
  outputPath = "1_xac_dinh_y_tuong.txt"
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
  const businessInfo = await getBusinessInfo("yeucau.json");

  if (businessInfo) {
    const businessPlan = await generateBusinessPlan(client, businessInfo);
    await saveBusinessPlan(businessPlan);
  } else {
    console.log("Không thể đọc thông tin input");
  }
}

main().catch(console.error);

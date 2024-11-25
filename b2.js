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
    
    Tài liệu Xác định ý tưởng kinh doanh:
    ${ideaDocuments}

    Hãy tạo tiếp kế hoạch chiến lược kinh doanh chi tiết theo cấu trúc sau:
    
    II. LẬP KẾ HOẠCH KINH DOANH

    1. Mô tả sản phẩm/dịch vụ

    1.1. Chi tiết về sản phẩm/dịch vụ cung cấp

    Danh mục sản phẩm/dịch vụ
    Đặc điểm kỹ thuật chi tiết
    Quy cách đóng gói/trình bày
    Tiêu chuẩn chất lượng
    Hạn sử dụng/bảo hành
    Dịch vụ hậu mãi
    Chính sách đổi trả
    Quy trình sử dụng

    1.2. Những điểm khác biệt

    Công nghệ/nguyên liệu độc đáo
    Thiết kế sáng tạo
    Trải nghiệm người dùng
    Tính năng đặc biệt
    Giá trị cảm xúc
    Dịch vụ khách hàng
    Chính sách bảo hành
    Cam kết chất lượng

    1.3. Tính năng chính

    Tính năng cốt lõi
    Tính năng nâng cao
    Khả năng tùy biến
    Hiệu suất hoạt động
    Độ bền/độ ổn định
    Khả năng mở rộng
    Tương thích hệ thống
    An toàn bảo mật

    1.4. Công nghệ độc quyền

    Bằng sáng chế
    Quy trình sản xuất riêng
    Công thức độc quyền
    Phần mềm/thuật toán
    Thiết kế công nghiệp
    Bí quyết kỹ thuật
    Nghiên cứu phát triển
    Đối tác công nghệ

    1.5. So sánh với sản phẩm hiện có

    Phân tích đối thủ cạnh tranh
    So sánh tính năng
    So sánh giá cả
    So sánh chất lượng 
    So sánh dịch vụ
    Ưu điểm vượt trội
    Nhược điểm cần cải thiện
    Chiến lược định vị

    2. Kế hoạch tiếp thị và bán hàng

    2.1. Chiến lược quảng cáo

    Mục tiêu quảng cáo
    Ngân sách quảng cáo
    Kênh quảng cáo online
    Kênh quảng cáo offline
    Lịch trình quảng cáo
    KPIs quảng cáo
    Đo lường hiệu quả
    Điều chỉnh chiến dịch

    2.2. Truyền thông

    Chiến lược PR
    Content marketing
    Social media
    Email marketing
    Event marketing
    Influencer marketing
    Brand storytelling
    Crisis management

    2.3. Kênh phân phối

    Kênh bán hàng trực tiếp
    Kênh bán hàng online
    Đại lý/nhà phân phối
    Cửa hàng bán lẻ
    Marketplace
    B2B partnerships
    Franchise
    Xuất khẩu

    2.4. Ngân sách tiếp thị

    Chi phí quảng cáo
    Chi phí PR
    Chi phí sự kiện
    Chi phí marketing online
    Chi phí sales
    Chi phí khuyến mãi
    Chi phí nghiên cứu thị trường
    Dự phòng

    2.5. Thông điệp chính

    Unique Value Proposition
    Brand positioning
    Slogan/tagline
    Key messages
    Tone of voice
    Visual identity
    Brand guidelines
    Communication strategy

    3. Phân tích tài chính

    3.1. Dự toán chi phí

    a. Cấu trúc chi phí

    Chi phí cố định
    Chi phí biến đổi
    Chi phí vận hành
    Chi phí marketing
    Chi phí nhân sự
    Chi phí quản lý
    Chi phí đầu tư
    Chi phí dự phòng

    b. Chỉ số tài chính

    Lợi nhuận gộp
    Lợi nhuận ròng
    Biên lợi nhuận
    ROI
    Break-even point
    Payback period
    NPV/IRR
    Cash conversion cycle

    c. Kế hoạch ngân sách

    Ngân sách hoạt động
    Ngân sách đầu tư
    Ngân sách marketing
    Ngân sách R&D
    Dự phòng rủi ro
    Phân bổ theo quý
    Điều chỉnh theo mùa
    KPIs tài chính

    d. Nguồn vốn

    Vốn chủ sở hữu
    Vốn vay ngân hàng
    Vốn đầu tư
    Grants/subsidies
    Crowdfunding
    Angel investors
    Venture capital
    Strategic partners

    3.2. Phân tích tài chính chi tiết

    a. Chi phí cố định

    Tiền thuê mặt bằng
    Lương nhân viên cố định
    Khấu hao tài sản
    Bảo hiểm
    Phí quản lý
    Tiện ích cơ bản
    Phần mềm/licenses
    Bảo trì định kỳ

    b. Dự báo tài chính

    Dự báo doanh thu
    Dự báo chi phí
    Dự báo lợi nhuận
    Dự báo cash flow
    Dự báo thị phần
    Kế hoạch tăng trưởng
    Kịch bản tài chính
    Phân tích nhạy cảm

    c. Quản lý dòng tiền

    Cash flow forecast
    Working capital
    Inventory management
    Account receivables
    Account payables
    Cash conversion cycle
    Treasury management
    Emergency fund

    d. Phân bổ ngân sách

    Tỷ lệ chi phí/doanh thu
    Phân bổ theo bộ phận
    Phân bổ theo dự án
    Phân bổ theo sản phẩm
    Phân bổ theo khu vực
    Phân bổ theo mùa vụ
    Điều chỉnh linh hoạt
    Kiểm soát chi phí
    
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
  outputPath = "2_ke_hoach_kinh_doanh.txt"
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
    const ideaDocuments = await readFile("1_xac_dinh_y_tuong.txt");

    if (businessInfo || ideaDocuments) {
      const businessPlan = await generateBusinessPlan(
        client,
        ideaDocuments,
        businessInfo
      );
      await saveBusinessPlan(businessPlan);
    } else {
      console.log("Không thể đọc thông tin input");
    }
  } catch (error) {
    console.error("Lỗi trong quá trình thực thi:", error.message);
  }
}

main().catch(console.error);

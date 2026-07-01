import streamlit as st
import base64
import os

# ==============================================================================
# CẤU HÌNH TRANG WEB & LOGO
# ==============================================================================
st.set_page_config(page_title="APP CHO VAY ONLINE KHCN - ĐỀ TÀI NHÓM 6", layout="wide")

# Đường link Logo (Có thể thay thế bằng link logo Trường hoặc Ngân hàng của bạn)
URL_LOGO = "tài chính.png" 

# Hiển thị Logo và thông tin tại thanh Sidebar bên trái
st.sidebar.image(URL_LOGO, use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.write("### 🏢 Hệ thống trực tuyến")
st.sidebar.info("Cổng Đăng Ký Khoản Vay Tự Động- NHÓM 6")
st.sidebar.markdown("---")
st.sidebar.caption("Ứng dụng tự động thẩm định hồ sơ đăng ký vay trực tuyến của Khách hàng.")

# Hàm mã hóa ảnh sang chuỗi base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# ==============================================================================
# CẤU HÌNH HÌNH NỀN & MÀU CHỮ NỔI BẬT CHO TOÀN BỘ APP (XINH.JPG)
# ==============================================================================
img_body_base64 = get_base64_image("xinh.jpg")

if img_body_base64:
    body_bg_css = f"""
    <style>
    /* 1. Thiết lập hình nền cho toàn bộ ứng dụng */
    .stApp {{
        background-image: url('data:image/jpeg;base64,{img_body_base64}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 2. Chỉnh chữ của các tiêu đề mục (Subheader) nổi bật */
    h2, h3, [data-testid="stMarkdownContainer"] h2, [data-testid="stMarkdownContainer"] h3 {{
        color: #0a3613 !important; 
        font-weight: bold !important;
        text-shadow: 1px 1px 3px rgba(255, 255, 255, 1) !important; 
    }}
    
    /* 3. Chỉnh chữ của các nhãn nhập liệu (Labels) rõ ràng */
    label, [data-testid="stWidgetLabel"] p {{
        color: #08210d !important; 
        font-weight: 600 !important;
        font-size: 15px !important;
    }}
    
    /* 4. Tạo lớp nền trắng mờ nhẹ cho các phần nhập liệu chung để dễ đọc chữ */
    div[data-testid="stForm"], .stAlert {{
        background-color: rgba(255, 255, 255, 0.45) !important; 
        padding: 15px;
        border-radius: 10px;
        backdrop-filter: blur(3px);
    }}
    </style>
    """
    st.markdown(body_bg_css, unsafe_allow_html=True)

# ==============================================================================
# TIÊU ĐỀ CHÍNH CỦA ỨNG DỤNG (HACK BANNER BACKGROUND)
# ==============================================================================
img_banner_base64 = get_base64_image("bìa.jpg")

if img_banner_base64:
    banner_html = f"""
    <div style="
        background-image: url('data:image/jpeg;base64,{img_banner_base64}');
        background-size: cover;
        background-position: center;
        padding: 45px 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: inset 0 0 0 2000px rgba(10, 50, 20, 0.4);
    ">
        <h1 style="color: #ffffff; font-family: 'Segoe UI', Arial, sans-serif; font-size: 34px; font-weight: 800; text-shadow: 2px 2px 8px rgba(0,0,0,0.8); margin-bottom: 12px; letter-spacing: 0.5px;">
            🏦 ĐĂNG KÝ VÀ KIỂM TRA ĐIỀU KIỆN VAY VỐN TRỰC TUYẾN
        </h1>
        <p style="color: #e8f5e9; font-family: Arial, sans-serif; font-size: 17px; font-weight: 600; text-shadow: 1px 1px 4px rgba(0,0,0,0.7); margin: 0;">
            Vui lòng điền đầy đủ và trung thực các thông tin dưới đây. Hệ thống sẽ tự động chấm điểm và trả kết quả sau 3 giây.
        </p>
    </div>
    """
    st.markdown(banner_html, unsafe_allow_html=True)
else:
    st.title("🏦 ĐĂNG KÝ VÀ KIỂM TRA ĐIỀU KIỆN VAY VỐN TRỰC TUYẾN")
    st.write("Vui lòng điền đầy đủ và trung thực các thông tin dưới đây. Hệ thống sẽ tự động chấm điểm và trả kết quả sau 3 giây.")

st.markdown("---")

# ==============================================================================
# PHẦN 1: THÔNG TIN ĐỊNH DANH KHÁCH HÀNG (HỌ TÊN, CCCD, ĐỊA CHỈ)
# ==============================================================================
st.subheader("🪪 1. Thông tin định danh cá nhân")
col_id1, col_id2, col_id3 = st.columns([1.5, 1.5, 2])

with col_id1:
    ho_ten = st.text_input("Họ và chữ lót, Tên của bạn:", value="Nguyễn Văn A")
with col_id2:
    cccd = st.text_input("Số Căn cước công dân (CCCD - 12 số):", value="012345678901")
with col_id3:
    dia_chi = st.text_input("Địa chỉ cư trú hiện tại (Số nhà, Đường, Phường/Xã, Quận/Huyện, Tỉnh/TP):", value="123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh")

st.markdown("---")

# ==============================================================================
# PHẦN 2 & 3: GIAO DIỆN NHẬP LIỆU (ĐÃ LOẠI BỎ HOÀN TOÀN KHUNG VIỀN XANH ĐẬM)
# ==============================================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 2. Nhu cầu vay vốn của bạn")
    loai_vay = st.selectbox(
        "Bạn muốn vay theo hình thức nào?", 
        ["Vay tiêu dùng tín chấp (Không cần tài sản)", "Vay mua Ô tô (Thế chấp bằng xe)", "Vay mua Bất động sản (Thế chấp bằng đất/nhà)", "Vay sản xuất kinh doanh"]
    )
    muc_dich = st.text_input("Mục đích sử dụng số tiền này cụ thể là gì?", value="Mua nhà chung cư / Chi tiêu gia đình")
    
    STV = st.number_input("Số tiền bạn muốn vay (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian bạn muốn trả góp (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất ước tính (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    
    if "Không cần tài sản" in loai_vay:
        GTTSDB = 0.0
        st.caption("ℹ️ Bạn đang chọn vay tín chấp, không cần kê khai giá trị tài sản đảm bảo.")
    else:
        GTTSDB = st.number_input("Ước tính giá trị Tài sản bạn định thế chấp (Triệu đồng):", min_value=1.0, value=200.0, step=10.0)
    
    hinh_thuc_tra = st.selectbox(
        "Bạn muốn trả nợ theo phương thức nào?", 
        ["Gốc đều, lãi giảm dần (Kỳ đầu cao nhất, giảm dần về sau)"]
    )
    nguon_chinh = st.selectbox(
        "Nguồn thu nhập chính để bạn trả nợ từ đâu?", 
        ["Lương từ công việc cố định (Có HĐLĐ)", "Thu nhập từ hộ kinh doanh / Doanh nghiệp riêng", "Thu nhập từ việc cho thuê tài sản (Nhà, xe)", "Thu nhập tự do không cố định"]
    )
    nguon_phu = st.selectbox(
        "Bạn có nguồn thu nhập dự phòng nào khác không?", 
        ["Không có", "Thu nhập bổ sung từ Vợ/Chồng", "Tiền gửi tiết kiệm / Tài sản tích lũy khác"]
    )

with col2:
    st.subheader("👤 3. Thông tin tài chính & Lịch sử tín dụng")
    STKH = st.number_input("Số tuổi hiện tại của bạn (Tuổi):", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân hiện tại:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    
    nghe_nghiep_mapping = {
        "Nhân viên văn phòng (HĐLĐ vô thời hạn)": "Nhân viên văn phòng (Có HĐLĐ)",
        "Kinh doanh tự do / Chủ doanh nghiệp": "Chủ cơ sở kinh doanh / Doanh nghiệp",
        "Công chức / Viên chức nhà nước": "Làm việc tại cơ quan Nhà nước",
        "Lao động tự do / Tạm thời": "Lao động tự do / Nghề nghiệp tạm thời"
    }
    nghe_chon = st.selectbox("Công việc hiện tại của bạn:", list(nghe_nghiep_mapping.keys()))
    nghe_nghiep = nghe_nghiep_mapping[nghe_chon]
    
    TN = st.number_input("Tổng thu nhập hàng tháng của bạn (Triệu đồng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người phụ thuộc trong gia đình (Người):", min_value=0, value=1, step=1)
    PTMC = st.number_input("Số tiền bạn đang phải trả nợ hàng tháng cho các tổ chức tín dụng khác nếu có (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    st.markdown("**📌 Lịch sử vay mượn & Trả nợ cũ của bạn:**")
    tinh_trang_no = st.selectbox(
        "Hiện tại, các khoản vay cũ của bạn (bao gồm cả thẻ tín dụng, mua trả góp) có bị trễ hạn không?",
        [
            "Chưa từng vay mượn ai",
            "Đã vay và luôn trả nợ đúng hạn",
            "Có nợ quá hạn từ 10 đến 90 ngày",
            "Có nợ quá hạn trên 90 ngày hoặc đang bị nợ xấu"
        ]
    )
    
    if tinh_trang_no in ["Chưa từng vay mượn ai", "Đã vay và luôn trả nợ đúng hạn"]:
        CIC = "Nhóm 1 - Nợ đủ tiêu chuẩn"
    elif tinh_trang_no == "Có nợ quá hạn từ 10 đến 90 ngày":
        CIC = "Nhóm 2 - Nợ cần chú ý"
    else:
        CIC = "Nhóm 3 đến 5 - Nợ xấu"

    so_lan_tra_cham = st.number_input(
        "Trong vòng 1 năm qua, bạn đã từng đóng tiền trễ (dù chỉ trễ vài ngày) bao nhiêu lần?", 
        min_value=0, value=0, step=1
    )
    
    ly_do_tra_cham = "Không có trả chậm"
    if so_lan_tra_cham > 0 or CIC != "Nhóm 1 - Nợ đủ tiêu chuẩn":
        ly_do_tra_cham = st.selectbox(
            "Nguyên nhân chính dẫn đến việc bạn thanh toán trễ hạn là gì?",
            [
                "Do sơ xuất, quên ngày thanh toán hoặc do lỗi ứng dụng/lỗi ngân hàng",
                "Do công ty chậm lương, hoặc đối tác thanh toán tiền chậm vài ngày",
                "Do công việc/kinh doanh gặp khó khăn, nguồn thu nhập bị sụt giảm mạnh",
                "Tôi không muốn trả khoản nợ đó hoặc đang có tranh chấp với bên cho vay"
            ]
        )
        ly_do_mapping = {
            "Do sơ xuất, quên ngày thanh toán hoặc do lỗi ứng dụng/lỗi ngân hàng": "Lý do khách quan",
            "Do công ty chậm lương, hoặc đối tác thanh toán tiền chậm vài ngày": "Lý do kỹ thuật",
            "Do công việc/kinh doanh gặp khó khăn, nguồn thu nhập bị sụt giảm mạnh": "Lý do chủ quan",
            "Tôi không muốn trả khoản nợ đó hoặc đang có tranh chấp với bên cho vay": "Lý do cố ý"
        }
        ly_do_chuyen_doi = ly_do_mapping[ly_do_tra_cham]
    else:
        ly_do_chuyen_doi = "Không có trả chậm"

# ==============================================================================
# PHẦN 3: TÍNH TOÁN DÒNG TIỀN DỰ KIẾN KÝ ĐẦU (REAL-TIME)
# ==============================================================================
TG_Thang = TGV * 12
if TG_Thang > 0:
    Goc_Hang_Thang = STV / TG_Thang
    Lai_Thang_Dau = STV * (LSV / 12)
    PTMM = Goc_Hang_Thang + Lai_Thang_Dau
else:
    PTMM = 0.0
    Goc_Hang_Thang = 0.0
    Lai_Thang_Dau = 0.0

st.info(f"💡 **Ước tính số tiền bạn cần trả hằng tháng (Kỳ đầu tiên):** `{PTMM:.2f}` Triệu đồng/tháng (Tiền Gốc cố định: {Goc_Hang_Thang:.2f} tr, Tiền Lãi tháng đầu: {PTMM - Goc_Hang_Thang:.2f} tr)")

st.markdown("---")

# ==============================================================================
# PHẦN 4: ĐIỀU KHOẢN PHÁP LÝ & BẢO MẬT DỮ LIỆU (TICK BOX)
# ==============================================================================
st.subheader("🔒 4. Cam kết bảo mật & Điều khoản pháp lý")
cam_ket = st.checkbox(
    "Tôi cam kết các thông tin trên là chính xác và đồng ý cho phép hệ thống tra cứu/xử lý dữ liệu để kiểm tra điều kiện vay vốn."
)

st.markdown("---")

# ==============================================================================
# PHẦN 5: LOGIC THẨM ĐỊNH VÀ PHÊ DUYỆT TỰ ĐỘNG KHI BẤM NÚT
# ==============================================================================
if st.button("📊 Gửi hồ sơ và Kiểm tra kết quả", type="primary", disabled=not cam_ket):
    
    if not ho_ten.strip():
        st.error("❌ Vui lòng nhập Họ và Tên của bạn.")
    elif len(cccd.strip()) != 12 or not cccd.strip().isdigit():
        st.error("❌ Số CCCD không hợp lệ. Vui lòng nhập đúng 12 ký tự số.")
    elif not dia_chi.strip():
        st.error("❌ Vui lòng cung cấp Địa chỉ cư trú hiện tại.")
    else:
        try:
            Tong_No_Phai_Tra = PTMM + PTMC
            CPSH_BAN_THAN = 5.0
            CPSH_PHU_THUOC = 3.5
            tong_chi_phi_sinh_hoat = CPSH_BAN_THAN + (SNPT * CPSH_PHU_THUOC)
            thu_nhap_rong = TN - tong_chi_phi_sinh_hoat
            
            DTI = Tong_No_Phai_Tra / TN if TN > 0 else 1.0
            LTV = STV / GTTSDB if GTTSDB > 0 else 0.0
            Tich_Luy_Con_Lai = thu_nhap_rong - PTMM

            tab1, tab2, tab3 = st.tabs(["📈 Kết quả xét duyệt sơ bộ", "📋 Chi tiết hồ sơ và dòng tiền", "💡 Khuyên dùng từ ngân hàng"])
            
            with tab1:
                st.markdown(f"### Xin chào Khách hàng: **{ho_ten.upper()}** (CCCD: `{cccd}`)")
                st.write("Các chỉ số an toàn tài chính cá nhân của bạn:")
                m1, m2, m3 = st.columns(3)
                m1.metric(label="Tỷ lệ nợ trên thu nhập (DTI)", value=f"{DTI * 100:.2f}%", delta="Mục tiêu: ≤ 70%")
                if "Không cần tài sản" in loai_vay:
                    m2.metric(label="Tỷ lệ khoản vay trên Tài sản (LTV)", value="Không áp dụng", delta="Vay tín chấp")
                else:
                    m2.metric(label="Tỷ lệ khoản vay trên Tài sản (LTV)", value=f"{LTV * 100:.2f}%", delta="Mục tiêu: ≤ 70%")
                m3.metric(label="Số tuổi của bạn", value=f"{STKH} tuổi", delta="Quy định: 18 - 70 tuổi")
                
                st.markdown("---")
                st.markdown("### 🏁 KẾT QUẢ ĐÁNH GIÁ TỰ ĐỘNG:")
                
                rejection_reasons = []
                
                if CIC == "Nhóm 3 đến 5 - Nợ xấu":
                    rejection_reasons.append("Bạn hiện đang có khoản nợ bị quá hạn quá lâu (trên 90 ngày). Ngân hàng không thể cấp thêm khoản vay mới khi nợ cũ chưa giải quyết.")
                if CIC == "Nhóm 2 - Nợ cần chú ý":
                    if "Lý do chủ quan" in ly_do_chuyen_doi or "Lý do cố ý" in ly_do_chuyen_doi:
                        rejection_reasons.append("Lịch sử trễ hạn cũ xuất phát từ việc kinh doanh khó khăn hoặc tranh chấp, tiềm ẩn rủi ro cho khoản vay mới.")
                    elif so_lan_tra_cham > 3:
                        rejection_reasons.append(f"Tần suất bạn nộp trễ hạn trong năm qua quá nhiều ({so_lan_tra_cham} lần), cho thấy thói quen tài chính chưa ổn định.")
                if "Lý do cố ý" in ly_do_chuyen_doi:
                    rejection_reasons.append("Hệ thống từ chối do bạn ghi nhận có tranh chấp cố ý không thanh toán nợ cũ.")
                if CIC == "Nhóm 1 - Nợ đủ tiêu chuẩn" and so_lan_tra_cham > 5:
                    rejection_reasons.append(f"Mặc dù bạn đã đóng đủ nợ cũ, nhưng việc nộp trễ quá nhiều lần ({so_lan_tra_cham} lần) khiến hệ thống đánh giá thấp mức độ uy tín dòng tiền.")

                if DTI > 0.70:
                    rejection_reasons.append(f"Tổng số tiền trả nợ mỗi tháng (cũ + mới) chiếm đến {DTI * 100:.2f}% thu nhập của bạn. Áp lực trả nợ quá lớn, vượt ngưỡng an toàn (70%).")
                if "Không cần tài sản" not in loai_vay and LTV > 0.70:
                    rejection_reasons.append(f"Giá trị tài sản bạn thế chấp không đủ bảo đảm cho số tiền muốn vay (Số tiền vay vượt quá 70% giá trị tài sản).")
                if "Không cần tài sản" in loai_vay and STV > 500:
                    rejection_reasons.append("Hạn mức tối đa cho gói vay tín chấp (không tài sản đảm bảo) của khách hàng cá nhân là 500 triệu đồng.")
                if STKH < 18 or STKH > 70:
                    rejection_reasons.append(f"Độ tuổi của bạn ({STKH} tuổi) nằm ngoài khung tuổi quy định hỗ trợ vay vốn (18 đến 70 tuổi).")
                if Tich_Luy_Con_Lai < 0:
                    rejection_reasons.append("Sau khi trừ tiền trả nợ mới và chi phí sinh hoạt tối thiểu của gia đình, thu nhập còn lại của bạn bị âm. Bạn sẽ không đủ tiền chi tiêu.")
                if "Lao động tự do" in nghe_nghiep and "Không cần tài sản" in loai_vay:
                    rejection_reasons.append("Hình thức vay tín chấp yêu cầu bắt buộc khách hàng phải có nguồn thu nhập ổn định từ lương có hợp đồng rõ ràng.")

                if len(rejection_reasons) == 0:
                    st.success("🎉 **CHÚC MỪNG! HỒ SƠ ĐỦ ĐIỀU KIỆN SƠ TUYỂN (APPROVED)**")
                    st.balloons()
                    st.write(f"Hồ sơ của khách hàng **{ho_ten}** đạt các tiêu chí an toàn cơ bản. Chuyên viên tín dụng ngân hàng tại khu vực **{dia_chi}** sẽ liên hệ với bạn trong thời gian sớm nhất.")
                else:
                    st.error("🚨 **RẤT TIẾC, HỒ SƠ CHƯA ĐỦ ĐIỀU KIỆN (REJECTED)**")
                    st.markdown("**Các lý do khiến hồ sơ chưa đạt:**")
                    for reason in rejection_reasons:
                        st.write(f"- {reason}")
                        
            with tab2:
                st.markdown("### Chi tiết thông tin đăng ký hồ sơ:")
                c_info1, c_info2 = st.columns(2)
                with c_info1:
                    st.write(f"- **Họ và tên:** {ho_ten}")
                    st.write(f"- **Số CCCD:** `{cccd}`")
                    st.write(f"- **Địa chỉ cư trú:** {dia_chi}")
                    st.write(f"- **Sản phẩm đăng ký:** {loai_vay}")
                    st.write(f"- **Mục đích vay:** {muc_dich}")
                with c_info2:
                    st.write(f"- **Tình trạng hôn nhân:** {hon_nhan}")
                    st.write(f"- **Nhóm công việc:** {nghe_chon}")
                    st.write(f"- **Lịch sử đóng nợ cũ:** {tinh_trang_no} (Trễ hạn {so_lan_tra_cham} lần)")
                    st.write(f"- **Nguyên nhân chậm đóng (nếu có):** {ly_do_tra_cham}")

                st.markdown("---")
                st.markdown("### Bản tóm tắt dòng tiền hàng tháng của bạn:")
                st.write(f"- 💵 **Tiền trả định kỳ cho khoản vay mới này (Kỳ đầu):** `{PTMM:.2f}` Triệu đồng/tháng")
                st.write(f"- 💳 **Tiền trả cho các khoản nợ cũ khác (nếu có):** `{PTMC:.2f}` Triệu đồng/tháng")
                st.write(f"- 💸 **Ước tính chi phí ăn ở, sinh hoạt tối thiểu của gia đình:** `{tong_chi_phi_sinh_hoat:.2f}` Triệu đồng/tháng")
                st.write(f"- 📈 **Số tiền thặng dư còn lại để tích lũy/dự phòng:** `{Tich_Luy_Con_Lai:.2f}` Triệu đồng/tháng")

            with tab3:
                st.markdown("### Lời khuyên tài chính dành cho bạn:")
                if DTI > 0.50 and DTI <= 0.70:
                    st.warning("⚠️ Khoản nợ này đang chiếm hơn một nửa thu nhập hằng tháng của bạn. Bạn nên cân nhắc kéo dài thời gian vay để giảm bớt tiền phải đóng mỗi tháng.")
                if "Lý do khách quan" in ly_do_chuyen_doi:
                    st.info("ℹ️ Nếu bạn từng trễ hạn chỉ vì 'quên ngày', sau khi giải ngân hãy bật tính năng 'Trích nợ tự động' trên app ngân hàng.")
                if "Lý do kỹ thuật" in ly_do_chuyen_doi:
                    st.info("ℹ️ Nếu ngày nhận lương lệch với ngày trả nợ, bạn có quyền yêu cầu chuyên viên đổi ngày đóng tiền sang ngày khớp kỳ lương.")
                if hon_nhan == "Đã kết hôn" and nguon_phu == "Không có":
                    st.warning("⚠️ Bạn nên làm hồ sơ 'Đồng vay' cùng Vợ/Chồng của mình để cộng gộp thu nhập, giúp hồ sơ dễ duyệt hơn.")
                if len(rejection_reasons) == 0 and so_lan_tra_cham == 0:
                    st.write("✅ Bạn có lịch sử tài chính tuyệt vời! Hãy tiếp tục duy trì thói quen chi tiêu đúng hạn này.")
                                    
        except ZeroDivisionError:
            st.error("❌ Có lỗi xảy ra trong quá trình tính toán. Vui lòng kiểm tra lại số liệu tài sản hoặc thời gian vay.")

if not cam_ket:
    st.info("⚠️ Bạn cần tích chọn ô 'Cam kết và đồng ý điều khoản bảo mật' ở mục 4 để kích hoạt nút gửi hồ sơ.")

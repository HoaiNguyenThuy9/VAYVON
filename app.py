Chào bạn, tôi đã hiểu ý bạn rồi! Bạn muốn giao diện không chỉ có màu nền (gradient) mà phải có các hình ảnh minh họa trực quan cho từng sản phẩm vay (như hình ảnh gia đình, kỹ sư, ô tô, kinh doanh) và các nút bấm, thẻ sản phẩm (Cards) được thiết kế bo góc, đổ bóng chuẩn UI/UX ngân hàng hiện đại giống như trang web của Vietcombank.

Để làm được điều này trong Streamlit mà vẫn giữ nguyên logic tính toán của bạn, chúng ta sẽ kết hợp giữa việc nhúng mã HTML/CSS và sử dụng các link hình ảnh trực tuyến (hoặc bạn có thể tự thay bằng link ảnh của bạn sau).

Dưới đây là mã nguồn Streamlit đã được làm lại hoàn toàn theo phong cách giao diện như ảnh bạn gửi:

Python
import streamlit as st

# ==============================================================================
# CẤU HÌNH TRANG WEB & CSS NÂNG CAO (PHONG CÁCH VIETCOMBANK)
# ==============================================================================
st.set_page_config(page_title="APP CHO VAY ONLINE KHCN - THUY HOAI", layout="wide")

# CSS để tùy biến giao diện giống giao diện ngân hàng hiện đại
st.markdown("""
    <style>
    /* Tổng thể nền trang web */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Thiết kế Banner chính */
    .hero-banner {
        background: linear-gradient(to right, #ffffff 40%, rgba(255,255,255,0) 100%), 
                    url('https://images.unsplash.com/photo-1556742044-3c52d6e88c62?auto=format&fit=crop&q=80&w=1200');
        background-size: cover;
        background-position: right center;
        padding: 50px;
        border-radius: 20px;
        margin-bottom: 30px;
        border: 1px solid #e9ecef;
    }
    
    /* Thiết kế thẻ Card cho từng mục */
    .product-card {
        background: #ffffff;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        border: 1px solid #edf2f7;
        overflow: hidden;
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    /* Ảnh header của từng Card */
    .card-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
    }
    
    /* Nội dung bên trong Card */
    .card-content {
        padding: 20px;
    }
    
    /* Tiêu đề phân đoạn */
    .card-title {
        color: #1b4d3e; /* Màu xanh lá đặc trưng ngân hàng */
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    /* Nút bấm Đăng ký chính */
    div.stButton > button:first-child {
        background-color: #7cb342; /* Màu xanh lá thương hiệu */
        color: white;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
        border-radius: 8px;
        width: 100%;
        transition: all 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #689f38;
        border: none;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
URL_LOGO = "tài chính.png" 
try:
    st.sidebar.image(URL_LOGO, use_container_width=True)
except:
    st.sidebar.warning("⚠️ Vui lòng kiểm tra file tài chính.png")

st.sidebar.markdown("---")
st.sidebar.info("🏢 **Hệ thống trực tuyến**\n\nCổng Đăng Ký Khoản Vay Tự Động\n\n**NHÓM 6**")

# ==============================================================================
# HERO BANNER CHÍNH (Giống phần trên cùng của Vietcombank)
# ==============================================================================
st.markdown("""
    <div class="hero-banner">
        <h1 style="color: #1b4d3e; font-size: 2.3rem; font-weight: 800; margin-bottom: 10px;">Vay trực tuyến</h1>
        <p style="color: #4a5568; font-size: 1.1rem; max-width: 500px; margin-bottom: 20px;">
            Lãi suất cạnh tranh, thời hạn linh hoạt. Hệ thống thẩm định và trả kết quả tự động siêu tốc.
        </p>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# PHẦN 1: THÔNG TIN ĐỊNH DANH (Thiết kế tinh gọn)
# ==============================================================================
st.markdown('<div class="product-card" style="padding: 20px;">', unsafe_allow_html=True)
st.markdown('<div class="card-title">🪪 1. Thông tin định danh cá nhân</div>', unsafe_allow_html=True)
col_id1, col_id2, col_id3 = st.columns([1.5, 1.5, 2])
with col_id1:
    ho_ten = st.text_input("Họ và chữ lót, Tên của bạn:", value="Nguyễn Văn A")
with col_id2:
    cccd = st.text_input("Số Căn cước công dân (12 số):", value="012345678901")
with col_id3:
    dia_chi = st.text_input("Địa chỉ cư trú hiện tại:", value="123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h2 style="color: #1b4d3e; font-size: 1.6rem; margin-top: 30px; margin-bottom: 20px;">Danh sách sản phẩm dịch vụ</h2>', unsafe_allow_html=True)

# ==============================================================================
# PHẦN 2 & 3: THIẾT KẾ CARD CÓ HÌNH ẢNH MINH HỌA (Chia thành 2 cột lớn)
# ==============================================================================
col_main1, col_main2 = st.columns(2)

with col_main1:
    # Bắt đầu Card Phần 2 (Nhu cầu vay với hình ảnh công trường/nhà cửa)
    st.markdown("""
        <div class="product-card">
            <img class="card-img" src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&q=80&w=600" alt="Nhu cầu vay">
            <div class="card-content">
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="card-title">📋 2. Nhu cầu vay vốn của bạn</div>', unsafe_allow_html=True)
    
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
        st.caption("ℹ️ Bạn đang chọn vay tín chấp, không cần kê khai tài sản đảm bảo.")
    else:
        GTTSDB = st.number_input("Ước tính giá trị Tài sản định thế chấp (Triệu đồng):", min_value=1.0, value=200.0, step=10.0)
    
    hinh_thuc_tra = st.selectbox(
        "Bạn muốn trả nợ theo phương thức nào?", 
        ["Gốc đều, lãi giảm dần (Kỳ đầu cao nhất)", "Gốc và lãi chia đều cố định hàng tháng (Annuity)"]
    )
    nguon_chinh = st.selectbox(
        "Nguồn thu nhập chính từ đâu?", 
        ["Lương từ công việc cố định (Có HĐLĐ)", "Thu nhập từ hộ kinh doanh / Doanh nghiệp riêng", "Thu nhập từ việc cho thuê tài sản", "Thu nhập tự do không cố định"]
    )
    nguon_phu = st.selectbox(
        "Nguồn thu nhập dự phòng khác?", 
        ["Không có", "Thu nhập bổ sung từ Vợ/Chồng", "Tiền gửi tiết kiệm / Tài sản tích lũy khác"]
    )
    
    st.markdown('</div></div>', unsafe_allow_html=True) # Đóng Card 2

with col_main2:
    # Bắt đầu Card Phần 3 (Thông tin tài chính với hình ảnh doanh nhân/văn phòng)
    st.markdown("""
        <div class="product-card">
            <img class="card-img" src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=600" alt="Tài chính khách hàng">
            <div class="card-content">
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="card-title">👤 3. Thông tin tài chính & Lịch sử tín dụng</div>', unsafe_allow_html=True)
    
    STKH = st.number_input("Số tuổi hiện tại của bạn (Tuổi):", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    
    nghe_nghiep_mapping = {
        "Nhân viên văn phòng (HĐLĐ vô thời hạn)": "Nhân viên văn phòng (Có HĐLĐ)",
        "Kinh doanh tự do / Chủ doanh nghiệp": "Chủ cơ sở kinh doanh / Doanh nghiệp",
        "Công chức / Viên chức nhà nước": "Làm việc tại cơ quan Nhà nước",
        "Lao động tự do / Tạm thời": "Lao động tự do / Nghề nghiệp tạm thời"
    }
    nghe_chon = st.selectbox("Công việc hiện tại:", list(nghe_nghiep_mapping.keys()))
    nghe_nghiep = nghe_nghiep_mapping[nghe_chon]
    
    TN = st.number_input("Tổng thu nhập hàng tháng (Triệu đồng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người phụ thuộc (Người):", min_value=0, value=1, step=1)
    PTMC = st.number_input("Số tiền đang trả nợ định kỳ ở nơi khác (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    st.markdown("<b style='color:#2d3748;'>📌 Lịch sử vay mượn & Trả nợ cũ:</b>", unsafe_allow_html=True)
    tinh_trang_no = st.selectbox(
        "Các khoản nợ cũ hiện tại có bị trễ hạn không?",
        [
            "Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai",
            "Tôi đang có khoản nợ bị quá hạn dưới 90 ngày chưa kịp thanh toán",
            "Tôi đang có nợ quá hạn quá lâu (trên 90 ngày) hoặc đang bị nợ xấu"
        ]
    )
    
    if tinh_trang_no == "Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai":
        CIC = "Nhóm 1 - Nợ đủ tiêu chuẩn"
    elif tinh_trang_no == "Tôi đang có khoản nợ bị quá hạn dưới 90 ngày chưa kịp thanh toán":
        CIC = "Nhóm 2 - Nợ cần chú ý"
    else:
        CIC = "Nhóm 3 đến 5 - Nợ xấu"

    so_lan_tra_cham = st.number_input("Trong 1 năm qua, số lần đóng trễ hạn?", min_value=0, value=0, step=1)
    
    if so_lan_tra_cham > 0 or CIC != "Nhóm 1 - Nợ đủ tiêu chuẩn":
        ly_do_tra_cham = st.selectbox(
            "Nguyên nhân chính dẫn đến trễ hạn là gì?",
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
        ly_do_tra_cham = "Không có trả chậm"
        ly_do_chuyen_doi = "Không có trả chậm"
        
    st.markdown('</div></div>', unsafe_allow_html=True) # Đóng Card 3

# ==============================================================================
# TÍNH TOÁN DÒNG TIỀN DỰ KIẾN KỲ ĐẦU
# ==============================================================================
TG_Thang = TGV * 12
if TG_Thang > 0:
    Goc_Hang_Thang = STV / TG_Thang
    if "Kỳ đầu cao nhất" in hinh_thuc_tra:
        Lai_Thang_Dau = STV * (LSV / 12)
        PTMM = Goc_Hang_Thang + Lai_Thang_Dau
    else:  
        r_monthly = LSV / 12
        if r_monthly > 0:
            PTMM = STV * (r_monthly * (1 + r_monthly)**TG_Thang) / ((1 + r_monthly)**TG_Thang - 1)
        else:
            PTMM = STV / TG_Thang
else:
    PTMM, Goc_Hang_Thang, Lai_Thang_Dau = 0.0, 0.0, 0.0

st.info(f"💡 **Ước tính số tiền bạn cần trả hằng tháng (Kỳ đầu tiên):** `{PTMM:.2f}` Triệu đồng/tháng (Tiền Gốc: {Goc_Hang_Thang:.2f} tr, Tiền Lãi tháng đầu: {PTMM - Goc_Hang_Thang:.2f} tr)")

# ==============================================================================
# PHẦN 4: NÚT ĐĂNG KÝ VÀ PHÊ DUYỆT TỰ ĐỘNG
# ==============================================================================
if st.button("Đăng ký ngay (Kiểm tra kết quả)", type="primary"):
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

            # Khối kết quả bọc trong card trắng tinh tế
            st.markdown('<div class="product-card" style="padding: 25px;">', unsafe_allow_html=True)
            
            tab1, tab2, tab3 = st.tabs(["📈 Kết quả xét duyệt sơ bộ", "📋 Chi tiết hồ sơ và dòng tiền", "💡 Khuyên dùng từ ngân hàng"])
            
            with tab1:
                st.write(f"### Khách hàng: **{ho_ten.upper()}** (CCCD: `{cccd}`)")
                m1, m2, m3 = st.columns(3)
                m1.metric(label="Tỷ lệ nợ trên thu nhập (DTI)", value=f"{DTI * 100:.2f}%", delta="Mục tiêu: ≤ 70%")
                if "Không cần tài sản" in loai_vay:
                    m2.metric(label="Tỷ lệ khoản vay trên Tài sản (LTV)", value="Không áp dụng", delta="Vay tín chấp")
                else:
                    m2.metric(label="Tỷ lệ khoản vay trên Tài sản (LTV)", value=f"{LTV * 100:.2f}%", delta="Mục tiêu: ≤ 70%")
                m3.metric(label="Số tuổi của bạn", value=f"{STKH} tuổi", delta="Quy định: 18 - 70 tuổi")
                
                st.markdown("---")
                
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
                    rejection_reasons.append(f"Tổng số tiền trả nợ mỗi tháng chiếm đến {DTI * 100:.2f}% thu nhập của bạn. Vượt ngưỡng an toàn (70%).")
                if "Không cần tài sản" not in loai_vay and LTV > 0.70:
                    rejection_reasons.append(f"Giá trị tài sản bạn thế chấp không đủ bảo đảm cho số tiền muốn vay (Vượt quá 70% giá trị tài sản).")
                if "Không cần tài sản" in loai_vay and STV > 500:
                    rejection_reasons.append("Hạn mức tối đa cho gói vay tín chấp cá nhân là 500 triệu đồng.")
                if STKH < 18 or STKH > 70:
                    rejection_reasons.append(f"Độ tuổi của bạn ({STKH} tuổi) nằm ngoài khung tuổi quy định (18 đến 70 tuổi).")
                if Tich_Luy_Con_Lai < 0:
                    rejection_reasons.append("Sau khi trừ tiền trả nợ mới và chi phí sinh hoạt tối thiểu, thu nhập còn lại bị âm.")
                if "Lao động tự do" in nghe_nghiep and "Không cần tài sản" in loai_vay:
                    rejection_reasons.append("Hình thức vay tín chấp yêu cầu bắt buộc khách hàng phải có nguồn thu nhập ổn định từ lương có hợp đồng rõ ràng.")

                if len(rejection_reasons) == 0:
                    st.success("🎉 **CHÚC MỪNG! HỒ SƠ ĐỦ ĐIỀU KIỆN SƠ TUYỂN (APPROVED)**")
                    st.balloons()
                else:
                    st.error("🚨 **RẤT TIẾC, HỒ SƠ CHƯA ĐỦ ĐIỀU KIỆN (REJECTED)**")
                    for reason in rejection_reasons:
                        st.write(f"- {reason}")
                        
            with tab2:
                st.write("### Chi tiết thông tin đăng ký và Dòng tiền:")
                st.write(f"- **Họ và tên:** {ho_ten} | **CCCD:** `{cccd}`")
                st.write(f"- **Sản phẩm:** {loai_vay} | **Mục đích:** {muc_dich}")
                st.write(f"- 💵 **Tiền trả định kỳ cho khoản vay mới:** `{PTMM:.2f}` tr/tháng")
                st.write(f"- 💸 **Ước tính chi phí sinh hoạt gia đình:** `{tong_chi_phi_sinh_hoat:.2f}` tr/tháng")
                st.write(f"- 📈 **Số tiền thặng dư tích lũy còn lại:** `{Tich_Luy_Con_Lai:.2f}` tr/tháng")

            with tab3:
                st.write("### Lời khuyên tài chính dành cho bạn:")
                if DTI > 0.50 and DTI <= 0.70:
                    st.warning("⚠️ Khoản nợ này đang chiếm hơn một nửa thu nhập hằng tháng của bạn. Bạn nên cân nhắc kéo dài thời gian vay.")
                if hon_nhan == "Đã kết hôn" and nguon_phu == "Không có":
                    st.warning("⚠️ Bạn nên làm hồ sơ 'Đồng vay' cùng Vợ/Chồng để dễ duyệt hơn.")
                if len(rejection_reasons) == 0 and so_lan_tra_cham == 0:
                    st.write("✅ Bạn có lịch sử tài chính tuyệt vời!")
            
            st.markdown('</div>', unsafe_allow_html=True)
                                    
        except ZeroDivisionError:
            st.error("❌ Có lỗi xảy ra trong quá trình tính toán.")

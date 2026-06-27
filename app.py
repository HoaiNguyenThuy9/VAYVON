Để tạo ra một giao diện đột phá, mang tính công nghệ và tiệm cận nhất với các ứng dụng Mobile Banking/Web Banking cao cấp hiện nay (như giao diện của các ngân hàng số thế hệ mới), tôi đã thiết kế lại ứng dụng theo phong cách Glassmorphism (Hiệu ứng kính mờ) kết hợp với hệ thống Tabs động để gom gọn lộ trình điền hồ sơ của khách hàng thay vì trải dài trang web.

Cách tiếp cận này giúp ứng dụng cực kỳ gọn gàng, mang tính tương tác cao và chuyên nghiệp như một hệ thống Core-Banking thực thụ.

#🌟 Mã nguồn Streamlit Giao diện Ngân hàng Số Thế hệ mới
Python
import streamlit as st

# ==============================================================================
# 1. CẤU HÌNH HỆ THỐNG & CORE CSS (HIỆU ỨNG KÍNH MỜ & CARD LỚN)
# ==============================================================================
st.set_page_config(page_title="HỆ THỐNG THẨM ĐỊNH TỰ ĐỘNG - THUY HOAI", layout="wide")

# Toàn bộ CSS giao diện nâng cao
st.markdown("""
    <style>
    /* Nền toàn trang chuyển màu Gradient tạo chiều sâu */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff;
    }
    
    /* Biến các text mặc định của Streamlit sang màu sáng để dễ đọc trên nền tối */
    .stApp p, .stApp label, .stApp span {
        color: #e2e8f0 !important;
    }
    
    /* Siêu Banner Kính mờ (Glassmorphism Banner) */
    .premium-banner {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 40px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    /* Thiết kế Form Card cao cấp */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    /* Tiêu đề phân đoạn mang tính nhận diện cao */
    .step-header {
        font-size: 1.4rem;
        font-weight: 700;
        color: #00ffcc;
        border-bottom: 2px solid rgba(0, 255, 204, 0.2);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    /* Nút bấm kiểm tra thiết kế phát sáng (Glow Button) */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
        color: #ffffff !important;
        border: none;
        padding: 14px 30px;
        font-size: 1.2rem;
        font-weight: 700;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.4);
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.7);
        border: none;
    }
    
    /* Tùy chỉnh thanh Tabs của Streamlit để khớp với giao diện tối */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        padding: 10px 20px;
        color: white !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(255, 255, 255, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar đồng bộ tông màu tối
st.sidebar.markdown("<h2 style='color:#00ffcc; text-align:center;'>VIBE BANK</h2>", unsafe_allow_html=True)
URL_LOGO = "tài chính.png" 
try:
    st.sidebar.image(URL_LOGO, use_container_width=True)
except:
    pass
st.sidebar.markdown("---")
st.sidebar.info("🤖 **Hệ thống AI Thẩm định**\nTự động phân tích dòng tiền và chấm điểm tín dụng CIC chỉ trong vài giây.")

# ==============================================================================
# 2. ĐỈNH TRANG: PREMIUM HERO BANNER
# ==============================================================================
st.markdown("""
    <div class="premium-banner">
        <h1 style="color: #ffffff; font-size: 2.5rem; font-weight: 800; letter-spacing: 1px;">
            HỆ THỐNG ĐĂNG KÝ VÀ DUYỆT VAY KHÁCH HÀNG CÁ NHÂN
        </h1>
        <p style="color: #00ffcc; font-size: 1.1rem; font-weight: 500;">
            ⚡ Trải nghiệm phê duyệt số hóa 100% dựa trên thuật toán quản trị rủi ro tự động
        </p>
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. QUY TRÌNH NHẬP LIỆU GOM GỌN THEO CÁC BƯỚC (STEP-BY-STEP TABS)
# ==============================================================================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

step_tab1, step_tab2, step_tab3 = st.tabs([
    "📂 Bước 1: Định danh khách hàng", 
    "📈 Bước 2: Nhu cầu vay vốn", 
    "🛡️ Bước 3: Năng lực tài chính & CIC"
])

with step_tab1:
    st.markdown('<div class="step-header">🪪 1. Xác thực thông tin cá nhân</div>', unsafe_allow_html=True)
    col_id1, col_id2 = st.columns(2)
    with col_id1:
        ho_ten = st.text_input("Họ và Tên chủ hồ sơ:", value="Nguyễn Văn A")
        cccd = st.text_input("Số Căn cước công dân (CCCD):", value="012345678901")
    with col_id2:
        dia_chi = st.text_input("Địa chỉ thường trú / Tạm trú:", value="123 Đường Lê Lợi, Quận 1, TP. Hồ Chí Minh")
        STKH = st.number_input("Số tuổi hiện tại (Tuổi):", min_value=0, max_value=120, value=30, step=1)

with step_tab2:
    st.markdown('<div class="step-header">📋 2. Thiết lập cấu trúc khoản vay</div>', unsafe_allow_html=True)
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        loai_vay = st.selectbox(
            "Phương thức cấp tín dụng:", 
            ["Vay tiêu dùng tín chấp (Không cần tài sản)", "Vay mua Ô tô (Thế chấp bằng xe)", "Vay mua Bất động sản (Thế chấp bằng đất/nhà)", "Vay sản xuất kinh doanh"]
        )
        muc_dich = st.text_input("Mục đích sử dụng vốn chi tiết:", value="Mua nhà chung cư / Chi tiêu gia đình")
        STV = st.number_input("Hạn mức đề xuất vay (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    with col_v2:
        TGV = st.number_input("Thời hạn phân kỳ trả nợ (Số năm):", min_value=0.5, value=5.0, step=0.5)
        LSV = st.number_input("Lãi suất biên chế định kỳ (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
        
        if "Không cần tài sản" in loai_vay:
            GTTSDB = 0.0
            st.caption("ℹ️ Hệ thống ghi nhận: Gói vay không yêu cầu tài sản bảo đảm.")
        else:
            GTTSDB = st.number_input("Giá trị thẩm định Tài sản thế chấp (Triệu đồng):", min_value=1.0, value=200.0, step=10.0)

with step_tab3:
    st.markdown('<div class="step-header">👤 3. Khai báo nguồn thu và Lịch sử CIC</div>', unsafe_allow_html=True)
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        hon_nhan = st.selectbox("Tình trạng hôn nhân:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
        nghe_nghiep_mapping = {
            "Nhân viên văn phòng (HĐLĐ vô thời hạn)": "Nhân viên văn phòng (Có HĐLĐ)",
            "Kinh doanh tự do / Chủ doanh nghiệp": "Chủ cơ sở kinh doanh / Doanh nghiệp",
            "Công chức / Viên chức nhà nước": "Làm việc tại cơ quan Nhà nước",
            "Lao động tự do / Tạm thời": "Lao động tự do / Nghề nghiệp tạm thời"
        }
        nghe_chon = st.selectbox("Phân nhóm nghề nghiệp nghề nghiệp:", list(nghe_nghiep_mapping.keys()))
        nghe_nghiep = nghe_nghiep_mapping[nghe_chon]
        TN = st.number_input("Thu nhập chứng minh hàng tháng (Triệu đồng):", min_value=0.0, value=30.0, step=5.0)
        SNPT = st.number_input("Số người phụ thuộc đang nuôi dưỡng:", min_value=0, value=1, step=1)
    
    with col_t2:
        PTMC = st.number_input("Nghĩa vụ trả nợ tổ chức tín dụng khác (Triệu đồng/tháng):", min_value=0.0, value=0.0, step=1.0)
        hinh_thuc_tra = st.selectbox("Phương thức thanh toán nợ kỳ gốc:", ["Gốc đều, lãi giảm dần (Kỳ đầu cao nhất)", "Gốc và lãi chia đều cố định hàng tháng (Annuity)"])
        tinh_trang_no = st.selectbox(
            "Phân loại nhóm nợ thực tế:",
            ["Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai", "Tôi đang có khoản nợ bị quá hạn dưới 90 ngày", "Tôi đang có nợ quá hạn quá lâu (trên 90 ngày) hoặc đang bị nợ xấu"]
        )
        so_lan_tra_cham = st.number_input("Tần suất chậm thanh toán trong 12 tháng qua (Lần):", min_value=0, value=0, step=1)

    # Khớp dữ liệu lý do tự động ẩn sau logic
    if tinh_trang_no == "Tôi luôn trả nợ đúng hạn / Chưa từng vay mượn ai":
        CIC = "Nhóm 1 - Nợ đủ tiêu chuẩn"
        ly_do_chuyen_doi = "Không có trả chậm"
    else:
        CIC = "Nhóm 2 - Nợ cần chú ý" if "dưới 90 ngày" in tinh_trang_no else "Nhóm 3 đến 5 - Nợ xấu"
        ly_do_chuyen_doi = "Lý do khách quan"

st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 4. TÍNH TOÁN DÒNG TIỀN DỰ KIẾN REAL-TIME
# ==============================================================================
TG_Thang = TGV * 12
if TG_Thang > 0:
    Goc_Hang_Thang = STV / TG_Thang
    if "Kỳ đầu cao nhất" in hinh_thuc_tra:
        Lai_Thang_Dau = STV * (LSV / 12)
        PTMM = Goc_Hang_Thang + Lai_Thang_Dau
    else:  
        r_monthly = LSV / 12
        PTMM = STV * (r_monthly * (1 + r_monthly)**TG_Thang) / ((1 + r_monthly)**TG_Thang - 1) if r_monthly > 0 else STV / TG_Thang
else:
    PTMM, Goc_Hang_Thang, Lai_Thang_Dau = 0.0, 0.0, 0.0

st.markdown(f"""
    <div style="background: rgba(0, 255, 204, 0.1); border-left: 4px solid #00ffcc; padding: 15px; border-radius: 8px; margin-bottom: 25px;">
        📊 <b>Ước tính dòng tiền thanh toán kỳ đầu:</b> <span style="color:#00ffcc; font-size:1.2rem; font-weight:700;">{PTMM:.2f}</span> Triệu đồng/tháng 
        (Gốc cố định: {Goc_Hang_Thang:.2f} tr | Lãi tháng đầu: {PTMM - Goc_Hang_Thang:.2f} tr)
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 5. NÚT KÍCH HOẠT HỆ THỐNG THẨM ĐỊNH AI
# ==============================================================================
if st.button("🚀 KHỞI CHẠY THẨM ĐỊNH HỒ SƠ TỰ ĐỘNG", type="primary"):
    if not ho_ten.strip() or len(cccd.strip()) != 12 or not cccd.strip().isdigit():
        st.error("❌ Dữ liệu Định danh không hợp lệ. Vui lòng kiểm tra lại Bước 1.")
    else:
        # Thực hiện nghiệp vụ logic rủi ro ngân hàng
        Tong_No_Phai_Tra = PTMM + PTMC
        tong_chi_phi_sinh_hoat = 5.0 + (SNPT * 3.5)
        thu_nhap_rong = TN - tong_chi_phi_sinh_hoat
        DTI = Tong_No_Phai_Tra / TN if TN > 0 else 1.0
        LTV = STV / GTTSDB if GTTSDB > 0 else 0.0
        Tich_Luy_Con_Lai = thu_nhap_rong - PTMM

        # Hiển thị Card kết quả Glassmorphism
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="step-header">📊 BÁO CÁO PHÂN TÍCH VÀ ĐÁNH GIÁ SƠ BỘ</div>', unsafe_allow_html=True)
        
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Chỉ số DTI (Nợ / Thu nhập)", value=f"{DTI * 100:.2f}%", delta="Ngưỡng an toàn: ≤ 70%")
        m2.metric(label="Chỉ số LTV (Vay / Tài sản)", value=f"{LTV * 100:.2f}%" if LTV > 0 else "Không áp dụng", delta="Hạn mức: ≤ 70%")
        m3.metric(label="Thặng dư tích lũy hàng tháng", value=f"{Tich_Luy_Con_Lai:.2f} Tr", delta="Yêu cầu: > 0")
        
        # Kiểm tra điều kiện chính sách chặn cứng của ngân hàng
        rejection_reasons = []
        if CIC == "Nhóm 3 đến 5 - Nợ xấu": rejection_reasons.append("Hồ sơ bị chặn do lịch sử ghi nhận có nợ xấu trên hệ thống thông tin tín dụng quốc gia (CIC).")
        if DTI > 0.70: rejection_reasons.append("Tỷ lệ nợ trên thu nhập vượt mức kiểm soát rủi ro (DTI > 70%).")
        if STKH < 18 or STKH > 70: rejection_reasons.append("Độ tuổi của khách hàng nằm ngoài khung quy định cấp tín dụng.")
        if Tich_Luy_Con_Lai < 0: rejection_reasons.append("Khả năng thặng dư dòng tiền âm, nguy cơ mất khả năng chi trả thực tế cao.")
        
        st.markdown("---")
        if len(rejection_reasons) == 0:
            st.success("🎉 **PHÊ DUYỆT SƠ BỘ (APPROVED)** - Hồ sơ đáp ứng trọn vẹn các tiêu chí rủi ro an toàn.")
            st.balloons()
        else:
            st.error("🚨 **TỪ CHỐI HỒ SƠ TỰ ĐỘNG (REJECTED)**")
            for r in rejection_reasons:
                st.markdown(f"- <span style='color:#ffa8a8;'>{r}</span>", unsafe_allow_html=True)
                
        st.markdown('</div>', unsafe_allow_html=True)

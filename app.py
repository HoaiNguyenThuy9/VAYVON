import streamlit as st

# ==============================================================================
# CẤU HÌNH TRANG WEB & LOGO
# ==============================================================================
st.set_page_config(page_title="APP CHO VAY ONLINE KHCN - THUY HOAI", layout="wide")

# Đường link Logo (Có thể thay thế bằng link logo Trường hoặc Ngân hàng của bạn)
URL_LOGO = "https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" 

# Hiển thị Logo và thông tin tại thanh Sidebar bên trái
st.sidebar.image(URL_LOGO, use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.write("### 🏢 Đơn vị thẩm định")
st.sidebar.info("Phòng Tín Dụng Khách Hàng Cá Nhân\n\nThực hiện bởi: THUY HOAI")
st.sidebar.markdown("---")
st.sidebar.caption("Ứng dụng phục vụ Đề tài 6: Thẩm định cho vay đối với khách hàng cá nhân.")

# ==============================================================================
# TIÊU ĐỀ CHÍNH CỦA ỨNG DỤNG
# ==============================================================================
st.title("🏦 APP THẨM ĐỊNH CHO VAY ONLINE KHCN - THUY HOAI - ĐỀ TÀI 6")
st.write("Hệ thống tự động thẩm định, phân tích rủi ro và phê duyệt tín dụng Khách hàng cá nhân.")

st.markdown("---")

# ==============================================================================
# PHẦN 1: GIAO DIỆN NHẬP LIỆU (CHIA THÀNH 2 CỘT)
# ==============================================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 1. Thông tin khoản vay đề xuất")
    loai_vay = st.selectbox(
        "Loại khoản vay:", 
        ["Vay tiêu dùng tín chấp", "Vay mua Ô tô (Thế chấp)", "Vay mua Bất động sản (Thế chấp)", "Vay sản xuất kinh doanh"]
    )
    muc_dich = st.text_input("Mục đích vay cụ thể:", value="Mua nhà chung cư / Tiêu dùng gia đình")
    
    STV = st.number_input("Số tiền muốn vay (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian vay (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất cho vay (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    GTTSDB = st.number_input("Giá trị tài sản đảm bảo (Triệu đồng):", min_value=0.0, value=200.0, step=10.0)
    
    hinh_thuc_tra = st.selectbox(
        "Hình thức trả nợ:", 
        ["Gốc đều, lãi giảm dần (Kỳ đầu cao nhất)", "Gốc và lãi trả đều hàng tháng (Annuity)"]
    )
    nguon_chinh = st.selectbox(
        "Nguồn trả nợ chính:", 
        ["Lương từ công việc cố định", "Thu nhập từ sản xuất kinh doanh", "Thu nhập từ cho thuê tài sản"]
    )
    nguon_phu = st.selectbox(
        "Nguồn trả nợ phụ (Dự phòng):", 
        ["Không có", "Thu nhập của người đồng vay (Vợ/Chồng)", "Tài sản tích lũy khác"]
    )

with col2:
    st.subheader("👤 2. Thông tin khách hàng & Uy tín (CIC)")
    STKH = st.number_input("Số tuổi của khách hàng (Tuổi):", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    nghe_nghiep = st.selectbox(
        "Nghề nghiệp/Lĩnh vực làm việc:", 
        ["Nhân viên văn phòng (HĐLĐ vô thời hạn)", "Kinh doanh tự do / Chủ doanh nghiệp", "Công chức / Viên chức nhà nước", "Lao động tự do / Tạm thời"]
    )
    
    TN = st.number_input("Thu nhập hàng tháng (Triệu đồng/tháng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người phụ thuộc (Người):", min_value=0, value=1, step=1)
    PTMC = st.number_input("Gốc lãi khoản vay cũ phải trả hàng tháng (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    # Quản lý rủi ro tín dụng qua hệ thống CIC
    CIC = st.selectbox(
        "Xếp hạng nhóm nợ (Hệ thống CIC):",
        ["Nhóm 1 - Nợ đủ tiêu chuẩn", "Nhóm 2 - Nợ cần chú ý", "Nhóm 3 đến 5 - Nợ xấu"]
    )
    so_lan_tra_cham = st.number_input("Số lần trả chậm trong 12 tháng qua (Tờ khai CIC):", min_value=0, value=0, step=1)
    
    # Logic ẩn/hiện: Lý do trả chậm chỉ xuất hiện khi có số lần trả chậm hoặc nhóm nợ xấu
    ly_do_tra_cham = "Không có trả chậm"
    if so_lan_tra_cham > 0 or CIC != "Nhóm 1 - Nợ đủ tiêu chuẩn":
        ly_do_tra_cham = st.selectbox(
            "Lý do trả chậm chính (Đánh giá từ tờ trình/phỏng vấn):",
            [
                "Lý do khách quan (Quên ngày thanh toán / Đi công tác / Lỗi hệ thống ngân hàng)",
                "Lý do kỹ thuật (Trễ lương từ công ty, dòng tiền về chậm 1-3 ngày)",
                "Lý do chủ quan (Kinh doanh thua lỗ / Suy giảm thu nhập nghiêm trọng)",
                "Lý do cố ý (Trốn tránh nghĩa vụ trả nợ / Phát sinh tranh chấp khoản vay cũ)"
            ]
        )

# ==============================================================================
# PHẦN 2: TÍNH TOÁN DÒNG TIỀN DỰ KIẾN KỲ ĐẦU (REAL-TIME)
# ==============================================================================
TG_Thang = TGV * 12
if TG_Thang > 0:
    Goc_Hang_Thang = STV / TG_Thang
    if hinh_thuc_tra == "Gốc đều, lãi giảm dần (Kỳ đầu cao nhất)":
        Lai_Thang_Dau = STV * (LSV / 12)
        PTMM = Goc_Hang_Thang + Lai_Thang_Dau
    else:  # Phương pháp tính đều hàng tháng (Annuity)
        r_monthly = LSV / 12
        if r_monthly > 0:
            PTMM = STV * (r_monthly * (1 + r_monthly)**TG_Thang) / ((1 + r_monthly)**TG_Thang - 1)
        else:
            PTMM = STV / TG_Thang
else:
    PTMM = 0.0
    Goc_Hang_Thang = 0.0
    Lai_Thang_Dau = 0.0

st.info(f"💡 **Khoản trả hàng tháng dự kiến (Kỳ đầu tiên/Ước tính):** `{PTMM:.2f}` Triệu đồng/tháng (Trong đó Gốc: {Goc_Hang_Thang:.2f} tr, Lãi: {PTMM - Goc_Hang_Thang:.2f} tr)")

st.markdown("---")

# ==============================================================================
# PHẦN 3: LOGIC THẨM ĐỊNH VÀ PHÊ DUYỆT TỰ ĐỘNG KHI BẤM NÚT
# ==============================================================================
if st.button("📊 Kiểm tra kết quả thẩm định", type="primary"):
    try:
        # Tổng nghĩa vụ tài chính phải trả hàng tháng
        Tong_No_Phai_Tra = PTMM + PTMC
        
        # Định mức chi phí sinh hoạt (Triệu đồng) quy đổi thực tế ngân hàng
        CPSH_BAN_THAN = 5.0
        CPSH_PHU_THUOC = 3.5
        tong_chi_phi_sinh_hoat = CPSH_BAN_THAN + (SNPT * CPSH_PHU_THUOC)
        thu_nhap_rong = TN - tong_chi_phi_sinh_hoat
        
        # Cách tính toán chỉ số theo chuẩn tài chính quốc tế
        DTI = Tong_No_Phai_Tra / TN if TN > 0 else 1.0
        LTV = STV / GTTSDB if GTTSDB > 0 else 1.0
        Tich_Luy_Con_Lai = thu_nhap_rong - PTMM

        # Giao diện Tabs phân tách thông tin chuyên nghiệp
        tab1, tab2, tab3 = st.tabs(["📈 Kết quả phân tích chỉ số", "📋 Hồ sơ & Nghĩa vụ dòng tiền", "⚠️ Khuyến nghị rủi ro"])
        
        with tab1:
            st.write("### Các chỉ số tài chính cốt lõi:")
            m1, m2, m3 = st.columns(3)
            m1.metric(label="Chỉ số DTI (Tổng nợ / Thu nhập)", value=f"{DTI * 100:.2f}%", delta="≤ 70% Tiêu chuẩn")
            m2.metric(label="Chỉ số LTV (Khoản vay / TSĐB)", value=f"{LTV * 100:.2f}%", delta="≤ 70% Tiêu chuẩn")
            m3.metric(label="Tuổi khách hàng", value=f"{STKH} tuổi", delta="18 - 70 tuổi")
            
            st.markdown("---")
            st.write("### 🏁 KẾT LUẬN THẨM ĐỊNH TỰ ĐỘNG:")
            
            # --- KHỐI LOGIC CHẶN CỨNG (POLICY RULES) ---
            rejection_reasons = []
            
            # Kiểm tra luật rủi ro CIC và Lý do trả chậm
            if CIC == "Nhóm 3 đến 5 - Nợ xấu":
                rejection_reasons.append("Khách hàng có lịch sử nợ xấu nghiêm trọng (Nhóm 3-5) trên hệ thống CIC.")
            
            if CIC == "Nhóm 2 - Nợ cần chú ý":
                if "Lý do chủ quan" in ly_do_tra_cham or "Lý do cố ý" in ly_do_tra_cham:
                    rejection_reasons.append(f"Khách hàng thuộc Nhóm 2 do yếu tố rủi ro cao từ phía chủ quan: {ly_do_tra_cham}")
                elif so_lan_tra_cham > 3:
                    rejection_reasons.append(f"Khách hàng thuộc Nhóm 2 và tần suất trễ hạn quá nhiều ({so_lan_tra_cham} lần).")
            
            if "Lý do cố ý" in ly_do_tra_cham:
                rejection_reasons.append("Hệ thống phát hiện dấu hiệu cố ý chây ỳ hoặc tranh chấp nghĩa vụ trả nợ cũ.")
            
            if CIC == "Nhóm 1 - Nợ đủ tiêu chuẩn" and so_lan_tra_cham > 5:
                rejection_reasons.append(f"Tần suất trả chậm quá dày ({so_lan_tra_cham} lần) cảnh báo rủi ro quản lý dòng tiền của khách hàng.")

            # Kiểm tra luật rủi ro tài chính
            if DTI > 0.70:
                rejection_reasons.append(f"Chỉ số DTI ({DTI * 100:.2f}%) vượt ngưỡng an toàn cho phép là 70%.")
            if loai_vay != "Vay tiêu dùng tín chấp" and LTV > 0.70:
                rejection_reasons.append(f"Chỉ số LTV ({LTV * 100:.2f}%) vượt quá quy định 70% đối với khoản vay thế chấp.")
            if loai_vay == "Vay tiêu dùng tín chấp" and STV > 500:
                rejection_reasons.append("Hạn mức khoản vay tín chấp cá nhân vượt quá quy định tối đa (500 triệu đồng).")
            if STKH < 18 or STKH > 70:
                rejection_reasons.append(f"Độ tuổi hiện tại của khách hàng ({STKH} tuổi) nằm ngoài phạm vi cấp tín dụng (18 - 70 tuổi).")
            if Tich_Luy_Con_Lai < 0:
                rejection_reasons.append("Thu nhập thặng dư còn lại bị âm. Khách hàng không đủ tiền duy trì cuộc sống sau khi trả nợ.")
            if nghe_nghiep == "Lao động tự do / Tạm thời" and loai_vay == "Vay tiêu dùng tín chấp":
                rejection_reasons.append("Nguồn thu nhập không ổn định/không có chứng từ hợp pháp, không đủ điều kiện cấp tín chấp.")

            # Đưa ra thông báo cuối cùng
            if len(rejection_reasons) == 0:
                st.success("🎉 **CHẤP THUẬN CHO VAY (APPROVED)**")
                st.balloons()
                st.write("Hồ sơ hoàn hảo, đáp ứng tốt các quy định về uy tín, năng lực tài chính và phương án sử dụng vốn.")
            else:
                st.error("🚨 **TỪ CHỐI CHO VAY (REJECTED)**")
                st.markdown("**Các lý do không đạt chi tiết từ hệ thống:**")
                for reason in rejection_reasons:
                    st.write(f"- {reason}")
                    
        with tab2:
            st.write("### Tóm tắt thông tin hồ sơ thẩm định:")
            c_info1, c_info2 = st.columns(2)
            with c_info1:
                st.write(f"- **Loại sản phẩm tín dụng:** {loai_vay}")
                st.write(f"- **Mục đích giải ngân:** {muc_dich}")
                st.write(f"- **Phương thức hoàn trả:** {hinh_thuc_tra}")
                st.write(f"- **Cơ cấu nguồn thu:** Chính: `{nguon_chinh}` | Dự phòng: `{nguon_phu}`")
            with c_info2:
                st.write(f"- **Tình trạng hôn nhân:** {hon_nhan}")
                st.write(f"- **Nhóm nghề nghiệp:** {nghe_nghiep}")
                st.write(f"- **Lịch sử tín dụng:** {CIC} (Tần suất trả chậm: {so_lan_tra_cham} lần)")
                st.write(f"- **Nguyên nhân chậm trả:** {ly_do_tra_cham}")

            st.markdown("---")
            st.write("### Phân tích dòng tiền hàng tháng:")
            st.write(f"- 💵 **Khoản phải trả hàng tháng cho khoản vay mới:** `{PTMM:.2f}` Triệu đồng/tháng")
            st.write(f"- 💳 **Nghĩa vụ trả nợ các khoản vay cũ (nếu có):** `{PTMC:.2f}` Triệu đồng/tháng")
            st.write(f"- 💸 **Ước tính tổng chi phí sinh hoạt gia đình:** `{tong_chi_phi_sinh_hoat:.2f}` Triệu đồng/tháng")
            st.write(f"- 📈 **Thu nhập thặng dư còn lại để tích lũy:** `{Tich_Luy_Con_Lai:.2f}` Triệu đồng/tháng")

        with tab3:
            st.write("### Đánh giá định tính & Biện pháp giảm thiểu rủi ro:")
            
            if "Lý do khách quan" in ly_do_tra_cham and CIC == "Nhóm 2 - Nợ cần chú ý":
                st.warning("⚠️ **Gợi ý Thẩm định viên:** Khách hàng nợ Nhóm 2 nhưng do nguyên nhân quên/lỗi hệ thống. Có thể đề xuất phê duyệt ngoại lệ (Vượt thẩm quyền cấp Đơn vị) nếu bổ sung chứng từ chứng minh thanh toán ngay lập tức.")
            if "Lý do kỹ thuật" in ly_do_tra_cham:
                st.info("ℹ️ **Cơ cấu dòng tiền:** Khách hàng chậm do lệch kỳ lương. Khuyến nghị thiết lập Ngày trả nợ định kỳ dịch sang sau ngày nhận lương 2-3 ngày.")
            if hon_nhan == "Đã kết hôn" and nguon_phu == "Không có":
                st.warning("⚠️ Khách hàng đã lập gia đình nhưng chưa đưa thông tin Vợ/Chồng vào làm Người đồng vay nhằm tăng độ bao phủ nguồn thu.")
            if nghe_nghiep == "Kinh doanh tự do / Chủ doanh nghiệp":
                st.info("ℹ️ **Yêu cầu kiểm tra thực địa:** Cần thẩm định thực tế cơ sở kinh doanh, kiểm tra sổ sách/nhật ký bán hàng để xác thực thu nhập.")
            if len(rejection_reasons) == 0 and so_lan_tra_cham > 0:
                st.warning(f"⚠️ Khách hàng từng có lịch sử chậm trả nhẹ ({so_lan_tra_cham} lần). Khuyến nghị bắt buộc cài đặt dịch vụ trích nợ tự động (Auto-debit) tài khoản lương khi giải ngân.")
            if len(rejection_reasons) == 0 and so_lan_tra_cham == 0:
                st.write("✅ Hồ sơ sạch, lịch sử uy tín tín dụng tốt. Không ghi nhận cảnh báo định tính.")
                                
    except ZeroDivisionError:
        st.error("❌ Hệ thống không thể tính toán do có trường dữ liệu bằng 0 hoặc chưa hợp lệ. Vui lòng kiểm tra lại Giá trị tài sản đảm bảo hoặc Thời gian vay.")

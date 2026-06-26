import streamlit as st

# Cấu hình trang web
st.set_page_config(page_title="APP CHO VAY ONLINE KHCN - THUY HOAI", layout="wide")

st.title("🏦 APP THẨM ĐỊNH CHO VAY ONLINE KHCN - THUY HOAI - ĐỀ TÀI 6")
st.write("Hệ thống tự động thẩm định, phân tích rủi ro và phê duyệt tín dụng Khách hàng cá nhân.")

st.markdown("---")

# --- PHẦN 1: GIAO DIỆN NHẬP LIỆU ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 1. Thông tin khoản vay đề xuất")
    
    # Bổ sung loại, mục đích, hình thức và nguồn trả nợ
    loai_vay = st.selectbox("Loại khoản vay:", ["Vay tiêu dùng tín chấp", "Vay mua Ô tô (Thế chấp)", "Vay mua Bất động sản (Thế chấp)", "Vay sản xuất kinh doanh"])
    muc_dich = st.text_input("Mục đích vay cụ thể:", value="Mua nhà chung cư / Tiêu dùng gia đình")
    
    STV = st.number_input("Số tiền muốn vay (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian vay (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất cho vay (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    GTTSDB = st.number_input("Giá trị tài sản đảm bảo (Triệu đồng):", min_value=0.0, value=200.0, step=10.0)
    
    hinh_thuc_tra = st.selectbox("Hình thức trả nợ:", ["Gốc đều, lãi giảm dần (Kỳ đầu cao nhất)", "Gốc và lãi trả đều hàng tháng (Annuity)"])
    nguon_chinh = st.selectbox("Nguồn trả nợ chính:", ["Lương từ công việc cố định", "Thu nhập từ sản xuất kinh doanh", "Thu nhập từ cho thuê tài sản"])
    nguon_phu = st.selectbox("Nguồn trả nợ phụ (Dự phòng):", ["Không có", "Thu nhập của người đồng vay (Vợ/Chồng)", "Tài sản tích lũy khác"])

with col2:
    st.subheader("👤 2. Thông tin khách hàng & Uy tín (CIC)")
    
    STKH = st.number_input("Số tuổi của khách hàng (Tuổi):", min_value=0, max_value=120, value=30, step=1)
    hon_nhan = st.selectbox("Tình trạng hôn nhân:", ["Độc thân", "Đã kết hôn", "Ly hôn/Khác"])
    nghe_nghiep = st.selectbox("Nghề nghiệp/Lĩnh vực làm việc:", ["Nhân viên văn phòng (HĐLĐ vô thời hạn)", "Kinh doanh tự do / Chủ doanh nghiệp", "Công chức / Viên chức nhà nước", "Lao động tự do / Tạm thời"])
    
    TN = st.number_input("Thu nhập hàng tháng (Triệu đồng/tháng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người phụ thuộc (Người):", min_value=0, value=1, step=1)
    PTMC = st.number_input("Gốc lãi khoản vay cũ phải trả hàng tháng (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    # Bổ sung CIC chi tiết: Nhóm nợ và Số lần trả chậm
    CIC = st.selectbox(
        "Xếp hạng nhóm nợ (Hệ thống CIC):",
        ["Nhóm 1 - Nợ đủ tiêu chuẩn", "Nhóm 2 - Nợ cần chú ý", "Nhóm 3 đến 5 - Nợ xấu"]
    )
    so_lan_tra_cham = st.number_input("Số lần trả chậm trong 12 tháng qua (Tờ khai CIC):", min_value=0, value=0, step=1)

# --- PHẦN 2: TÍNH TOÁN DỰ KIẾN KHOẢN TRẢ HÀNG THÁNG ---
# Tính toán động ngay khi người dùng thay đổi dữ liệu để hiển thị số tiền trả dự kiến
TG_Thang = TGV * 12
if TG_Thang > 0:
    Goc_Hang_Thang = STV / TG_Thang
    if hinh_thuc_tra == "Gốc đều, lãi giảm dần (Kỳ đầu cao nhất)":
        Lai_Thang_Dau = STV * (LSV / 12)
        PTMM = Goc_Hang_Thang + Lai_Thang_Dau
    else:  # Annuity (Gốc lãi đều)
        r_monthly = LSV / 12
        if r_monthly > 0:
            PTMM = STV * (r_monthly * (1 + r_monthly)**TG_Thang) / ((1 + r_monthly)**TG_Thang - 1)
        else:
            PTMM = STV / TG_Thang
else:
    PTMM = 0.0
    Goc_Hang_Thang = 0.0
    Lai_Thang_Dau = 0.0

st.info(f"💡 **Khoản trả hàng tháng dự kiến (Kỳ đầu tiên/Ước tính):** `{PTMM:.2f}` Triệu đồng/tháng (Gốc: {Goc_Hang_Thang:.2f} tr, Lãi ước tính: {PTMM - Goc_Hang_Thang:.2f} tr)")

st.markdown("---")

# --- PHẦN 3: XỬ LÝ LOGIC THẨM ĐỊNH KHI BẤM NÚT ---
if st.button("📊 Kiểm tra kết quả thẩm định", type="primary"):
    try:
        # Tổng nghĩa vụ trả nợ hàng tháng
        Tong_No_Phai_Tra = PTMM + PTMC
        
        # Định mức chi phí sinh hoạt (Triệu đồng)
        CPSH_BAN_THAN = 5.0
        CPSH_PHU_THUOC = 3.5
        tong_chi_phi_sinh_hoat = CPSH_BAN_THAN + (SNPT * CPSH_PHU_THUOC)
        thu_nhap_rong = TN - tong_chi_phi_sinh_hoat
        
        # Chỉ số tài chính
        DTI = Tong_No_Phai_Tra / TN if TN > 0 else 1.0
        LTV = STV / GTTSDB if GTTSDB > 0 else 1.0
        Tich_Luy_Con_Lai = thu_nhap_rong - PTMM

        # Tabs hiển thị kết quả
        tab1, tab2, tab3 = st.tabs(["📈 Kết quả phân tích chỉ số", "📋 Hồ sơ & Nghĩa vụ dòng tiền", "⚠️ Khuyến nghị rủi ro"])
        
        with tab1:
            st.write("### Các chỉ số tài chính cốt lõi:")
            m1, m2, m3 = st.columns(3)
            m1.metric(label="Chỉ số DTI (Tổng nợ / Thu nhập)", value=f"{DTI * 100:.2f}%", delta="≤ 70% Tiêu chuẩn")
            m2.metric(label="Chỉ số LTV (Khoản vay / TSĐB)", value=f"{LTV * 100:.2f}%", delta="≤ 70% Tiêu chuẩn")
            m3.metric(label="Tuổi khách hàng", value=f"{STKH} tuổi", delta="18 - 70 tuổi")
            
            st.markdown("---")
            st.write("### 🏁 KẾT LUẬN THẨM ĐỊNH TỰ ĐỘNG:")
            
            # Thiết lập quy tắc chấm điểm (Hard-rules)
            rejection_reasons = []
            
            if CIC == "Nhóm 3 đến 5 - Nợ xấu":
                rejection_reasons.append("Khách hàng có nợ xấu lịch sử (Nhóm 3-5) trên hệ thống CIC.")
            if CIC == "Nhóm 2 - Nợ cần chú ý" and so_lan_tra_cham > 2:
                rejection_reasons.append(f"Khách hàng thuộc Nhóm 2 và có số lần trả chậm quá cao ({so_lan_tra_cham} lần).")
            if so_lan_tra_cham > 5:
                rejection_reasons.append(f"Tần suất trả chậm nghiêm trọng ({so_lan_tra_cham} lần trong năm qua) mặc dù đang ở Nhóm 1.")
            if DTI > 0.70:
                rejection_reasons.append(f"Chỉ số DTI ({DTI * 100:.2f}%) vượt ngưỡng an toàn 70%.")
            if loai_vay != "Vay tiêu dùng tín chấp" and LTV > 0.70:
                rejection_reasons.append(f"Chỉ số LTV ({LTV * 100:.2f}%) vượt quá 70% đối với khoản vay thế chấp.")
            if loai_vay == "Vay tiêu dùng tín chấp" and STV > 500:
                rejection_reasons.append("Khoản vay tín chấp vượt hạn mức tối đa cho phép (500 triệu).")
            if STKH < 18 or STKH > 70:
                rejection_reasons.append(f"Độ tuổi ({STKH} tuổi) ngoài quy định tối đa cho vay (18 - 70).")
            if Tich_Luy_Con_Lai < 0:
                rejection_reasons.append("Thu nhập thặng dư tích lũy bị âm sau khi trừ toàn bộ chi phí và nợ phải trả.")
            if nghe_nghiep == "Lao động tự do / Tạm thời" and loai_vay == "Vay tiêu dùng tín chấp":
                rejection_reasons.append("Nghề nghiệp rủi ro cao, không có nguồn thu nhập ổn định chứng minh cho khoản vay tín chấp.")

            if len(rejection_reasons) == 0:
                st.success("🎉 **CHẤP THUẬN CHO VAY (APPROVED)**")
                st.balloons()
            else:
                st.error("🚨 **TỪ CHỐI CHO VAY (REJECTED)**")
                st.markdown("**Lý do chi tiết từ hệ thống:**")
                for reason in rejection_reasons:
                    st.write(f"- {reason}")
                    
        with tab2:
            st.write("### Tóm tắt thông tin hồ sơ thẩm định:")
            c_info1, c_info2 = st.columns(2)
            with c_info1:
                st.write(f"- **Loại sản phẩm:** {loai_vay}")
                st.write(f"- **Mục đích giải ngân:** {muc_dich}")
                st.write(f"- **Phương thức hoàn trả:** {hinh_thuc_tra}")
                st.write(f"- **Cơ cấu nguồn thu:** Chính: `{nguon_chinh}` | Dự phòng: `{nguon_phu}`")
            with c_info2:
                st.write(f"- **Tình trạng hôn nhân:** {hon_nhan}")
                st.write(f"- **Nhóm nghề nghiệp:** {nghe_nghiep}")
                st.write(f"- **Lịch sử trả chậm:** {so_lan_tra_cham} lần")

            st.markdown("---")
            st.write("### Chi tiết dòng tiền hàng tháng:")
            st.write(f"- 💵 **Khoản trả hàng tháng dự kiến (Mới):** `{PTMM:.2f}` Triệu đồng/tháng")
            st.write(f"- 💳 **Khoản trả gốc lãi từ các tổ chức tín dụng khác (Cũ):** `{PTMC:.2f}` Triệu đồng/tháng")
            st.write(f"- 💸 **Ước tính chi phí sinh hoạt gia đình:** `{tong_chi_phi_sinh_hoat:.2f}` Triệu đồng/tháng")
            st.write(f"- 📈 **Thu nhập thặng dư còn lại để tích lũy:** `{Tich_Luy_Con_Lai:.2f}` Triệu đồng/tháng")

        with tab3:
            st.write("### Đánh giá định tính từ hệ thống rủi ro:")
            if hon_nhan == "Đã kết hôn" and nguon_phu == "Không có":
                st.warning("⚠️ Khách hàng đã kết hôn nhưng chưa đưa thu nhập của Vợ/Chồng vào nguồn thu bổ sung để tăng tỷ lệ an toàn.")
            if nghe_nghiep == "Kinh doanh tự do / Chủ doanh nghiệp":
                st.info("ℹ️ Cần thẩm định thực tế cơ sở kinh doanh để xác minh tính xác thực của dòng tiền thu nhập.")
            if so_lan_tra_cham > 0 and so_lan_tra_cham <= 2:
                st.warning(f"⚠️ Khách hàng có {so_lan_tra_cham} lần trả chậm nhẹ. Cần theo dõi sát tiến độ thanh toán nếu duyệt vay.")
            if len(rejection_reasons) == 0:
                st.write("✅ Hồ sơ sạch, không ghi nhận cảnh báo định tính đặc biệt.")
                                
    except ZeroDivisionError:
        st.error("❌ Hệ thống không thể tính toán do có trường dữ liệu bằng 0 hoặc chưa hợp lệ.")

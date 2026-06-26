import streamlit as st

# Cấu hình trang web
st.set_page_config(page_title="APP CHO VAY ONLINE KHCN - THUY HOAI", layout="wide")

st.title("🏦 APP THẨM ĐỊNH CHO VAY ONLINE KHCN - THUY HOAI - ĐỀ TÀI 6")
st.write("Hệ thống tự động thẩm định và phê duyệt điều kiện cấp tín dụng đối với Khách hàng cá nhân.")

st.markdown("---")

# Tạo 2 cột để nhập liệu trực quan hơn
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 1. Thông tin khoản vay đề xuất")
    STV = st.number_input("Số tiền muốn vay (Triệu đồng):", min_value=0.0, value=100.0, step=10.0)
    TGV = st.number_input("Thời gian vay (Số năm):", min_value=0.5, value=5.0, step=0.5)
    LSV = st.number_input("Lãi suất cho vay (%/năm):", min_value=0.0, max_value=50.0, value=10.0, step=0.5) / 100
    GTTSDB = st.number_input("Giá trị tài sản đảm bảo (Triệu đồng):", min_value=0.0, value=200.0, step=10.0)

with col2:
    st.subheader("👤 2. Thông tin khách hàng & Uy tín")
    STKH = st.number_input("Số tuổi của khách hàng (Tuổi):", min_value=0, max_value=120, value=30, step=1)
    TN = st.number_input("Thu nhập hàng tháng (Triệu đồng/tháng):", min_value=0.0, value=30.0, step=5.0)
    SNPT = st.number_input("Số người phụ thuộc (Người):", min_value=0, value=1, step=1)
    PTMC = st.number_input("Gốc lãi khoản vay cũ phải trả hàng tháng (Triệu đồng):", min_value=0.0, value=0.0, step=1.0)
    
    # Bổ sung chỉ số CIC rất quan trọng trong ngân hàng
    CIC = st.selectbox(
        "Lịch sử tín dụng (Hệ thống CIC):",
        ["Nhóm 1 - Nợ đủ tiêu chuẩn", "Nhóm 2 - Nợ cần chú ý", "Nhóm 3 đến 5 - Nợ xấu"]
    )

# Định mức chi phí sinh hoạt cơ bản cho bản thân khách hàng và người phụ thuộc (Triệu đồng)
CPSH_BAN_THAN = 5.0
CPSH_PHU_THUOC = 3.5

st.markdown("---")

# Nút bấm để kích hoạt tính toán
if st.button("📊 Kiểm tra kết quả thẩm định", type="primary"):
    
    try:
        # 1. Tính số tiền trả nợ hàng tháng cho khoản vay mới (Ước tính theo phương pháp dư nợ giảm dần/gốc đều lãi giảm dần kỳ đầu cao nhất)
        # Kỳ trả nợ đầu tiên (áp lực lớn nhất): Gốc hàng tháng + Lãi tháng đầu tiên
        TG_Thang = TGV * 12
        Goc_Hang_Thang = STV / TG_Thang
        Lai_Thang_Dau = STV * (LSV / 12)
        PTMM = Goc_Hang_Thang + Lai_Thang_Dau
        
        # Tổng nghĩa vụ trả nợ hàng tháng
        Tong_No_Phai_Tra = PTMM + PTMC
        
        # 2. Tính toán Thu nhập ròng (Thu nhập thặng dư sau khi trừ chi phí sinh hoạt)
        tong_chi_phi_sinh_hoat = CPSH_BAN_THAN + (SNPT * CPSH_PHU_THUOC)
        thu_nhap_rong = TN - tong_chi_phi_sinh_hoat
        
        # 3. Tính toán các chỉ số DTI và LTV
        DTI = Tong_No_Phai_Tra / TN if TN > 0 else 1.0  # DTI tính trên tổng thu nhập trước thuế/chi phí theo chuẩn quốc tế
        LTV = STV / GTTSDB if GTTSDB > 0 else 1.0
        
        # Tính thu nhập tích lũy còn lại sau khi trả nợ
        Tich_Luy_Con_Lai = thu_nhap_rong - PTMM

        # Giao diện hiển thị kết quả bằng Tabs cho chuyên nghiệp
        tab1, tab2 = st.tabs(["📈 Kết quả phân tích chỉ số", "📋 Chi tiết nghĩa vụ tài chính"])
        
        with tab1:
            st.write("### Các chỉ số tài chính cốt lõi:")
            
            # Sử dụng cột và st.metric để hiển thị đẹp mắt
            m1, m2, m3 = st.columns(3)
            m1.metric(label="Chỉ số DTI (Nợ / Thu nhập)", value=f"{DTI * 100:.2f}%", delta="≤ 70% Tiêu chuẩn")
            m2.metric(label="Chỉ số LTV (Vay / TSĐB)", value=f"{LTV * 100:.2f}%", delta="≤ 70% Tiêu chuẩn")
            m3.metric(label="Tuổi khách hàng", value=f"{STKH} tuổi", delta="18 - 70 tuổi")
            
            st.markdown("---")
            st.write("### 🏁 KẾT LUẬN THẨM ĐỊNH TỰ ĐỘNG:")
            
            # Khởi tạo danh sách lý do từ chối nếu có
            rejection_reasons = []
            
            # Hệ thống điều kiện phê duyệt
            if CIC == "Nhóm 3 đến 5 - Nợ xấu":
                rejection_reasons.append("Khách hàng đang có nợ xấu trên hệ thống CIC (Nhóm 3-5).")
            if CIC == "Nhóm 2 - Nợ cần chú ý":
                rejection_reasons.append("Khách hàng thuộc nhóm nợ cần chú ý (Nhóm 2), rủi ro chậm trả cao.")
            if DTI > 0.70:
                rejection_reasons.append(f"Chỉ số DTI quá cao ({DTI * 100:.2f}% > 70%). Áp lực trả nợ vượt ngưỡng an toàn.")
            if LTV > 0.70:
                rejection_reasons.append(f"Chỉ số LTV quá cao ({LTV * 100:.2f}% > 70%). Giá trị tài sản đảm bảo không đủ che phủ khoản vay.")
            if STKH < 18 or STKH > 70:
                rejection_reasons.append(f"Độ tuổi khách hàng ({STKH} tuổi) nằm ngoài phạm vi quy định (18 - 70 tuổi).")
            if Tich_Luy_Con_Lai < 0:
                rejection_reasons.append("Thu nhập thặng dư bị âm sau khi trừ chi phí sinh hoạt và khoản phải trả mới.")

            # Trả ra kết quả phê duyệt cuối cùng
            if len(rejection_reasons) == 0:
                st.success("🎉 **CHẤP THUẬN CHO VAY (APPROVED)**")
                st.balloons()
                st.write("Khách hàng đáp ứng đầy đủ các tiêu chí về uy tín CIC, năng lực tài chính và tài sản bảo đảm.")
            else:
                st.error("🚨 **TỪ CHỐI CHO VAY (REJECTED)**")
                st.markdown("**Lý do không đạt chi tiết:**")
                for reason in rejection_reasons:
                    st.write(f"- {reason}")
                    
        with tab2:
            st.write("### Chi tiết dòng tiền hàng tháng (Kỳ đầu tiên):")
            st.write(f"- 💵 **Gốc phải trả khoản vay mới:** `{Goc_Hang_Thang:.2f}` Triệu đồng/tháng")
            st.write(f"- 📉 **Lãi phải trả (kỳ đầu) khoản vay mới:** `{Lai_Thang_Dau:.2f}` Triệu đồng/tháng")
            st.write(f"- 💰 **Tổng số tiền phải trả cho khoản mới (Ước tính):** `{PTMM:.2f}` Triệu đồng/tháng")
            st.write(f"- 💸 **Ước tính tổng chi phí sinh hoạt gia đình:** `{tong_chi_phi_sinh_hoat:.2f}` Triệu đồng/tháng")
            st.write(f"- 📈 **Số tiền tích lũy thặng dư còn lại:** `{Tich_Luy_Con_Lai:.2f}` Triệu đồng/tháng")
                                
    except ZeroDivisionError:
        st.error("❌ Có lỗi xảy ra do nhập giá trị bằng 0 ở các mục tính toán (Thời gian vay hoặc Giá trị tài sản đảm bảo).")

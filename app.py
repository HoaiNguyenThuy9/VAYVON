import streamlit as st

# Thiết lập cấu hình trang
st.set_page_config(page_title="App Thẩm Định Cho Vay Cá Nhân", layout="wide")

st.title("📊 HỆ THỐNG THẨM ĐỊNH CHO VAY KHÁCH HÀNG CÁ NHÂN")
st.write("Nhập các thông tin dưới đây để hệ thống tự động đánh giá điều kiện cấp tín dụng.")

---

# Chia giao diện thành 2 cột: Cột nhập liệu và Cột kết quả
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📝 Thông tin Khoản Vay & Khách Hàng")
    
    ### 1. Thông tin khoản vay đề xuất
    st.subheader("1. Khoản vay đề xuất")
    loan_amount = st.number_input("Số tiền đề nghị vay (VND)", min_value=0.0, value=500000000.0, step=10000000.0, format="%f")
    loan_term = st.number_input("Thời gian vay (tháng)", min_value=1, value=60, step=1)
    interest_rate = st.number_input("Lãi suất cho vay (%/năm)", min_value=0.0, value=10.5, step=0.1)

    ### 2. Thông tin tài chính & Khách hàng
    st.subheader("2. Năng lực tài chính & Nhân thân")
    monthly_income = st.number_input("Thu nhập hằng tháng của khách hàng (VND)", min_value=0.0, value=30000000.0, step=1000000.0, format="%f")
    dependents = st.number_input("Số người phụ thuộc", min_value=0, value=1, step=1)
    existing_debt_service = st.number_input("Gốc lãi khoản vay cũ phải trả hằng tháng (VND)", min_value=0.0, value=2000000.0, step=500000.0, format="%f")

    ### 3. Tài sản đảm bảo (TSĐB) & Uy tín tín dụng
    st.subheader("3. Tài sản đảm bảo & Uy tín (CIC)")
    collateral_value = st.number_input("Giá trị Tài sản đảm bảo (VND)", min_value=0.0, value=1000000000.0, step=50000000.0, format="%f")
    cic_status = st.selectbox("Nhóm nợ CIC (Tra cứu hệ thống)", ["Nhóm 1 (Nợ đủ tiêu chuẩn)", "Nhóm 2 (Nợ cần chú ý)", "Nhóm 3-5 (Nợ xấu)"])

---

with col2:
    st.header("📈 Kết Quả Tính Toán & Thẩm Định")
    
    # --- LOGIC TÍNH TOÁN CÁC CHỈ SỐ ---
    
    # 1. Tính gốc lãi hằng tháng của khoản vay mới (Ước tính theo phương pháp trả đều - Annuity)
    r_monthly = (interest_rate / 100) / 12
    if r_monthly > 0:
        new_debt_service = loan_amount * (r_monthly * (1 + r_monthly)**loan_term) / ((1 + r_monthly)**loan_term - 1)
    else:
        new_debt_service = loan_amount / loan_term

    # 2. Tính LTV (Loan to Value) - Tỷ lệ cho vay trên giá trị TSĐB
    if collateral_value > 0:
        ltv = (loan_amount / collateral_value) * 100
    else:
        ltv = 100.0 if loan_amount > 0 else 0.0

    # 3. Tính DTI (Debt-to-Income) - Tỷ lệ nợ trên thu nhập
    # Tổng nghĩa vụ trả nợ hằng tháng = Khoản cũ + Khoản mới đề xuất
    total_monthly_debt = existing_debt_service + new_debt_service
    if monthly_income > 0:
        dti = (total_monthly_debt / monthly_income) * 100
    else:
        dti = 100.0

    # 4. Tính Thu nhập thặng dư (Disposable Income) sau khi trừ chi phí sinh hoạt ước tính (ví dụ: 4 triệu/người phụ thuộc + 5 triệu bản thân)
    estimated_living_cost = 5000000 + (dependents * 4000000)
    disposable_income = monthly_income - total_monthly_debt - estimated_living_cost

    # --- HIỂN THỊ CHỈ SỐ ---
    st.metric(label="Gốc + Lãi phải trả hằng tháng (Khoản mới)", value=f"{new_debt_service:,.0f} VND")
    
    col_ltv, col_dti = st.columns(2)
    with col_ltv:
        st.metric(label="Tỷ lệ LTV (Số tiền vay / TSĐB)", value=f"{ltv:.2f}%")
    with col_dti:
        st.metric(label="Tỷ lệ DTI (Tổng nợ / Thu nhập)", value=f"{dti:.2f}%")
        
    st.metric(label="Thu nhập thặng dư ước tính", value=f"{disposable_income:,.0f} VND")

    st.markdown("---")
    st.subheader("🏁 ĐÁNH GIÁ ĐIỀU KIỆN CHO VAY")

    # --- LOGIC RA QUYẾT ĐỊNH (THẨM ĐỊNH TỰ ĐỘNG) ---
    rejection_reasons = []

    # Quy tắc 1: Kiểm tra CIC
    if cic_status != "Nhóm 1 (Nợ đủ tiêu chuẩn)":
        rejection_reasons.append(f"Khách hàng có lịch sử tín dụng xấu ({cic_status}).")

    # Quy tắc 2: Kiểm tra DTI (Thông thường ngân hàng quy định DTI <= 55% - 60%)
    if dti > 60:
        rejection_reasons.append(f"Tỷ lệ DTI quá cao ({dti:.2f}% > 60%). Khách hàng không đủ khả năng trả nợ.")

    # Quy tắc 3: Kiểm tra LTV (Thông thường LTV đối với BĐS <= 70%, Động sản <= 60%)
    if ltv > 70:
        rejection_reasons.append(f"Tỷ lệ LTV vượt ngưỡng an toàn ({ltv:.2f}% > 70%). Thiếu tài sản đảm bảo.")

    # Quy tắc 4: Kiểm tra Thu nhập thặng dư
    if disposable_income < 0:
        rejection_reasons.append("Thu nhập thặng dư bị âm sau khi trừ chi phí sinh hoạt và nghĩa vụ trả nợ.")

    # Hiển thị kết quả thẩm định
    if len(rejection_reasons) == 0:
        st.success("🟢 KẾT LUẬN: ĐỀ XUẤT PHÊ DUYỆT KHOẢN VAY")
        st.write("Khách hàng đáp ứng đầy đủ các tiêu chí cơ bản về năng lực tài chính, tài sản đảm bảo và uy tín tín dụng.")
    else:
        st.error("🔴 KẾT LUẬN: TỪ CHỐI CHO VAY (HOẶC CẦN GIẢM SỐ TIỀN VAY)")
        st.write("**Lý do từ chối:**")
        for reason in rejection_reasons:
            st.write(f"- {reason}")

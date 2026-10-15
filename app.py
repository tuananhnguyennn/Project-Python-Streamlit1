import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# --- PHẦN 1: XỬ LÝ DỮ LIỆU ---
data = {
    'Họ và tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [9.0, 8.5, 7.0, 10.0, 6.5, 8.0, 9.5, 5.0, 7.5, 8.5],
    'Giữa kỳ': [8.0, 7.5, 6.5, 9.0, 7.0, 8.5, 8.0, 5.5, 6.0, 8.0],
    'Cuối kỳ': [8.5, 8.0, 7.0, 9.5, 6.0, 9.0, 8.5, 4.5, 7.0, 8.5]
}
df = pd.DataFrame(data)

# Tính tổng kết và xếp loại
df['Tong_ket'] = 0.2 * df['Chuyên cần'] + 0.3 * df['Giữa kỳ'] + 0.5 * df['Cuối kỳ']

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# --- PHẦN 2: GIAO DIỆN STREAMLIT ---
# 1. Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 2. Bảng điểm
st.subheader("1. Bảng điểm chi tiết")
st.dataframe(df)

# 3. Thống kê
st.subheader("2. Thống kê chung")
diem_tb = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = len(df[df['Tong_ket'] >= 5.0])

st.write(f"- **Điểm trung bình của lớp:** {diem_tb:.2f}")
st.write(f"- **Sinh viên cao điểm nhất:** {sv_max['Họ và tên']} ({sv_max['Tong_ket']} điểm)")
st.write(f"- **Sinh viên thấp điểm nhất:** {sv_min['Họ và tên']} ({sv_min['Tong_ket']} điểm)")
st.write(f"- **Số sinh viên đạt (>= 5.0):** {so_sv_dat}")

# 4. Tra cứu sinh viên
st.subheader("3. Tra cứu điểm sinh viên")
# Tạo danh sách xổ xuống
sv_chon = st.selectbox("Chọn tên sinh viên:", df['Họ và tên'])

# Hiển thị thông tin sinh viên được chọn
thong_tin = df[df['Họ và tên'] == sv_chon].iloc[0]
st.write(f"- **Họ tên:** {thong_tin['Họ và tên']}")
st.write(f"- **Chuyên cần:** {thong_tin['Chuyên cần']} | **Giữa kỳ:** {thong_tin['Giữa kỳ']} | **Cuối kỳ:** {thong_tin['Cuối kỳ']}")
st.write(f"- **Tổng kết:** {thong_tin['Tong_ket']} | **Xếp loại:** {thong_tin['Xep_loai']}")

# 5. Biểu đồ
st.subheader("4. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df['Họ và tên'], df['Tong_ket'], color='teal')
ax.set_title('Điểm tổng kết của sinh viên')
ax.set_xlabel('Họ và tên')
ax.set_ylabel('Điểm')
ax.set_ylim(0, 10)
st.pyplot(fig)

# 6. Footer thông tin sinh viên
st.markdown("---")
# ĐỪNG QUÊN THAY TÊN VÀ MSSV CỦA BẠN VÀO ĐÂY
st.markdown("<h6 style='text-align: center; color: gray;'>Người thực hiện: NGUYỄN VĂN A - MSSV: 12345678</h6>", unsafe_allow_html=True)
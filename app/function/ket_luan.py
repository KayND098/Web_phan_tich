import pandas as pd
import streamlit as st

DATA_PATH = r"app/database/market_data_6mo.csv"

def phan_tich_tuong_quan(data_path=DATA_PATH):
    # Đọc dữ liệu
    df = pd.read_csv(data_path, parse_dates=["Date"])
    df.set_index("Date", inplace=True)

    # Tính hệ số tương quan
    corr = df.corr()

    st.subheader("📊 Ma trận tương quan")
    st.dataframe(corr.style.background_gradient(cmap="coolwarm").format("{:.2f}"))

    # Hàm kết luận (chữ trắng)
    def ket_luan(x, y, label_x, label_y):
        value = corr.loc[x, y]
        if value > 0.5:
            st.markdown(f"<span style='color:white'>* {label_x} tăng thì {label_y} cũng tăng (tương quan dương mạnh: {value:.2f})</span>", unsafe_allow_html=True)
        elif value < -0.5:
            st.markdown(f"<span style='color:white'>* {label_x} tăng thì {label_y} giảm (tương quan âm mạnh: {value:.2f})</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:white'>* {label_x} và {label_y} có tương quan yếu ({value:.2f})</span>", unsafe_allow_html=True)

    st.subheader("|| Kết luận hành vi mua sắm")
    ket_luan("Gia_vang", "So_nguoi_mua", "Giá vàng", "số người mua")
    ket_luan("Gia_vang", "So_nguoi_ban", "Giá vàng", "số người bán")
    ket_luan("Chi_so_bien_dong", "So_nguoi_mua", "Chỉ số biến động (VIX)", "số người mua")
    ket_luan("Lai_suat_%", "So_nguoi_mua", "Lãi suất", "số người mua")
    ket_luan("Ty_gia_USD_VND", "Gia_vang", "Tỷ giá USD/VND", "giá vàng")

    st.subheader("|| Phân tích bổ sung hành vi người mua vàng")
    st.subheader("|| Phân tích bổ sung hành vi người mua vàng")

    if corr.at["Gia_vang", "So_nguoi_mua"] < -0.5:
        st.markdown("<span style='color:white'>* Người mua vàng có xu hướng tăng khi giá vàng giảm (mua tích trữ).</span>", unsafe_allow_html=True)

    if corr.at["Chi_so_bien_dong", "So_nguoi_mua"] > 0.5:
        st.markdown("<span style='color:white'>* Người mua vàng tăng khi thị trường biến động mạnh (tìm nơi trú ẩn an toàn).</span>", unsafe_allow_html=True)

    if corr.at["Lai_suat_%", "So_nguoi_mua"] < -0.5:
        st.markdown("<span style='color:white'>* Người mua vàng giảm khi lãi suất cao (ưu tiên gửi tiết kiệm).</span>", unsafe_allow_html=True)

    if (corr.at["Ty_gia_USD_VND", "Gia_vang"] > 0.5) and (corr.at["Gia_vang", "So_nguoi_mua"] < -0.5):
        st.markdown("<span style='color:white'>* USD tăng làm giá vàng trong nước tăng, dẫn đến người mua vàng giảm.</span>", unsafe_allow_html=True)

    return corr


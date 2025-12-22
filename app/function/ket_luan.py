import pandas as pd
import streamlit as st
import plotly.express as px

DATA_PATH = r"app/database/market_data_6mo.csv"

REQUIRED_COLS = [
    "Gia_vang", "Gia_dau", "Chi_so_bien_dong", "Ty_gia_USD_VND",
    "Gia_vang_the_gioi", "Lai_suat_%", "So_nguoi_mua", "So_nguoi_ban"
]

def phan_tich_tuong_quan(data_path=DATA_PATH):
    # 1) Đọc dữ liệu & làm sạch tên cột
    df = pd.read_csv(data_path, parse_dates=["Date"])
    df.columns = df.columns.str.strip()
    df.set_index("Date", inplace=True)

    # 2) Kiểm tra cột bắt buộc
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        st.error(f"Thiếu cột trong CSV: {missing}")
        return None

    # 3) Tính hệ số tương quan
    corr = df.corr(numeric_only=True)

    # Tiêu đề chính màu trắng
    st.markdown("<h1 style='color:white'>📊 Dashboard phân tích tương quan thị trường vàng</h1>", unsafe_allow_html=True)

    # Heatmap tương quan
    st.markdown("<h2 style='color:white'>🔎 Ma trận tương quan</h2>", unsafe_allow_html=True)
    fig_corr = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r")
    fig_corr.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(240,240,240,0.3)")
    st.plotly_chart(fig_corr, use_container_width=True)

    # Biểu đồ đường
    st.markdown("<h2 style='color:white'>📉 Diễn biến giá vàng và số người mua</h2>", unsafe_allow_html=True)
    fig_line = px.line(df.reset_index(), x="Date", y=["Gia_vang", "So_nguoi_mua"],
                       labels={"value": "Giá trị", "Date": "Ngày"},
                       title="Giá vàng vs Người mua theo thời gian")
    fig_line.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(240,240,240,0.3)")
    st.plotly_chart(fig_line, use_container_width=True)

    # Biểu đồ cột
    st.markdown("<h2 style='color:white'>📊 So sánh số người mua/bán</h2>", unsafe_allow_html=True)
    fig_bar = px.bar(df.reset_index(), x="Date", y=["So_nguoi_mua", "So_nguoi_ban"],
                     barmode="group", title="Người mua vs Người bán")
    fig_bar.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(240,240,240,0.3)")
    st.plotly_chart(fig_bar, use_container_width=True)

    # Scatter plot
    st.markdown("<h2 style='color:white'>🔗 Quan hệ giữa giá vàng và số người mua</h2>", unsafe_allow_html=True)
    fig_scatter = px.scatter(df, x="Gia_vang", y="So_nguoi_mua",
                             trendline="ols", title="Tương quan Giá vàng - Người mua")
    fig_scatter.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(240,240,240,0.3)")
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Kết luận
    st.markdown("<h2 style='color:white'>📌 Kết luận phân tích</h2>", unsafe_allow_html=True)
    try:
        if corr.at["Gia_vang", "So_nguoi_mua"] < -0.5:
            st.markdown("<span style='color:white'>* Người mua vàng có xu hướng tăng khi giá vàng giảm (mua tích trữ).</span>", unsafe_allow_html=True)
        if corr.at["Chi_so_bien_dong", "So_nguoi_mua"] > 0.5:
            st.markdown("<span style='color:white'>* Người mua vàng tăng khi thị trường biến động mạnh (trú ẩn an toàn).</span>", unsafe_allow_html=True)
        if corr.at["Lai_suat_%", "So_nguoi_mua"] < -0.5:
            st.markdown("<span style='color:white'>* Người mua vàng giảm khi lãi suất cao (ưu tiên gửi tiết kiệm).</span>", unsafe_allow_html=True)
        if (corr.at["Ty_gia_USD_VND", "Gia_vang"] > 0.5) and (corr.at["Gia_vang", "So_nguoi_mua"] < -0.5):
            st.markdown("<span style='color:white'>* USD tăng làm giá vàng trong nước tăng, dẫn đến người mua vàng giảm.</span>", unsafe_allow_html=True)
    except KeyError as e:
        st.error(f"Không tìm thấy cột trong ma trận tương quan: {e}")

    return corr

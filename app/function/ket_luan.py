import pandas as pd
import streamlit as st
import plotly.express as px

DATA_PATH = r"app/database/market_data_6mo.csv"

def phan_tich_tuong_quan(data_path=DATA_PATH):
    # 1. Đọc dữ liệu
    df = pd.read_csv(data_path, parse_dates=["Date"])
    df.set_index("Date", inplace=True)

    # 2. Tính hệ số tương quan
    corr = df.corr()

    # 3. Hiển thị dashboard
    st.title("📊 Dashboard phân tích tương quan thị trường vàng")

    # Heatmap tương quan
    st.subheader("🔎 Ma trận tương quan")
    fig_corr = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r")
    st.plotly_chart(fig_corr, use_container_width=True)

    # Biểu đồ đường: Giá vàng vs Người mua
    st.subheader("📉 Diễn biến giá vàng và số người mua")
    fig_line = px.line(df, x=df.index, y=["Gia_vang", "So_nguoi_mua"],
                       labels={"value":"Giá trị", "Date":"Ngày"},
                       title="Giá vàng vs Người mua theo thời gian")
    st.plotly_chart(fig_line, use_container_width=True)

    # Biểu đồ cột: Người mua vs Người bán
    st.subheader("📊 So sánh số người mua/bán")
    fig_bar = px.bar(df, x=df.index, y=["So_nguoi_mua", "So_nguoi_ban"],
                     barmode="group", title="Người mua vs Người bán")
    st.plotly_chart(fig_bar, use_container_width=True)

    # Scatter plot: Giá vàng vs Người mua
    st.subheader("🔗 Quan hệ giữa giá vàng và số người mua")
    fig_scatter = px.scatter(df, x="Gia_vang", y="So_nguoi_mua",
                             trendline="ols",
                             title="Tương quan Giá vàng - Người mua")
    st.plotly_chart(fig_scatter, use_container_width=True)

    # 4. Kết luận phân tích
    st.subheader("📌 Kết luận phân tích")
    try:
        if corr.at["Gia_vang", "So_nguoi_mua"] < -0.5:
            st.markdown("* Người mua vàng có xu hướng tăng khi giá vàng giảm (mua tích trữ).")
        if corr.at["Chi_so_bien_dong", "So_nguoi_mua"] > 0.5:
            st.markdown("* Người mua vàng tăng khi thị trường biến động mạnh (tìm nơi trú ẩn an toàn).")
        if corr.at["Lai_suat_%", "So_nguoi_mua"] < -0.5:
            st.markdown("* Người mua vàng giảm khi lãi suất cao (ưu tiên gửi tiết kiệm).")
        if (corr.at["Ty_gia_USD_VND", "Gia_vang"] > 0.5) and (corr.at["Gia_vang", "So_nguoi_mua"] < -0.5):
            st.markdown("* USD tăng làm giá vàng trong nước tăng, dẫn đến người mua vàng giảm.")
    except KeyError as e:
        st.error(f"Không tìm thấy cột trong dữ liệu: {e}")

    # 5. Trả về ma trận tương quan để dùng tiếp
    return corr

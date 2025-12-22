import pandas as pd
import streamlit as st
import plotly.express as px

DATA_PATH = r"app/database/market_data_6mo.csv"

def phan_tich_tuong_quan(data_path=DATA_PATH):
    # Đọc dữ liệu
    df = pd.read_csv(data_path, parse_dates=["Date"])
    df.set_index("Date", inplace=True)

    # Tính hệ số tương quan
    corr = df.corr()

    st.title("📊 Dashboard phân tích thị trường vàng")

    # 1. Heatmap tương quan (giống Tableau)
    st.subheader("🔎 Ma trận tương quan")
    fig_corr = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r")
    st.plotly_chart(fig_corr, use_container_width=True)

    # 2. Biểu đồ đường (trend theo thời gian)
    st.subheader("📉 Diễn biến giá vàng và số người mua")
    fig_line = px.line(df, x=df.index, y=["Gia_vang", "So_nguoi_mua"],
                       labels={"value":"Giá trị", "Date":"Ngày"},
                       title="Giá vàng vs Người mua theo thời gian")
    st.plotly_chart(fig_line, use_container_width=True)

    # 3. Biểu đồ cột (so sánh người mua/bán)
    st.subheader("📊 So sánh số người mua/bán")
    fig_bar = px.bar(df, x=df.index, y=["So_nguoi_mua", "So_nguoi_ban"],
                     barmode="group", title="Người mua vs Người bán")
    st.plotly_chart(fig_bar, use_container_width=True)

    # 4. Scatter plot (quan hệ giữa biến)
    st.subheader("🔗 Quan hệ giữa giá vàng và số người mua")
    fig_scatter = px.scatter(df, x="Gia_vang", y="So_nguoi_mua",
                             trendline="ols",
                             title="Tương quan Giá vàng - Người mua")
    st.plotly_chart(fig_scatter, use_container_width=True)

    return corr





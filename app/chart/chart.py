import pandas as pd
import matplotlib.pyplot as plt

# Đường dẫn dữ liệu
DATA_PATH = r"C:\Users\ngokh\Documents\BTL T4\database\market_data_6mo.csv"

# Hàm chung để vẽ biểu đồ (nền trong suốt + chi tiết màu #CC9933)
def plot_minimal(df, column, title, ylabel=""):
    fig, ax = plt.subplots(figsize=(16, 6))

    # Vẽ đường dữ liệu màu #CC9933
    ax.plot(df.index, df[column], color="#00FFFF")

    # Nền trong suốt
    fig.patch.set_alpha(0.1)   # nền ngoài
    ax.patch.set_alpha(0.1)    # nền trong

    # Tiêu đề và nhãn màu #CC9933
    ax.set_title(title, color="#CC66FF")
    ax.set_ylabel(ylabel, color="#CC66FF")

    # Trục X, Y màu #CC9933
    ax.tick_params(axis='x', colors="#00FFFF")
    ax.tick_params(axis='y', colors="#00FFFF")

    # Đổi màu spines (khung trục) thành #CC9933
    for spine in ax.spines.values():
        spine.set_color("#CC9933")

    return fig

# Các hàm biểu đồ riêng
def Gia_vang():
    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    return plot_minimal(df, "Gia_vang", "Giá Vàng", "Giá vàng trong nước")

def Gia_dau():
    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    return plot_minimal(df, "Gia_dau", "Giá dầu biến động", "Giá dầu")

def Gia_vang_tg():
    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    return plot_minimal(df, "Gia_vang_tg", "Giá vàng thế giới biến động", "Giá vàng TG")

def Chi_so_bien_dong():
    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    return plot_minimal(df, "Chi_so_bien_dong", "Chỉ số biến động", "Chỉ số")

def Ty_gia():
    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    return plot_minimal(df, "Ty_gia_USD_VND", "Tỷ giá USD/VND", "USD/VND")
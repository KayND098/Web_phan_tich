import yfinance as yf
import pandas as pd

# Lấy dữ liệu 6 tháng từ Yahoo Finance
gold = yf.Ticker("GC=F").history(period="6mo")[["Close"]].rename(columns={"Close": "Gia_vang"})          # Giá vàng (Gold Futures)
oil = yf.Ticker("CL=F").history(period="6mo")[["Close"]].rename(columns={"Close": "Gia_dau"})            # Giá dầu (Crude Oil Futures)
vix = yf.Ticker("^VIX").history(period="6mo")[["Close"]].rename(columns={"Close": "Chi_so_bien_dong"})   # Chỉ số biến động VIX
usd_vnd = yf.Ticker("USDVND=X").history(period="6mo")[["Close"]].rename(columns={"Close": "Ty_gia_USD_VND"}) # Tỷ giá USD/VND
xauusd = yf.Ticker("GLD").history(period="6mo")[["Close"]].rename(columns={"Close": "Gia_vang_the_gioi"})   # Giá vàng thế giới (ETF GLD)

# Nhập tay lãi suất (ví dụ 4%/năm) cho tất cả các ngày
lai_suat_value = 0.4
lai_suat = pd.DataFrame({"Lai_suat_%": [lai_suat_value] * len(gold)}, index=gold.index)

# Gộp tất cả dữ liệu theo Date
combined = pd.concat([gold, oil, vix, usd_vnd, xauusd, lai_suat], axis=1)

# Nếu có giá trị NaN thì điền bằng dữ liệu hôm qua (forward fill),
# nếu ngày đầu tiên trống thì lấy dữ liệu ngày sau (backward fill)
combined = combined.fillna(method="ffill").fillna(method="bfill")

# Xuất ra file CSV duy nhất
combined.to_csv("market_data_6mo.csv")



import numpy as np

# Chuẩn hóa giá vàng thế giới để làm thước đo
gia_vang = combined["Gia_vang_the_gioi"]

# Giả lập số người mua: tỷ lệ nghịch với giá vàng
so_nguoi_mua = (max(gia_vang) - gia_vang) / (max(gia_vang) - min(gia_vang)) * 5000
so_nguoi_mua = so_nguoi_mua.astype(int)
so_nguoi_mua = np.maximum(1000, so_nguoi_mua)  # đảm bảo >=1000

# Giả lập số người bán: tỷ lệ thuận với giá vàng
so_nguoi_ban = (gia_vang - min(gia_vang)) / (max(gia_vang) - min(gia_vang)) * 5000
so_nguoi_ban = so_nguoi_ban.astype(int)
so_nguoi_ban = np.maximum(1000, so_nguoi_ban)  # đảm bảo >=1000

# Thêm vào DataFrame
combined["So_nguoi_mua"] = so_nguoi_mua
combined["So_nguoi_ban"] = so_nguoi_ban

# Xuất lại file CSV
combined.to_csv("market_data_6mo.csv")

print("Đã xuất dữ liệu với quy luật: giá vàng tăng thì người mua giảm, người bán tăng (>=1000)")
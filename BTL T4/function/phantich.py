import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv("market_data_6mo.csv", parse_dates=["Date"])
df.set_index("Date", inplace=True)

# 1. Tính hệ số tương quan giữa các biến
corr = df.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap tương quan giữa các biến")
plt.show()

# 2. Scatter plot: Giá vàng vs Số người mua
plt.figure(figsize=(8,6))
plt.scatter(df["Gia_vang"], df["So_nguoi_mua"], alpha=0.6, color="gold")
plt.title("Mối quan hệ giữa Giá vàng và Số người mua")
plt.xlabel("Giá vàng")
plt.ylabel("Số người mua")
plt.grid(True)
plt.show()

# 3. Scatter plot: Giá vàng vs Số người bán
plt.figure(figsize=(8,6))
plt.scatter(df["Gia_vang"], df["So_nguoi_ban"], alpha=0.6, color="red")
plt.title("Mối quan hệ giữa Giá vàng và Số người bán")
plt.xlabel("Giá vàng")
plt.ylabel("Số người bán")
plt.grid(True)
plt.show()
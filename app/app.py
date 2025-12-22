import streamlit as st
import pandas as pd
import base64, os
from config import account
from config.pre_clas import cla, pre
from chart.chart import Gia_vang, Gia_dau, Gia_vang_tg, Chi_so_bien_dong, Ty_gia

st.set_page_config(layout="wide")

# --- Hàm đọc ảnh nền ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = r"app/web.jpg"
if os.path.exists(img_path):
    img_base64 = get_base64_of_bin_file(img_path)
    page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# --- CSS cho button ---
button_style = """
<style>
div.stButton > button {
    background-color: #0A3D62;
    color: #CC9933;
    border-radius: 8px;
    border: 2px solid #CC9933;
    height: 40px;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #CC9933;
    color: #0A3D62;
}
</style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# --- Đăng nhập / đăng ký ---
if account.current_user is None:
    col_empty, col_buttons, col_empty2 = st.columns([1,2,1])
    with col_buttons:
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("Đăng ký", use_container_width=True):
                st.session_state.action = "register"
        with col2:
            if st.button("Đăng nhập", use_container_width=True):
                st.session_state.action = "login"

    if "action" in st.session_state:
        col_empty, col_form, col_empty2 = st.columns([1,2,1])
        with col_form:
            if st.session_state.action == "register":
                st.subheader("Đăng ký tài khoản")
                email = st.text_input(" Email")
                username = st.text_input(" Tên đăng nhập")
                password = st.text_input(" Mật khẩu", type="password")
                phone = st.text_input(" Số điện thoại")
                is_paid = st.radio(" Có trả phí hay không?", ["Yes", "No"])
                if st.button(" Xác nhận đăng ký", use_container_width=True):
                    st.success(account.register(email, phone, is_paid == "Yes", password, username))

            elif st.session_state.action == "login":
                st.subheader("Đăng nhập")
                col_empty, col_form, col_empty2 = st.columns([1,2,1])
                with col_form:
                    username = st.text_input(" Tên đăng nhập")
                    password = st.text_input(" Mật khẩu", type="password")
                    if st.button(" Xác nhận đăng nhập", use_container_width=True):
                        st.success(account.login(username, password))
else:
    # Nếu đã đăng nhập
    try:
        data = pd.read_csv(r'app/database/acc.csv')
        # Lấy đúng dòng của user hiện tại
        user_row = data.loc[data['username'] == account.current_user]
        if not user_row.empty:
            is_paid_value = str(user_row.iloc[0]['is_paid']).strip().lower()
            if is_paid_value == "yes":
                pre()
            else:
                cla()
        else:
            st.error("Không tìm thấy thông tin người dùng trong file acc.csv")
    except Exception as e:
        st.error(f"Lỗi khi đọc file CSV: {e}")

    with st.sidebar:
        if st.button(" Đăng xuất", use_container_width=True):

            st.info(account.logout())



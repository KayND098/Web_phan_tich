import streamlit as st
from chart.chart import Gia_vang, Gia_dau, Gia_vang_tg, Chi_so_bien_dong, Ty_gia

def cla():
    """Hiển thị menu sidebar và nội dung chính"""
    if "selected_function" not in st.session_state:
        st.session_state.selected_function = None

    with st.sidebar.expander("≡ Menu", expanded=True):
        if st.button("Giá vàng", key="btn_vang"):
            st.session_state.selected_function = "Gia_vang"
        if st.button("Giá dầu", key="btn_dau"):
            st.session_state.selected_function = "Gia_dau"
        if st.button("Giá vàng TG", key="btn_vang_tg"):
            st.session_state.selected_function = "Gia_vang_tg"
        if st.button("Chỉ số biến động", key="btn_biendong"):
            st.session_state.selected_function = "Chi_so_bien_dong"
        if st.button("Tỷ giá USD/VND", key="btn_tygia"):
            st.session_state.selected_function = "Ty_gia"

    # Nội dung chính
    if st.session_state.selected_function == "Gia_vang":
        st.pyplot(Gia_vang())
    elif st.session_state.selected_function == "Gia_dau":
        st.pyplot(Gia_dau())
    elif st.session_state.selected_function == "Gia_vang_tg":
        st.pyplot(Gia_vang_tg())
    elif st.session_state.selected_function == "Chi_so_bien_dong":
        st.pyplot(Chi_so_bien_dong())
    elif st.session_state.selected_function == "Ty_gia":
        st.pyplot(Ty_gia())

from function.ket_luan import phan_tich_tuong_quan

def pre():
    """Hiển thị menu sidebar và nội dung chính"""
    if "selected_function" not in st.session_state:
        st.session_state.selected_function = None

    with st.sidebar.expander("≡ Menu", expanded=True):
        if st.button("Giá vàng", key="btn_vang"):
            st.session_state.selected_function = "Gia_vang"
        if st.button("Giá dầu", key="btn_dau"):
            st.session_state.selected_function = "Gia_dau"
        if st.button("Giá vàng TG", key="btn_vang_tg"):
            st.session_state.selected_function = "Gia_vang_tg"
        if st.button("Chỉ số biến động", key="btn_biendong"):
            st.session_state.selected_function = "Chi_so_bien_dong"
        if st.button("Tỷ giá USD/VND", key="btn_tygia"):
            st.session_state.selected_function = "Ty_gia"
        if st.button("Phân tích tương quan", key="btn_tuongquan"):   # thêm nút mới
            st.session_state.selected_function = "phan_tich_tuong_quan"

    # Nội dung chính
    if st.session_state.selected_function == "Gia_vang":
        st.pyplot(Gia_vang())
    elif st.session_state.selected_function == "Gia_dau":
        st.pyplot(Gia_dau())
    elif st.session_state.selected_function == "Gia_vang_tg":
        st.pyplot(Gia_vang_tg())
    elif st.session_state.selected_function == "Chi_so_bien_dong":
        st.pyplot(Chi_so_bien_dong())
    elif st.session_state.selected_function == "Ty_gia":
        st.pyplot(Ty_gia())
    elif st.session_state.selected_function == "phan_tich_tuong_quan":
        st.pyplot(phan_tich_tuong_quan())   # gọi hàm mới
    
import streamlit as st


def show():
    st.header("Свяжитесь с нами")

    with st.form("contact_form"):
        name = st.text_input("Имя")
        email = st.text_input("Email")
        message = st.text_area("Сообщение")
        submitted = st.form_submit_button("Отправить")

        if submitted:
            st.success(f"Спасибо, {name}! Ваше сообщение отправлено.")
            # Здесь может быть логика обработки данных
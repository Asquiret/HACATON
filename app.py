import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="ИИ-Ассистент",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🤖"
)

# Инициализация состояния сессии
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Функция изменения страницы
def change_page(page_name):
    st.session_state.current_page = page_name

# Создаем верхнюю панель навигации
empty_col, btn_col1, btn_col2, btn_col3, btn_col4 = st.columns([2, 1, 1, 1, 1])

with btn_col1:
    st.button("🏠 ИИ-агент", on_click=change_page, args=("Home",), use_container_width=True)
with btn_col2:
    st.button("🏠 Документация", on_click=change_page, args=("Home 2.0",), use_container_width=True)
with btn_col3:
    st.button("ℹ️ О проекте", on_click=change_page, args=("About",), use_container_width=True)
with btn_col4:
    st.button("📞 Контакты", on_click=change_page, args=("Contact",), use_container_width=True)

st.markdown("---")  # Горизонтальная разделительная линия

# Отображаем текущую страницу
if st.session_state.current_page == "Home":
    from list import Ai_page
    Ai_page.show()
elif st.session_state.current_page == "Home 2.0":
    from list import document_page
    document_page.show()
elif st.session_state.current_page == "About":
    from list import about_page
    about_page.show()
elif st.session_state.current_page == "Contact":
    from list import contact_page
    contact_page.show()
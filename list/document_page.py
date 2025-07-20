import streamlit as st
import time
import ask

LKEY = "sk-P_K5kEpuT9Suh3Ot5P1Evul2TjQ-Vme1aN8jefGUt54"
url = "http://localhost:7860/api/v1/run/9e8296ca-d3a3-46f4-9fbb-1705d2db32ac"

# Ссылки на скачивание документаций
def show():
    st.title("Документация")
    st.caption("ПОЛИТИКА ОБРАБОТКИ ПЕРСОНАЛЬНЫХ ДАННЫХ")
    st.download_button('privacypolicy.pdf', 'Sample text content', file_name='privacypolicy.pdf', mime='text/pdf')
    st.caption("ДИСКОВЫЕ МОДУЛИ РАСШИРЕНИЯ")
    st.download_button('YADRO_Modules_Datasheet.pdf', 'Sample text content', file_name='YADRO_Modules_Datasheet.pdf', mime='text/pdf')
    st.caption("ИНСТРУКЦИЯ ПО ВЗАИМОДЕЙСТВИЮ С СЕРВИСНОЙ СЛУЖБОЙ YADRO")
    st.download_button('YADRO_Service_Instruction_on_interaction_v_1_21.pdf', 'Sample text content', file_name='YADRO_Service_Instruction_on_interaction_v_1_21.pdf', mime='text/pdf')
    st.caption("YADRO СУПРИМ (Версия 1.5)")
    st.download_button('YADRO_TATLIN_UNIFIED_GEN2_Presentation_RUS.pdf', 'Sample text content', file_name='YADRO_TATLIN_UNIFIED_GEN2_Presentation_RUS.pdf', mime='text/pdf')
    st.caption("YADRO TATLIN.OBJECT")
    st.download_button('YADRO_TATLIN_FLEX_Presentation_RUS.pdf', 'Sample text content', file_name='YADRO_TATLIN_FLEX_Presentation_RUS.pdf', mime='text/pdf')
    st.caption("YADRO TATLIN.FLEX")
    st.download_button('YADRO_SUPREME_1.5_Whitepaper.pdf', 'Sample text content', file_name='YADRO_SUPREME_1.5_Whitepaper.pdf', mime='text/pdf')
    st.caption("YADRO TATLIN.UNIFIED GEN2")
    st.download_button('YADRO_TATLIN.OBJECT_DS_RUS.pdf', 'Sample text content', file_name='YADRO_TATLIN.OBJECT_DS_RUS.pdf', mime='text/pdf')

    # Инициализация истории чата в session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant",
            "content": "Привет! Я ваш ИИ-помощник. Чем могу помочь?",
            "avatar": "🤖"
        })

    # Отображение истории сообщений
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            st.markdown(message["content"])

    # Прием ввода пользователя
    if prompt := st.chat_input("Введите ваше сообщение..."):
        # Добавление сообщения пользователя в историю
        user_msg = {"role": "user", "content": prompt, "avatar": "👤"}
        answer = ask.ask_bot(user_msg["content"], url)
        st.session_state.messages.append(user_msg)

        # Отображение сообщения пользователя
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Имитация обработки запроса (заглушка для будущего ИИ)
        with st.chat_message("assistant", avatar="🤖"):
            message_placeholder = st.empty()
            full_response = ""

            # Имитация "печатания" ответа
            with st.spinner("Думаю..."):
                time.sleep(1)  # Имитация задержки обработки

                # Постепенная "печать" ответа
                for chunk in answer.split():
                    full_response += chunk + " "
                    time.sleep(0.1)
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)

        # Добавление ответа ассистента в историю
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "avatar": "🤖"
        })
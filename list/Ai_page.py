import streamlit as st
import time
import ask
import requests
import json

# API Configuration

LKEY = "sk-P_K5kEpuT9Suh3Ot5P1Evul2TjQ-Vme1aN8jefGUt54"
url = "http://localhost:7860/api/v1/run/5388527b-44bb-4755-bb85-d34adecae609"  # The complete API endpoint URL for this flow

def show():
    st.title("💬 Чат с ИИ-агентом")
    st.caption("Это демо-интерфейс для будущего ИИ-агента")
    
    # Инициализация истории чата в session state
    if "messages1" not in st.session_state:
        st.session_state.messages1 = []
        st.session_state.messages1.append({
            "role": "assistant", 
            "content": "Привет! Я ваш ИИ-помощник. Чем могу помочь?",
            "avatar": "🤖"
        })
    
    # Отображение истории сообщений
    for message in st.session_state.messages1:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            st.markdown(message["content"])
    
    # Прием ввода пользователя
    if prompt := st.chat_input("Введите ваше сообщение..."):
        # Добавление сообщения пользователя в историю
        user_msg = {"role": "user", "content": prompt, "avatar": "👤"}
        answer = ask.ask_bot(user_msg["content"], url)
        st.session_state.messages1.append(user_msg)

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
        st.session_state.messages1.append({
            "role": "assistant", 
            "content": answer,
            "avatar": "🤖"
        })
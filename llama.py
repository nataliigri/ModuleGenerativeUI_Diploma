import streamlit as st
import requests
import pandas as pd
import os
import json
from dotenv import load_dotenv
from render_screens import render_screen_st, render_main_screen, render_savings_goals_screen, render_statistics_screen

# ==== Завантаження API ключа ====
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

if not TOGETHER_API_KEY:
    st.error("Не знайдено TOGETHER_API_KEY у .env файлі.")
    st.stop()

# ==== Генерація UI JSON з LLaMA ====
def generate_ui_json(prompt):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta-llama/Llama-3-70b-chat-hf",
        "messages": [
            {
                "role": "system",
                "content": "Ти генератор JSON UI структури мобільного застосунків. "
                           
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
    }

    res = requests.post(url, headers=headers, json=payload)
    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]

# ==== Витяг валідного JSON ====
def extract_json_block(text):
    brace_count = 0
    json_started = False
    result = ""
    for char in text:
        if char == '{':
            brace_count += 1
            json_started = True
        if json_started:
            result += char
        if char == '}':
            brace_count -= 1
            if brace_count == 0:
                break
    if result:
        return result
    else:
        raise ValueError("Не знайдено валідного JSON.")


# ==== Інтерфейс Streamlit ====
st.set_page_config(page_title="🇺🇦 Генератор UI (LLaMA)", layout="centered")
st.title("🧠 Український Генератор UI (на базі LLaMA 3)")

default_prompt = (
    "Україномовний застосунок для фінансового менеджменту та трекінгу бюджету (до 10 екранів): "
    "онбординг, логін, головна сторінка з картками та балансом, історія транзакцій з фільтрами, категорії витрат, "
    "огляд бюджету по категоріях, цілі накопичення, форма додавання транзакції, сторінка профілю, статистика, налаштування."
)

prompt = st.text_area("📝 Опишіть застосунок:", value=default_prompt, height=200)

# ==== Кнопка генерації ====
if st.button("🚀 Згенерувати JSON"):
    with st.spinner("Генерація через LLaMA 3..."):
        try:
            raw_output = generate_ui_json(prompt)
            clean_json = extract_json_block(raw_output)
            data = json.loads(clean_json)

            st.success("✅ JSON згенеровано!")
            st.code(json.dumps(data, indent=2, ensure_ascii=False), language="json")
            st.session_state["ui_data"] = data

        except Exception as e:
            st.error(f"❌ Помилка: {e}")

# ==== Кнопка візуалізації ====
if "ui_data" in st.session_state:
    screens = st.session_state["ui_data"].get("screens", [])
    # Знайдемо потрібні екрани по id
    main_screen = next((s for s in screens if s["id"] == "main"), None)
    goals_screen = next((s for s in screens if s["id"] == "goals"), None)
    statistics_screen = next((s for s in screens if s["id"] == "statistics"), None)

    if st.button("📱 Показати основні екрани (головна, заощадження, статистика)"):
        if main_screen:
            render_main_screen(main_screen)
        if goals_screen:
            render_savings_goals_screen(goals_screen)
        if statistics_screen:
            render_statistics_screen(statistics_screen)


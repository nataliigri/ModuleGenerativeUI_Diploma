import streamlit as st
import pandas as pd

def render_screen_st(screen):
    st.subheader(f"📱 Екран: {screen.get('title', screen.get('id', 'Невідомий'))}")
    components = screen.get("components", [])

    for comp in components:
        ctype = comp.get("type")

        if ctype == "text":
            st.markdown(f"<p style='font-size:16px;'>{comp.get('text', '')}</p>", unsafe_allow_html=True)

        elif ctype == "image":
            st.image(comp.get("src"), use_column_width=True)

        elif ctype == "button":
            if st.button(comp.get("text", "Кнопка")):
                st.info(f"Натиснули кнопку: {comp.get('text')}")

        elif ctype == "input":
            label = comp.get("label", "")
            placeholder = comp.get("placeholder", "")
            if comp.get("secure"):
                st.text_input(label, placeholder=placeholder, type="password")
            else:
                st.text_input(label, placeholder=placeholder)

        elif ctype == "select":
            label = comp.get("label", "")
            options = [opt.get("label") for opt in comp.get("options", [])]
            st.selectbox(label, options)

        elif ctype == "list":
            items = comp.get("items", [])
            for item in items:
                title = item.get("title") or item.get("name") or "Елемент"
                value = item.get("value") or item.get("amount") or ""
                extra = ""
                if "progress" in item:
                    extra = f" (Прогрес: {item['progress']})"
                st.markdown(f"- **{title}**: {value}{extra}")

        elif ctype == "filter":
            options = [opt.get("label") for opt in comp.get("options", [])]
            st.selectbox("Фільтр", options)

        elif ctype == "card":
            title = comp.get("title", "")
            value = comp.get("value", "")
            st.markdown(f"""
                <div style="
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 12px 16px;
                    margin-bottom: 12px;
                    background-color: #f9f9f9;
                ">
                    <h4 style="margin: 0 0 6px 0;">{title}</h4>
                    <p style="font-size: 18px; font-weight: bold; margin: 0;">{value}</p>
                </div>
            """, unsafe_allow_html=True)

        elif ctype == "chart":
            data = comp.get("data", [])
            labels = []
            values = []
            for d in data:
                label = d.get("label") or d.get("category") or ""
                raw_val = d.get("value") or d.get("amount") or "0"
                val_str = str(raw_val).replace(" грн", "").replace(" ", "").replace("%", "")
                try:
                    val = float(val_str)
                except:
                    val = 0
                labels.append(label)
                values.append(val)

            df = pd.DataFrame({"Категорія": labels, "Значення": values})
            st.bar_chart(df.set_index("Категорія"))

        elif ctype == "switch":
            label = comp.get("label", "")
            value = comp.get("value", False)
            st.checkbox(label, value=value)

        else:
            st.warning(f"Невідомий компонент: {ctype}")

def render_main_screen(screen):
    st.subheader(f"📱 {screen.get('title', 'Головна')}")
    for comp in screen.get("components", []):
        if comp["type"] == "card":
            title = comp.get("title", "")
            value = comp.get("value", "")
            st.markdown(f"""
                <div style="
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 12px 16px;
                    margin-bottom: 12px;
                    background-color: #f9f9f9;
                ">
                    <h4 style="margin: 0 0 6px 0;">{title}</h4>
                    <p style="font-size: 18px; font-weight: bold; margin: 0;">{value}</p>
                </div>
            """, unsafe_allow_html=True)
        elif comp["type"] == "button":
            if st.button(comp.get("text", "Кнопка")):
                st.info(f"Натиснули: {comp.get('text')}")

def render_savings_goals_screen(screen):
    st.subheader(f"🎯 {screen.get('title', 'Цілі накопичення')}")
    for comp in screen.get("components", []):
        if comp["type"] == "list":
            items = comp.get("items", [])
            for item in items:
                name = item.get("name", "Ціль")
                amount = item.get("amount", "")
                progress = item.get("progress", "0%")
                st.markdown(f"- **{name}**: {amount} (Прогрес: {progress})")
        else:
            st.write(f"Невідомий компонент: {comp}")

def render_statistics_screen(screen):
    st.subheader(f"📊 {screen.get('title', 'Статистика')}")
    for comp in screen.get("components", []):
        if comp["type"] == "chart":
            data = comp.get("data", [])
            labels = []
            values = []
            for d in data:
                label = d.get("label") or ""
                raw_val = d.get("value", "0")

                # Очищаємо рядок, лишаємо лише цифри і крапку для float
                val_str = ''.join(ch for ch in raw_val if ch.isdigit() or ch == '.')

                try:
                    val = float(val_str) if val_str else 0
                except:
                    val = 0

                labels.append(label)
                values.append(val)

            df = pd.DataFrame({"Категорія": labels, "Значення": values})
            st.bar_chart(df.set_index("Категорія"))
        else:
            st.write(f"Невідомий компонент: {comp}")

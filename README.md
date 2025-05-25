# Генератор структури користувацького інтерфейсу на основі LLaMA 3 та Streamlit

Цей проєкт реалізує прототип генеративного модуля, що створює JSON-структуру інтерфейсу мобільного застосунку на основі текстового опису (prompt). Система використовує велику мовну модель LLaMA 3–70B-chat, доступ до якої надається через API-платформу Together AI. Для введення запитів, обробки результатів та візуалізації використано фреймворк Streamlit.

## Функціональні можливості
- Зчитування API-ключа з локального середовища
- Надсилання запиту до LLaMA 3 через Together API
- Отримання у відповідь JSON-структури інтерфейсу
- Інтерактивне відображення згенерованих екранів у Streamlit

## Структура проєкту

ModuleGenerativeUI_Diploma/
├── llama.py # Логіка запиту до моделі через API і Основна програма Streamlit
├── render_screens.py # Компоненти візуалізації інтерфейсу
├── .env # API-ключ для доступу до Together AI
├── requirements.txt # Список залежностей
├── README.md # Цей файл

## Вимоги

- Python 3.9+
- Інтернет-з’єднання
- Безкоштовний API-ключ Together AI

## Встановлення та запуск

1. Клонуйте репозиторій:

git clone https://github.com/your-username/ModuleGenerativeUI_Diploma.git
cd ModuleGenerativeUI_Diploma

2. Встановіть залежності:

pip install -r requirements.txt

3. Створіть файл `.env` і додайте свій API-ключ:

TOGETHER_API_KEY=sk-ваш_ключ_тут

Ключ можна отримати безкоштовно після реєстрації на сайті https://platform.together.xyz.

4. Запустіть застосунок:

streamlit run llama.py

## Формат prompt-запиту

Текстовий опис інтерфейсу, наприклад:

Ukrainian-language finance tracker app with onboarding, login, home with balance, transaction history, expense categories, budget, savings goals, add transaction, profile, and settings.

## Як це працює

1. Користувач вводить опис застосунку.
2. Запит надсилається до моделі LLaMA 3 через Together API.
3. Модель генерує структуру інтерфейсу у форматі JSON.
4. Streamlit обробляє JSON і відображає візуальне уявлення екранів.

## Автор

Розроблено в межах кваліфікаційної роботи  
Спеціальність 122 – Комп’ютерні науки  
2025  
[Грицишин Наталія Андріївна]

import streamlit as st
import streamlit.components.v1 as components

# Установим параметры страницы
st.set_page_config(
    page_title="Ситуационный Центр",
    page_icon="🏙️",
    layout="wide"
)

# HTML и CSS для более современного дизайна с градиентом, анимацией и выпадающими списками
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #83a4d4, #b6fbff);
            color: #202021;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .header {
            text-align: center;
            margin-bottom: 2rem;
            position: relative;
        }
        .header img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100px;
        }
        .header h1 {
            font-size: 3rem;
            color: #fff;
            margin: 0;
        }
        .header p {
            font-size: 1.25rem;
            color: #f0f0f0;
        }
        .nav {
            text-align: right;
            margin-bottom: 2rem;
        }
        .nav a {
            font-size: 1rem;
            color: #fff;
            text-decoration: none;
            margin-left: 1rem;
            padding: 0.5rem 1rem;
            background-color: #183F71;
            border-radius: 8px;
            transition: background-color 0.3s;
        }
        .nav a:hover {
            background-color: #142d5e;
        }
        .modules {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            margin-bottom: 2rem;
        }
        .module {
            flex: 1;
            margin: 0.5rem;
            padding: 1.5rem;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .module:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .module img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        .module h3 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
            color: #183F71;
        }
        .module p {
            font-size: 1rem;
            color: #6c757d;
        }
        .cases {
            text-align: center;
            margin-bottom: 2rem;
        }
        .cases h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #fff;
        }
        .case-buttons {
            display: flex;
            justify-content: center;
            gap: 1rem;
        }
        .case-button {
            background-color: #ECEBE5;
            border: none;
            padding: 1rem 2rem;
            font-size: 1rem;
            cursor: pointer;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s, transform 0.3s;
        }
        .case-button:hover {
            background-color: #dcdcdc;
            transform: translateY(-5px);
        }
        .traffic-management {
            background-color: #fff;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 2rem;
            text-align: center;
        }
        .traffic-management h3 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: #183F71;
        }
        .traffic-management p {
            font-size: 1rem;
            color: #6c757d;
        }
        .traffic-management .details {
            display: flex;
            justify-content: space-between;
            margin-top: 1rem;
            font-size: 1rem;
        }
        .details div {
            flex: 1;
            padding: 0 1rem;
        }
        .dropdown {
            position: relative;
            display: inline-block;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
            border-radius: 8px;
        }
        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
        }
        .dropdown-content a:hover {
            background-color: #f1f1f1;
        }
        .dropdown:hover .dropdown-content {
            display: block;
        }
        .feedback {
            background-color: #fff;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 2rem;
            text-align: center;
        }
        .feedback h3 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: #183F71;
        }
        .feedback form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        .feedback input, .feedback textarea {
            padding: 1rem;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 1rem;
        }
        .feedback button {
            background-color: #183F71;
            color: #fff;
            border: none;
            padding: 1rem;
            font-size: 1rem;
            cursor: pointer;
            border-radius: 8px;
            transition: background-color 0.3s, transform 0.3s;
        }
        .feedback button:hover {
            background-color: #142d5e;
            transform: translateY(-5px);
        }
    </style>
    <script src="https://unpkg.com/htmx.org@1.8.4"></script>
</head>
<body>
    <div class="container">
        <div class="nav">
            <a href="#">Главная</a>
            <a href="https://deep-analytics.smartalmaty.kz/" target="_blank">Аналитика</a>
            <a href="#feedback">Обратная связь</a>
        </div>
        <div class="header">
            <img src="https://via.placeholder.com/100" alt="Логотип">
            <h1>Ситуационный Центр</h1>
            <p>Современный цифровой хаб для эффективного управления городом и улучшения качества жизни его жителей.</p>
        </div>
        <div class="modules">
            <div class="module">
                <img src="https://via.placeholder.com/300x200" alt="Картинка 1">
                <h3>90</h3>
                <p>Информационных модулей</p>
            </div>
            <div class="module">
                <img src="https://via.placeholder.com/300x200" alt="Картинка 2">
                <h3>70</h3>
                <p>Аналитических модулей</p>
            </div>
            <div class="module">
                <img src="https://via.placeholder.com/300x200" alt="Картинка 3">
                <h3>70</h3>
                <p>Аналитических модулей</p>
            </div>
        </div>
        <div class="modules">
            <div class="module">
                <img src="https://via.placeholder.com/300x200" alt="Картинка 4">
                <h3>1</h3>
                <p>Сбор данных</p>
                <p>Получение информации из различных источников: датчики, камеры, социальные сети и др.</p>
            </div>
            <div class="module">
                <img src="https://via.placeholder.com/300x200" alt="Картинка 5">
                <h3>2</h3>
                <p>Обработка данных</p>
                <p>Очистка, структурирование и хранение данных в безопасном и эффективном хранилище.</p>
            </div>
            <div class="module">
                <img src="https://via.placeholder.com/300x200" alt="Картинка 6">
                <h3>3</h3>
                <p>Интеллектуальный анализ</p>
                <p>Применение продвинутых алгоритмов для выявления закономерностей и прогнозирования.</p>
            </div>
        </div>
        <div class="cases">
            <h2>Успешные кейсы:</h2>
            <div class="case-buttons">
                <div class="dropdown">
                    <button class="case-button">Управление трафиком</button>
                    <div class="dropdown-content">
                        <a href="#">Подробности</a>
                        <a href="#">Статистика</a>
                        <a href="#">Отчеты</a>
                    </div>
                </div>
                <div class="dropdown">
                    <button class="case-button">Профилактика преступности</button>
                    <div class="dropdown-content">
                        <a href="#">Подробности</a>
                        <a href="#">Статистика</a>
                        <a href="#">Отчеты</a>
                    </div>
                </div>
                <div class="dropdown">
                    <button class="case-button">Управление трафиком</button>
                    <div class="dropdown-content">
                        <a href="#">Подробности</a>
                        <a href="#">Статистика</a>
                        <a href="#">Отчеты</а>
                    </div>
                </div>
            </div>
            <div class="traffic-management">
                <h3>Управление трафиком</h3>
                <p>Получение информации из различных источников: датчики, камеры, социальные сети и др.</p>
                <div class="details">
                    <div>26 Всего компаний</div>
                    <div>2355 Транспортных ед.</div>
                    <div>186 Всего маршрутов</div>
                    <div>81 Общий % выходов</div>
                </div>
            </div>
        </div>
        <div class="feedback" id="feedback">
            <h3>Обратная связь</h3>
            <form>
                <input type="text" placeholder="Ваше имя" required>
                <input type="email" placeholder="Ваш email" required>
                <textarea placeholder="Ваше сообщение" required></textarea>
                <button type="submit">Отправить</button>
            </form>
        </div>
    </div>
</body>
</html>
"""

# Встраивание HTML и CSS в Streamlit с использованием streamlit.components.v1
components.html(html_code, height=2000)

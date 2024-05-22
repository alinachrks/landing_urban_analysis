import streamlit as st
import streamlit.components.v1 as components
import base64

# Установим параметры страницы
st.set_page_config(
    page_title="Аналитика для развития г. Алматы",
    page_icon="🏙️",
    layout="centered"
)

# Загрузим изображение для фона
with open("background.jpeg", "rb") as image_file:
    encoded_background = base64.b64encode(image_file.read()).decode()

page_element = """
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://i.ibb.co.com/MfCbbPM/DALL-E-2024-05-02-17-52-04-Wide-horizontal-image-for-an-app-cover-capturing-a-serene-summer-park-sce.jpg");
    background-size: cover;
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right: 2rem;
    background-image: url("https://cdn.iconscout.com/icon/free/png-256/hamburger-menu-462145.png");
    background-size: cover;
}
</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

# Определим изображения для кнопок и ссылки
buttons = {
    "Безопасность": {"image": "безопасность.png", "url": "https://deep-analytics.smartalmaty.kz/"},
    "Бизнес": {"image": "финансы.png", "url": "https://deep-analytics.smartalmaty.kz/"},
    "Благоустройство": {"image": "Благоустройство.png", "url": "https://deep-analytics.smartalmaty.kz/"},
    "Участки реновации": {"image": "Экономика.png", "url": "https://deep-analytics.smartalmaty.kz/"}
}

encoded_images = {}
for name, info in buttons.items():
    with open(info["image"], "rb") as image_file:
        encoded_images[name] = base64.b64encode(image_file.read()).decode()

# background: linear-gradient(to bottom, #83a4d4, #b6fbff), url('data:image/jpeg;base64,{encoded_background}') no-repeat center center fixed;
# background: url('data:image/png;base64,{encoded_background}') no-repeat center center fixed;


# HTML и CSS для главной страницы
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {{
            height: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }}
        body {{
            font-family: 'Arial', sans-serif;
            background-color: rgba(255, 255, 255, 0.5); /* Полупрозрачный фон */
            background-size: cover;
            color: #202021;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            text-align: center;
            background-color: transparent;
        }}
        .header {{
            margin-top: 2rem;
            margin-left: 16rem;
            background-color: rgba(81, 112, 98, 0.3); /* Полупрозрачный фон */
            padding: 1rem;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        .header h1 {{
            font-size: 3rem;
            color: #e3ffff;
            margin: 0;
        }}
        .header p {{
            font-size: 1.5rem;
            color: #e3ffff;
            margin: 0;
        }}
                .direction-buttons {{
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 2rem;
            position: absolute;
            bottom: 10%;
            left: 10%;
        }}
        .direction-button {{
            padding: 1rem;
            width: 150px;
            height: 150px;
            background-color: rgba(0, 162, 255, 0.5); /* Полупрозрачный голубой фон */
            border-radius: 50%; /* Круглые кнопки */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            margin-left: calc(10% * var(--step));
            text-decoration: none; /* Убираем подчеркивание */
        }}
        .direction-button img {{
            width: 60%;
            height: 60%;
        }}
        .direction-button span {{
            margin-top: 0.5rem;
            color: #fff;
            font-weight: bold;
        }}
        .direction-button:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }}
        .tooltip {{
            visibility: hidden;
            width: 150px;
            background-color: #183F71;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            top: 50%;
            left: 110%;
            margin-left: 10px;
            opacity: 0;
            transition: opacity 0.3s;
        }}
        .direction-button:hover .tooltip {{
            visibility: visible;
            opacity: 1;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>AlmatyAnalytics</h1>
        <p>Принятие решений на основе данных</p>
    </div>
    <div class="spacer"></div>
    <div class="direction-buttons">
"""

# Добавим кнопки в HTML код с применением каскадного шага для лестницы
step = 0
for name, info in buttons.items():
    html_code += f"""
                <a href="{info['url']}" class="direction-button" style="--step: {step}" title="{name}">
                    <img src="data:image/png;base64,{encoded_images[name]}" alt="{name}"/>
                    <span>{name}</span>
                    <div class="tooltip">{name}</div>
                </a>
    """
    step += 1

html_code += """
    </div>
</body>
</html>
"""

# Встраивание HTML и CSS в Streamlit с использованием streamlit.components.v1
components.html(html_code, height=1000)
import streamlit as st
import streamlit.components.v1 as components
import base64

# Установим параметры страницы
st.set_page_config(
    page_title="Аналитика для развития г. Алматы",
    page_icon="🏙️",
    layout="wide"
)

# Загрузим картинку для баннера
with open("banner.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

# Определим изображения для кнопок
images = {
    "Безопасность": "безопасность.png",
    "Бизнес": "финансы.png",
    "Благоустройство": "Благоустройство.png",
    "Досуг и развитие": "Экономика.png",
    "Недвижимость": "будущее.png",
    "Полицентричное развитие": "будущее.png",
    "Рабочие места": "бизнес.png",
    "Социальные объекты": "будущее.png",
    "Участки реновации": "Экономика.png"
}

encoded_images = {}
for name, file in images.items():
    with open(file, "rb") as image_file:
        encoded_images[name] = base64.b64encode(image_file.read()).decode()

# HTML и CSS для более современного дизайна с градиентом, анимацией и выпадающими списками
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #83a4d4, #b6fbff);
            color: #202021;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
        .header {{
            text-align: center;
            margin-bottom: 2rem;
        }}
        .header h1 {{
            font-size: 3rem;
            color: #fff;
            margin: 0;
        }}
        .header p {{
            font-size: 1.25rem;
            color: #f0f0f0;
        }}
        .banner {{
            background-image: url('data:image/png;base64,{encoded_image}');
            background-size: cover;
            background-position: center;
            height: 300px;
            border-radius: 8px;
            margin-bottom: 2rem;
        }}
        .directions {{
            text-align: center;
            margin-bottom: 2rem;
        }}
        .directions h2 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #fff;
        }}
        .direction-buttons {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1rem;
        }}
        .direction-button {{
            flex: 1;
            margin: 0.5rem;
            padding: 1.5rem;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            font-size: 1rem;
            font-weight: bold;
            text-decoration: none;
            color: #183F71;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .direction-button img {{
            width: 30px;
            height: 30px;
            margin-right: 10px;
        }}
        .direction-button:hover {{
            transform: translateY(-10px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }}
        .cases {{
            text-align: center;
            margin-bottom: 2rem;
        }}
        .cases h2 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #fff;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Аналитика для развития г. Алматы</h1>
            <p>Современный цифровой хаб для эффективного управления городом и улучшения качества жизни его жителей.</p>
        </div>
        <div class="banner"></div>
        <div class="directions">
            <h2>Направления</h2>
            <div class="direction-buttons">
"""

# Добавим кнопки в HTML код
for name, encoded_img in encoded_images.items():
    html_code += f"""
                <a href="/{name.lower()}" class="direction-button">
                    <img src="data:image/png;base64,{encoded_img}" alt="{name}"/>
                    {name}
                </a>
    """

html_code += """
            </div>
        </div>
        <div class="cases">
            <h2>Карта города</h2>
            <div id="map"></div>
        </div>
    </div>
</body>
</html>
"""

# Встраивание HTML и CSS в Streamlit с использованием streamlit.components.v1
components.html(html_code, height=1200)

# Встраивание карты из файла map.html
with open("map.html", 'r', encoding='utf-8') as file:
    map_html = file.read()
components.html(map_html, height=600)

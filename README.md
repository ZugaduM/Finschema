<img src="https://github.com/user-attachments/assets/ffec9f13-aecd-4251-844f-9cf673a46c8b" align="center" alt="Authentications">

![GitHub last commit](https://img.shields.io/github/last-commit/ZugaduM/Finschema)
![GitHub repo size](https://img.shields.io/github/repo-size/ZugaduM/Finschema)
![GitHub Repo stars](https://img.shields.io/github/stars/ZugaduM/Finschema)
![GitHub watchers](https://img.shields.io/github/watchers/ZugaduM/Finschema)
![GitHub followers](https://img.shields.io/github/followers/ZugaduM)
![Static Badge](https://img.shields.io/badge/e--mail%3A-zugadum%40gmail.com-blue?link=mailto:zugadum@gmail.com)

# Анализа и визуализации данных об акциях

## Оглавление
- [Введение](#intro)
- [Возможности](#poss)
- [Особенностии](#req)
- [Установка](#install)
- [Использование](#using)
- [Структура проекта](#struct)
- [Примеры тикеров](#example)
- [Приложение Пример графика](#add_1)

## <img src="https://github.com/user-attachments/assets/06f711e2-fc6b-4d17-9abc-17c5991280cf" width="64"> <a id='intro'>Введение</a>
Простое приложение на Python для получения, анализа и визуализации биржевых данных с использованием API Yahoo Finance.

## <img src="https://github.com/user-attachments/assets/3c4b8cb5-a99d-43d6-8cb1-d16b1d5cc958" width="64"> <a id='poss'>Возможности</a>
- Загрузка исторических данных акций по тикеру
- Расчет скользящей средней
- Вычисление средней цены закрытия
- Построение графиков цен акций
- Сохранение графиков в формате PNG

## <img src="https://github.com/user-attachments/assets/31f870e1-c478-469c-b3c4-57e4dbeeea98" width="64"> <a id='req'>Требования</a>
- Python 3.7+
- yfinance
- pandas 
- matplotlib
- numpy

## <img src="https://github.com/user-attachments/assets/23612cb6-7df8-44d6-a1a6-fdca47c3de19" width="64"> <a id='install'>Установка</a>

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/stock-analysis-tool.git
```
2. Установите зависимости:
```bash
pip install yfinance pandas matplotlib numpy
```

## <img src="https://github.com/user-attachments/assets/9a67c23d-2863-43e9-bc03-e87dc78e3358" width="64"> <a id='using'>Использование</a>
1. Запустите main.py:
```bash
python main.py
```
2. Следуйте инструкциям в консоли:
- Введите тикер акции (например, AAPL, GOOGL, MSFT)
- Укажите период для анализа (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
3. Программа:
- Загрузит данные
- Покажет среднюю цену закрытия
- Создаст график с ценой закрытия и скользящей средней
- Сохранит график в папку ./img/

## <img src="https://github.com/user-attachments/assets/e9f0fd8f-4f43-443b-93e2-842d7c4bbc07" width="64"> <a id='struct'>Структура проекта</a>
- main.py - основной файл программы
- data_download.py - функции для загрузки и обработки данных
- data_plotting.py - функции для создания графиков
- /img/ - папка для сохранения графиков

## <img src="https://github.com/user-attachments/assets/1875a045-180f-418e-a8c6-cca2b6795b4c" width="64"> <a id='example'>Примеры тикеров</a>
- AAPL - Apple Inc
- GOOGL - Alphabet Inc
- MSFT - Microsoft Corporation
- AMZN - Amazon.com Inc
- TSLA - Tesla Inc

## <a id='add_1'>Пример графика</a>
<img src="https://github.com/ZugaduM/Finschema/blob/main/.img/AAPL_1mo_stock_price_chart.png">


[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=zugadum&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
<h3 align="left">Я использую:</h3>
<p align="left"> <a href="https://www.arduino.cc/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/arduino-1.svg" alt="arduino" width="40" height="40"/> </a> <a href="https://www.blender.org/" target="_blank" rel="noreferrer"> <img src="https://download.blender.org/branding/community/blender_community_badge_white.svg" alt="blender" width="40" height="40"/> </a> <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.qt.io/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Qt_logo_2016.svg" alt="qt" width="40" height="40"/> </a> <a href="https://www.sketch.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sketchapp/sketchapp-icon.svg" alt="sketch" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> </p>

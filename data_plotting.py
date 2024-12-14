"""
Модуль для создания и сохранения графиков биржевых данных.

Обеспечивает визуализацию ценовых данных и технических индикаторов
с помощью библиотеки matplotlib.

Функции:
    create_and_save_plot(): Создает и сохраняет график цен акций
"""

import matplotlib.pyplot as plt
import pandas as pd
import os


def create_and_save_plot(data, ticker, period, filename=None):
    """
    Создает и сохраняет график цен акций.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций
        ticker (str): Тикер акции
        period (str): Период времени данных
        filename (str, optional): Путь для сохранения файла
    """

    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    # Создаем директорию img если её нет
    if not os.path.exists('img'):
        os.makedirs('img')

    # Формируем полный путь к файлу
    filepath = os.path.join('img', filename)

    plt.savefig(filepath)
    print(f"График сохранен в директории 'img' под именем {filename}")

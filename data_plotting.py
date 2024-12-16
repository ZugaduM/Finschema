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

    # Создаем подграфики: основной график и RSI
    fig, (ax1, ax2) = plt.subplots(2,
                                   1,
                                   figsize=(10, 8),
                                   gridspec_kw={
                                       'height_ratios': [2, 1],
                                       'hspace': 0.5
                                                }
                                   )

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            ax1.plot(dates, data['Close'].values, label='Close Price')
            ax1.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        ax1.plot(data['Date'], data['Close'], label='Close Price')
        ax1.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    ax1.set_title(f"{ticker} Цена акций с течением времени")
    ax1.set_xlabel("Дата")
    ax1.set_ylabel("Цена")
    ax1.legend()

    # График RSI
    ax2.plot(data.index, data['RSI'], label='RSI', color='purple')
    ax2.axhline(y=70, color='r', linestyle='--', alpha=0.5)
    ax2.axhline(y=30, color='g', linestyle='--', alpha=0.5)
    ax2.set_title("Индекс относительной силы (RSI)")
    ax2.set_ylabel("RSI")
    ax2.set_ylim(0, 100)
    ax2.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    # Создаем директорию img если её нет
    if not os.path.exists('img'):
        os.makedirs('img')

    # Формируем полный путь к файлу
    filepath = os.path.join('img', filename)

    plt.savefig(filepath)
    print(f"График сохранен в директории 'img' под именем {filename}")

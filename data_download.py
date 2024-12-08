"""
Модуль для загрузки и обработки биржевых данных.

Предоставляет функции для получения исторических данных акций
через API Yahoo Finance и их первичной обработки. (https://pypi.org/project/yfinance/)

Функции:
    fetch_stock_data(): Загружает исторические данные акций
    add_moving_average(): Добавляет скользящую среднюю к данным
    calculate_and_display_average_price(): Вычисляет и показывает среднюю цену
"""

import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    """
    Загружает исторические данные акций.

    Args:
        ticker (str): Тикер акции
        period (str): Период времени для загрузки данных

    Returns:
        pandas.DataFrame: DataFrame с историческими данными
    """

    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    Добавляет скользящую среднюю к данным.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций
        window_size (int): Размер окна для скользящей средней

    Returns:
        pandas.DataFrame: DataFrame с добавленной скользящей средней
    """

    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
    Вычисляет и выводит среднюю цену закрытия.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций
    """

    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия: {average_price:.2f}")
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
import os


def fetch_stock_data(ticker, period=None, start_date=None, end_date=None):
    """
    Загружает исторические данные акций за указанный период или диапазон дат.

    Args:
        ticker (str): Тикер акции
        period (str, optional): Предустановленный период
        start_date (str, optional): Дата начала в формате YYYY-MM-DD
        end_date (str, optional): Дата окончания в формате YYYY-MM-DD

    Returns:
        pandas.DataFrame: DataFrame с историческими данными
    """
    stock = yf.Ticker(ticker)
    if start_date and end_date:
        data = stock.history(interval='1d', start=start_date, end=end_date)
    else:
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


def notify_if_strong_fluctuations(data, threshold):
    """
    Анализирует колебания цены акций и уведомляет о сильных изменениях.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций
        threshold (float): Пороговое значение колебаний в процентах
    """
    max_price = data['Close'].max()
    min_price = data['Close'].min()

    # Вычисляем процент изменения
    price_change_percent = ((max_price - min_price) / min_price) * 100

    if price_change_percent > threshold:
        print(f"ВНИМАНИЕ: Обнаружено сильное колебание цены!")
        print(f"Максимальная цена: {max_price:.2f}")
        print(f"Минимальная цена: {min_price:.2f}")
        print(f"Процент изменения: {price_change_percent:.2f}%")


def export_data_to_csv(data, filename):
    """
    Экспортирует данные об акциях в CSV файл.

    Args:
        data (pandas.DataFrame): DataFrame с данными акций
        filename (str): Имя файла для сохранения данных
    """
    # Создаем директорию export если её нет
    if not os.path.exists('export'):
        os.makedirs('export')

    # Формируем полный путь к файлу
    filepath = os.path.join('export', filename)

    # Сохраняем данные в CSV
    data.to_csv(filepath)
    print(f"Данные успешно экспортированы в файл: {filepath}")

def calculate_rsi(data, period=14):
    """
    Рассчитывает индикатор RSI (Relative Strength Index).

    Args:
        data (pandas.DataFrame): DataFrame с данными акций
        period (int): Период для расчета RSI

    Returns:
        pandas.DataFrame: DataFrame с добавленным RSI
    """
    delta = data['Close'].diff()
    profit = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    waste  = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = profit / waste
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

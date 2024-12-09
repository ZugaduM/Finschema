"""
Основной модуль приложения для анализа биржевых данных.

Этот модуль обеспечивает пользовательский интерфейс и координирует работу
других модулей для загрузки данных, их анализа и визуализации.

Функции:
    main(): Основная функция, управляющая работой приложения
"""

from numpy.ma.extras import average

import data_download as dd
import data_plotting as dplt


def main():
    """
        Основная функция приложения.

        Обеспечивает взаимодействие с пользователем, получает входные данные
        и координирует работу остальных модулей для анализа и визуализации.
    """

    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = float(input("Введите пороговое значение колебаний в процентах (например, 5): "))

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Check for strong fluctuations
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Calculate and display average price
    dd.calculate_and_display_average_price(stock_data)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)


if __name__ == "__main__":
    main()

"""
Основной модуль приложения для анализа биржевых данных.

Этот модуль обеспечивает пользовательский интерфейс и координирует работу
других модулей для загрузки данных, их анализа и визуализации.

Функции:
    main(): Основная функция, управляющая работой приложения
"""

import data_download as dd
import data_plotting as dplt
from datetime import datetime
import matplotlib.pyplot as plt


def validate_date(date_string):
    """
    Проверяет корректность введенной даты.

    Args:
        date_string (str): Дата в формате YYYY-MM-DD

    Returns:
        bool: True если дата корректна, False если нет
    """
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def get_available_styles():
    """
    Получает список стилей графиков из matplotlib.

    Returns:
        list: Список из 10 доступных стилей
    """
    # Получаем все доступные стили
    all_styles = plt.style.available

    # Берем первые 10 стилей
    popular_styles = ['default'] + all_styles[:9]
    return popular_styles


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL "
          "(Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")

    use_custom_dates = input("Использовать конкретные даты? (да/нет): ").lower()

    if use_custom_dates == 'да':
        while True:
            start_date = input("Введите дату начала (YYYY-MM-DD): ")
            if validate_date(start_date):
                break
            print("Неверный формат даты. Используйте YYYY-MM-DD")

        while True:
            end_date = input("Введите дату окончания (YYYY-MM-DD): ")
            if validate_date(end_date):
                break
            print("Неверный формат даты. Используйте YYYY-MM-DD")

        stock_data = dd.fetch_stock_data(ticker, start_date=start_date, end_date=end_date)
        period = f"from_{start_date}_to_{end_date}"
    else:
        print("Общие периоды времени включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
        period = input("Введите период для данных (например, '1mo' для одного месяца): ")
        stock_data = dd.fetch_stock_data(ticker, period=period)

    threshold = float(input("Введите пороговое значение колебаний в процентах (например, 5): "))

    # Добавляем выбор стиля графика
    print("\nДоступные стили оформления графика:")
    styles = get_available_styles()
    for i, style in enumerate(styles, 1):
        print(f"{i}. {style}")

    style_choice = input("\nВыберите номер стиля (Enter для стиля по умолчанию): ")

    if style_choice.strip():
        selected_style = styles[int(style_choice) - 1]
    else:
        selected_style = 'default'

    # Добавление средней скользящей
    stock_data = dd.add_moving_average(stock_data)

    # Добавление RSI индикатора
    stock_data = dd.calculate_rsi(stock_data)

    # Проверка на сильные колебания
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Вычисление средней цены закрытия
    dd.calculate_and_display_average_price(stock_data)

    # Экспорт данных в CSV
    filename = f"{ticker}_{period}_stock_data.csv"
    dd.export_data_to_csv(stock_data, filename)

    # Отображение графиков
    dplt.create_and_save_plot(stock_data, ticker, period, style=selected_style)


if __name__ == "__main__":
    main()

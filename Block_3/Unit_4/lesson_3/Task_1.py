# Пропишите нужные импорты.
from datetime import datetime, timedelta, date


def get_weekday_name(weekday_number):
    if weekday_number == 0:
        return "понедельник"
    # Продолжите писать код.
    if weekday_number == 1:
        return "вторник"
    if weekday_number == 2:
        return "среда"
    if weekday_number == 3:
        return "четверг"
    if weekday_number == 4:
        return "пятница"
    if weekday_number == 5:
        return "суббота"
    if weekday_number == 6:
        return "воскресенье"


def get_day_after_tomorrow(date_string):
    # Напишите код функции.
    date_1 = datetime.strptime(date_string, "%Y-%m-%d")
    delta = timedelta(days=2)
    after_tomorrow = date_1 + delta
    print(
        f"Сегодня {date_string}, {get_weekday_name(date_1.weekday())}, а послезавтра будет {get_weekday_name(after_tomorrow.weekday())}"
    )


# Проверьте работу программы, можете подставить свои значения.
get_day_after_tomorrow("2024-01-01")
get_day_after_tomorrow("2024-01-02")
get_day_after_tomorrow("2024-01-03")
get_day_after_tomorrow("2024-01-04")
get_day_after_tomorrow("2024-01-05")
get_day_after_tomorrow("2024-01-06")

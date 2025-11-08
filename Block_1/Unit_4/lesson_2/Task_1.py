# Допишите нужные импорты.
from datetime import datetime, timedelta


def timedelta_days(datetime_str_1, datetime_str_2):
    # Напишите тело функции.
    datetime_1 = datetime.strptime(datetime_str_1, "%Y/%m/%d %H:%M:%S")
    datetime_2 = datetime.strptime(datetime_str_2, "%Y/%m/%d %H:%M:%S")
    datetime_1 = datetime.date(datetime_1)
    datetime_2 = datetime.date(datetime_2)
    delta = datetime_2 - datetime_1
    return int(timedelta.total_seconds(delta) // (24 * 60 * 60))


difference = timedelta_days("2019/05/10 00:00:00", "2019/10/04 00:00:00")

print("От начала посевной до начала сбора урожая прошло", difference, "дней.")

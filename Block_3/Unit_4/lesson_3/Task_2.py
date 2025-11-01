# Пропишите нужные импорты.
from datetime import datetime


# Напишите код функции, следуя плану из задания.
def get_results(leader_time, player_time):
    leader_time = datetime.strptime(leader_time, "%H:%M:%S")
    player_time = datetime.strptime(player_time, "%H:%M:%S")
    if leader_time == player_time:
        print(f"Вы пробежали за {datetime.time(leader_time)} и победили!")
    else:
        print(
            f"Вы пробежали за {datetime.time(player_time)} с отставанием от лидера {player_time-leader_time}"
        )


# Проверьте работу программы, можете подставить свои значения.
get_results("02:02:02", "02:02:02")
get_results("02:02:02", "03:04:05")

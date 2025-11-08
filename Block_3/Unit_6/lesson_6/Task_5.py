# Напишите функцию get_competition_data().
def get_competition_data(data):
    scores = {}
    for race in data:
        for team, score in race.items():
            if team not in scores:
                scores[team] = 0
            scores[team] += score

    team_winner = None
    win_score = 0
    for team, score in scores.items():
        if score > win_score:
            win_score = score
            team_winner = team

    list_ = scores.keys()
    list_ = sorted(list_)

    print(f"Команды, участвовавшие в гонке: {', '.join(list_)}")
    print(f"В гонке победила команда {team_winner} с результатом {win_score} баллов")


races_data = [
    {"Ferrari": 20, "Mercedes": 5, "Aston Martin": 10, "Williams": 15},
    {"Mercedes": 15, "Aston Martin": 20, "Ferrari": 10, "Williams": 0},
    {"Ferrari": 20, "Williams": 15, "Aston Martin": 10, "Mercedes": 5},
]


get_competition_data(races_data)

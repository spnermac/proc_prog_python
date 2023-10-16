list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
N = len(list_players)
first_team = list_players[0:int(N/2)]
second_team = list_players[int(N/2):N]
print(first_team)
print( second_team)

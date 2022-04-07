import csv

import random

with open('baixo_nivel_players.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    players_score = {}
    line_count = 0
    teams = {0: [], 1: [], 2: []}
    for row in csv_reader:
        players_score[row[0]] = row[1]
    players_score_ordered = sorted(
        players_score.items(), key=lambda x: x[1], reverse=True)

    # Pegamos sempre os 3 do topo e do fundo e alocamos aleatoriamente nos times até restar apenas 3 jogadores
    # na list para assim gerar times diferentes a cada vez que o programa é executado
    r = [0, 1, 2]
    while len(players_score_ordered) > 3:
        top_3 = sorted(players_score_ordered,
                       key=lambda x: x[1], reverse=True)[0:3]
        bottom_3 = sorted(players_score_ordered,
                          key=lambda x: x[1], reverse=False)[0:3]
        for i in r:
            try:
                top_random_player = random.choice(top_3)
                bottom_random_player = random.choice(bottom_3)
                teams[i].append(top_random_player)
                teams[i].append(bottom_random_player)
                players_score_ordered.remove(top_random_player)
                players_score_ordered.remove(bottom_random_player)
                top_3.remove(top_random_player)
                bottom_3.remove(bottom_random_player)
            except IndexError as e:
                break

    # Adiciona ao time aleatoriamente os ultimos 3 jogadores.
    for i in r:
        random_player = random.choice(players_score_ordered)
        teams[i].append(random_player)
        players_score_ordered.remove(random_player)

    for k, v in teams.items():
        print('----------------')
        print('team: ' + str(k+1))
        team_score = 0
        sortedTeam = sorted(v, key=lambda x: x[1], reverse=True)
        for p in sortedTeam:
            print('{:<20} {}'.format(p[0], p[1]))
            team_score += float(p[1])
        print('{:<20} {}'.format("Team Score:", str(team_score)))

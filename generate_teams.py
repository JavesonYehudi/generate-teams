import csv

with open('baixo_nivel_players.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    players_score = {}
    line_count = 0
    teams = {0: [], 1: [], 2: []}
    teams_score = {0:0.0, 1:0.0, 2:0.0}
    for row in csv_reader:
        players_score[row[0]] = row[1]
    players_score_ordered = sorted(players_score.items(), key=lambda x: x[1], reverse=True)

    r = [0,1,2]
    while len(players_score_ordered) != 0:
        for i in r:
            try:
                teams[i].append(players_score_ordered[0])
                teams_score[i] += float(players_score_ordered[0][1])
                players_score_ordered.remove(players_score_ordered[0])
            except IndexError as e:
                break
        r = [k for k,v in sorted(teams_score.items(), key=lambda item: item[1])]

    for k, v in teams.items():
        print('----------------')
        print('team: ' + str(k+1))
        team_score = 0
        for p in v:
            print('{:<20} {}'.format(p[0], p[1]))
            team_score += float(p[1])
        print('{:<20} {}'.format("Team Score:", str(team_score)))
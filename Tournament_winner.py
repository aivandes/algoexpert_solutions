def tournamentWinner(competitions, results):
    curr_winner = ""
    a = {}
    for competition, result in zip(competitions, results):
        if result==0:
            team = competition[1]
            if team not in a:
                a[team] = 3
                winner = [team, 3]
            else:
                a[team] += 3
                winner = [team, a[team]]
        else:
            team = competition[0]
            if team not in a:
                a[team] = 3
                winner = [team, 3]
            else:
                a[team] += 3
                winner = [team, a[team]]
        if curr_winner:
            if winner[1]>curr_winner[1]:
                curr_winner = winner[:]
        else:
            curr_winner = winner[:]
    return curr_winner[0]
def inputMatchData():
    """
    Collects match data from user input.

    Returns:
        list: A list of match data, where each entry is a list containing:
            - Team1 name (str)
            - Team2 name (str)
            - Team1 score (int)
            - Team2 score (int)
            - Goals scored by Team1 (list of str)
            - Goals scored by Team2 (list of str)
    """
    numMatches = int(input('Enter the number of matches: '))
    Datalis = []

    for i in range(numMatches):
        matchTeams = input('Enter the teams playing in the match (separated by comma): ')
        team1, team2 = matchTeams.split(',')

        finalS = input('Enter the final scores of the match (separated by space): ')
        team1S, team2S = finalS.split(' ')

        Datalis.append([team1, team2, int(team1S), int(team2S), [], []])

        for j in range(int(team1S)):
            Goal1 = input(f'Enter Goal {j + 1} for {team1}: ')
            Datalis[i][4].append(Goal1)

        for k in range(int(team2S)):
            Goal2 = input(f'Enter Goal {k + 1} for {team2}: ')
            Datalis[i][5].append(Goal2)

    return Datalis

# Test your function
'''matchData = inputMatchData()
print(matchData)'''







def predictMatchWinner(FirsT, secondT, teamData):
    """
    Predicts the winner of a match between two teams based on their historical win records.

    Args:
        FirsT (str): The name of the first team.
        secondT (str): The name of the second team.
        teamData (list): A list of team data, where each entry is a list containing:
            - Team name (str)
            - Opponent name (str)
            - Wins (tuple of (int, int)) representing (wins for Team1, wins for Team2)

    Returns:
        str: A string indicating the predicted winner and the reason for the prediction.
            Example: "Team1 (Team1 has more wins than Team2)"
            If the win records are equal, returns: "None (Team1 and Team2 have the same number of wins)"
    """
    for j in teamData:
        if FirsT.capitalize() and secondT.capitalize() in j:
            teamsD = j
    Team1 = teamsD[0]
    Team2 = teamsD[1]

    if teamsD[2][1] == teamsD[2][3]:
        winer = 'None'
    elif teamsD[2][1] > teamsD[2][3]:
        winer = Team1
        loser = Team2
    else:
        winer = Team2
        loser = Team1
    return winer #f'{winer} ({winer} has more wins than {loser})' if winer != 'None' else f'None ({Team1} and {Team2} have the same number of wins)'


team_data = [
    ['Qatar', 'India', ['wins', 10, 'losses', 5, 'draws', 3]],
    ['Jordan', 'Iraq', ['wins', 3, 'losses', 3, 'draws', 2]],
    ['Pakistan', 'China', ['wins', 6, 'losses', 8, 'draws', 4]]
]
'''
predicted_winner = predictMatchWinner('Qatar', 'India', team_data)
print(predicted_winner)
# Expected output: 'Qatar' (Qatar has more wins than India)

predicted_winner = predictMatchWinner('india', 'qatar', team_data)
print(predicted_winner)
# Expected output: 'Qatar' (Qatar has more wins than India)

predicted_winner = predictMatchWinner('Jordan', 'Iraq', team_data)
print(predicted_winner)
# Expected output: None (Jordan and Iraq have the same number of wins)

predicted_winner = predictMatchWinner('Pakistan', 'China', team_data)
print(predicted_winner)
# Expected output: 'China' (China has more wins than Pakistan)
'''

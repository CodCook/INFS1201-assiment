def calculateTeamPoints(Data):
    """
    Calculates the points for each team based on match data.

    Args:
        Data (list): A list of match data. Each match is represented as a tuple
                     (team1, team2, team1Sc, team2Sc).

    Returns:
        list: A list of lists, where each inner list contains the team name and
              their total points.
    """
    team_points = []
    
    for match in Data:
        team1, team2, team1Sc, team2Sc = match
        
        if team1Sc > team2Sc:
            team1Point = 3
            team2Point = 0
        elif team1Sc == team2Sc:
            team1Point = 1
            team2Point = 1
        else:
            team1Point = 0
            team2Point = 3
        
        # Update team1's points
        try:
            score_index = team_points.index(team1) + 1
            team_points[score_index] += team1Point
        except ValueError:
            team_points.append(team1)
            team_points.append(team1Point)
        
        # Update team2's points
        try:
            score_index = team_points.index(team2) + 1
            team_points[score_index] += team2Point
        except ValueError:
            team_points.append(team2)
            team_points.append(team2Point)
    
    final_list = []
    i = 0
    j = 2
    while j <= len(team_points):
        final_list.append(team_points[i:j])
        i += 2
        j += 2
        
    return final_list

# Test cases
matchData = [
    ['Qatar', 'Iraq', 3, 2],
    ['Jordan', 'Qatar', 1, 1],
    ['Jordan', 'Palestine', 1, 2]
]
'''
team_points = calculateTeamPoints(matchData)
print(team_points)  # Expected output: [['Qatar', 4], ['Iraq', 0], ['Jordan', 1], ['Palestine', 3]]
'''

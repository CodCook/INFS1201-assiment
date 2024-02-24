
def highestScoringTeam(Data):
    """
    Calculates the highest-scoring team based on match data.

    Args:
        Data (list): A list of tuples representing match data.
            Each tuple contains (team1, team2, team1Sc, team2Sc).

    Returns:
        tuple: A tuple containing the highest score and a list of team names.
            Example: (4, ['Qatar'])
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
        
        try:
            score_index = team_points.index(team1)+1
            team_points[score_index]+= team1Point
        except:
            team_points.append(team1)
            team_points.append(team1Sc)
        try:
            score_index = team_points.index(team2)+1
            team_points[score_index]+= team2Point
        except:
            team_points.append(team2)
            team_points.append(team2Sc)
    final_list = []
    i = 0
    j = 2
    while j<=len(team_points):
        final_list.append(team_points[i:j])
        i+=2
        j+=2
    
    top_points = final_list[0][1]
    newlist = []
    for point in final_list:
        if point[1]>=top_points:
            newlist.append(point)
            top_points = point[1]
    finallist = (newlist[0][1],[])
    for team in newlist:
        finallist[1].append(team[0])
        
    return finallist





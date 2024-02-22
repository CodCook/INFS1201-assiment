def calculateTeamPoints(Data):
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
        
        # Check if the team is already in the list
        team1Index = -1
        for i, team in enumerate(team_points):
            if team[0] == team1:
                team1Index = i
                break
        
        team2Index = -1
        for i, team in enumerate(team_points):
            if team[0] == team2:
                team2Index = i
                break
        
        # If the team is not in the list, append it
        if team1Index == -1:
            team_points.append([team1, team1Point])
        else:
            team_points[team1Index][1] += team1Point
        
        if team2Index == -1:
            team_points.append([team2, team2Point])
        else:
            team_points[team2Index][1] += team2Point
                    
    return team_points



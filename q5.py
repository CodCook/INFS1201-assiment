def topGoalScorers(goalData):
    '''this function return the top goal scorers'''
    length = len(goalData)
    team = 0
    player = 1
    goals = 2
    lst = []

    while goals < length:

        if goalData[goals] > goalData[goals + 3]:
            lst.append((goalData[team], goalData[player], goalData[goals]))
        else:
            lst.append((goalData[team], goalData[player + 3], goalData[goals + 3]))

        team += 6
        player += 6
        goals += 6

    top_team_score = lst[0][2]
    topScorers = []

    for j in range(len(lst)):
        if lst[j][2] >= top_team_score:
            topScorers.append(lst[j])
            top_team_score = lst[j][2]

    return topScorers



#Test cases
# Sample Run
goalData = ['Qatar', 'Hassan Al-Haydos', 3, 'Qatar', 'Akram Afif', 1, 'Iraq', 'Amir Al-Ammari', 2, 'Iraq', 'Hussein Ali', 1, 'Jordan', 'Mahmoud Al-Mardi', 2, 'Jordan', 'Musa Al-Taamari', 1, 'Palestine', 'Oday Dabbagh', 3, 'Palestine', 'Bader Nasser', 1]

print(topGoalScorers(goalData))
# Expected output: [('Qatar', 'Hassan Al-Haydos', 3), ('Palestine', 'Oday Dabbagh', 3)]

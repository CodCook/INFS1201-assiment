def checkMatchUpDistance(winT, persT):
    """
    Calculates the match-up distance between two strings and determines the prize.

    Args:
        winT (str): The winning ticket number.
        persT (str): The user's ticket number.

    Returns:
        tuple: A tuple containing:
            - int: The match-up distance (number of differing characters).
            - str: The winning ticket number.
            - str: The modified user's ticket number with differing characters replaced by '*'.
            - str: A message indicating the prize won based on the match-up distance.
    """
    if len(winT) != len(persT):
        return None

    distance = 0
    newtex = ''

    for i in range(len(persT)):
        if persT[i] != winT[i]:
            distance += 1
            newtex += persT[i]
        else:
            newtex += '*'

    if distance == 0:
        Price = 'Congratulations! You are the winner of the Grand Prize: A VIP PASS to enjoy the Qatar Asia Cups from the best seats in the stadium!'

    elif 1 <= distance <= 2:
        Price = 'Congratulations! You win a small prize: An exclusive Qatar Asia Cups-themed football jersey.'

    else:
        Price = 'Better luck next time!'

    return (distance, winT, newtex, f'Your ticket number has a match-up distance of {distance}! {Price}')




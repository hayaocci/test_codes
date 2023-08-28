goal_found = 0

while True:
    # word = int(input('Enter a number'))
    try:
        word = int(input('Enter a number'))
        if word == 0:
            goal_found = 1
    except:
        print('Error Try Again')
    
    if goal_found == 1:
        break


import random
menuSelect = 'init'
while menuSelect != '0':
    rolls = 0
    dice = list()
    print('Select the number of dice to roll between 1 and 6')
    print('0 - Quit')
    menuSelect = input('-> ')
    if menuSelect == '0':
        break
    elif int(menuSelect) > 6:
        continue
    else:
        totalDice = int(menuSelect)
        print('Select the dice type to roll')
        print('1 - D4')
        print('2 - D6')
        print('3 - D8')
        print('4 - D10')
        print('5 - D12')
        print('6 - D20')
        print('0 - Quit')
        menuSelect = input('-> ')
        if menuSelect == '0':
            break
        elif menuSelect == '1':
            while rolls < totalDice:
                dice.append(random.randint(1,4))
                rolls += 1
            print('your ' + str(totalDice) + ' D4 rolls:')
            print(dice)
        elif menuSelect == '2':
            while rolls < totalDice:
                dice.append(random.randint(1,6))
                rolls += 1
            print('your ' + str(totalDice) + ' D6 rolls:')
            print(dice)
        elif menuSelect == '3':
            while rolls < totalDice:
                dice.append(random.randint(1,8))
                rolls += 1
            print('your ' + str(totalDice) + ' D8 rolls:')
            print(dice)
        elif menuSelect == '4':
            while rolls < totalDice:
                dice.append(random.randint(1,10))
                rolls += 1
            print('your ' + str(totalDice) + ' D10 rolls:')
            print(dice)
        elif menuSelect == '5':
            while rolls < totalDice:
                dice.append(random.randint(1,12))
                rolls += 1
            print('your ' + str(totalDice) + ' D12 rolls:')
            print(dice)
        elif menuSelect == '6':
            while rolls < totalDice:
                dice.append(random.randint(1,20))
                rolls += 1
            print('your ' + str(totalDice) + ' D20 rolls:')
            print(dice)
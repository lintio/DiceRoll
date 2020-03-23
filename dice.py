import random, os
menuSelect = 1
totalDice = 1
diceType = 'D6'
dieMax = 6
os.system('cls' if os.name == 'nt' else 'clear')
while menuSelect != 'q':
    rolls = 0
    dice = list()
    print('Current settings -> ' + str(totalDice) + ' ' + diceType + ' Dice <-')
    print('1) Roll dice')
    print('2) Change Numebr of dice')
    print('3) Change Dice')
    print('q) To quit')
    menuSelect = input('-> ')
    if menuSelect == '0':
        break
    elif menuSelect == '1' or menuSelect == '':
        while rolls < totalDice:
            dice.append(random.randint(1, dieMax))
            rolls += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print('your rolls are: ')
        print(dice)
    elif menuSelect == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Select the number of dice to roll')
        print('Enter 0 to go back')
        menuSelect = input('-> ')
        if menuSelect == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            totalDice = int(menuSelect)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    elif menuSelect == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Select the dice type to roll')
        print('1 - D4')
        print('2 - D6')
        print('3 - D8')
        print('4 - D10')
        print('5 - D12')
        print('6 - D20')
        print('Enter 0 to go back')
        menuSelect = input('-> ')
        if menuSelect == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif menuSelect == '1':
            diceType = 'D4'
            dieMax = 4
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif menuSelect == '2':
            diceType = 'D6'
            dieMax = 6
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif menuSelect == '3':
            diceType = 'D8'
            dieMax = 8
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif menuSelect == '4':
            diceType = 'D10'
            dieMax = 10
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif menuSelect == '5':
            diceType = 'D12'
            dieMax = 12
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif menuSelect == '6':
            diceType = 'D20'
            dieMax = 20
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
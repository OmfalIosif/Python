import random

no100 = 0    #mia random metavliti mono k mono gia na trexei to while
play = input('1. Start Game \n2. Exit\n')
while no100 == 0:
    if play == '1':  
        mny = int(input('Enter the amount of money you want to play with: '))        #mny = lefta
        if mny > 0:
            while mny > 0:
                play = input('-----------------------------\n2. Play again \nExit the game\n')
                if play != '2':  
                    break
                else:
                    win = 0
                    pos = int(input('--------------------------------\nEnter bet amount: '))
                    a = random.randint(1, 9)
                    b = random.randint(1, 9)
                    c = random.randint(1, 9)
                    d = b - 1
                    e = c - 1
                    f = b + 1

                    print(a, b, c)
                    if a == b and b == c:
                        win = pos * 2
                        mny += win
                    elif a == b and b == c and c == 7:
                        win = pos * 5
                        mny += win
                    elif a == d and b == e and c == f:
                        win = pos * 0.5
                        mny += win
                    else:
                        win = 0
                        mny -= pos
                    
                    if win > 0:
                        print('You won: ', win)
                    else:
                        print('You lost!')
                    
                    print('Current balance: ', mny)
                
                if mny <= 0:
                    print('You are out of money!')
                    break
        elif mny <= 0:
            print('You have no money left.')
    else:
        break

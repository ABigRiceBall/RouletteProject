money = 1000
import random

def roulette(guess, bet):
    global money
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    wheel = random.randint(1, 36)
    if wheel in black:
        print('The ball landed on ' + str(wheel) + ' black.')
    elif wheel in red:
        print('The ball landed on ' + str(wheel) + ' red.')

    if guess == 'black' and wheel in black:
        money = money + bet
        print('Black! You won ' + str(bet) + ' dollars!')
    elif guess == 'red' and wheel in red:
        money = money + bet
        print('Red! You won ' + str(bet) + ' dollars!')
    elif guess == 'even' and wheel % 2 == 0:
        money = money + bet
        print('Even! You won ' + str(bet) + ' dollars!')
    elif guess == 'odd' and wheel % 2 == 1:
            money = money + bet
            print('Odd! You won ' + str(bet) + ' dollars!')
    elif guess == wheel:
        money = money + bet * 36
        print('Straight bet won! You win ' + str(bet * 36) + ' dollars!')
    elif guess != wheel:
        money = money - bet
        print('You lose ' + str(bet) + ' dollars.')
    else:
        print('You lose ' + str(bet) + ' dollars.')

roulette(1, 10)
print(money)
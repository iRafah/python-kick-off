import random


def checkNumberGuessed(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You are a genius!')
            return True
        else:
            print('Wrong guess. Try again...')
            print('-------------------------')
    else:
        print('Hey bozo, I said 1~10')
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Guess a number 1~10: '))
            if (checkNumberGuessed(guess, answer)):
                break
        except ValueError:
            print('Please enter a number')
            continue

# Error handling

while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('Please, enter a number')
    except ZeroDivisionError:
        print('Seriously? 0? Write your real age or get out of here')
    else:
        print('Thank you for proving your age!')
        break
    finally:
        print('I am done!')

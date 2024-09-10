# Error handling.

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please, enter number. Error => {err}')


print(sum('1', 2))

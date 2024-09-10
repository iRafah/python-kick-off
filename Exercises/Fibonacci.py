def fib(index):
    a = 0
    b = 1

    for i in range(index):
        yield a
        sum = a + b
        b = a
        a = sum


# for x in fib(200):
#     print(x)


a = 'Hello baby'

new = a.replace('Hello', 'Bye')
print(new)

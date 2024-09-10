# @see https://docs.python.org/3/py-modindex.html
import random

print(random.random())

print(random.randint(1, 50))

print(random.choice([1, 2, 3, 4, 5]))

my_list = [2, 10, 58, 100, 655, 12]
random.shuffle(my_list)
print(my_list)

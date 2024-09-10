# list, set, dictionary

# list = []
# set = {}
import random
import sys
from dbm import dumb


my_list = {char for char in 'Rafael'}

your_list = [num for num in range(0, 100)]

his_list = [num**2 for num in range(5, 10)]



her_list = [num**2 for num in range(5, 10)
            if num % 2 == 0]

# print(my_list)
# print(your_list)
# print(his_list)
# print(her_list)

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}
# print(my_dict)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([item for item in some_list if some_list.count(
    item) > 1]))

print(duplicates)

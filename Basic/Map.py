from functools import reduce

# map, filter, zip and reduce.


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0

# reduce


def accumulator(acc, item):
    return acc + item


items = [1, 2, 5, 8]
more_items = [41, 20, 4]

# Map
print(list(map(lambda item: item*2, items)))

# Filter
print(list(filter(only_odd, items)))

# Filter with lambda
print(list(filter(lambda item: item % 2 != 0, items)))

# Zip
print(list(zip(items, more_items)))

# Reduce
print(reduce(accumulator, items, 0))

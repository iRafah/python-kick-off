# Pure functions have two rules
# 1 - Given the same input, it should result in the same output everytime.
# 2 - They should not interact with the outside world (scope)

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)

    return new_list


print(multiply_by2([1, 2, 3]))

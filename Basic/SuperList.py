from ast import List

# Extends the list class.


class SuperList(list):
    # Override len function.
    def __len__(self):
        return 1000


super_list = SuperList()

print(len(super_list))

# Append comes from the list class.
super_list.append(5)
print(super_list[0])

# list > Superlist
print(issubclass(SuperList, list))

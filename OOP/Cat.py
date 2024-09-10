class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


yellow_cat = Cat('Meow', 2)
blue_cat = Cat('Sky', 8)
brown_cat = Cat('Brownie', 9)


def oldest_cat(*cats):
    list_ages = []
    for cat in cats:
        list_ages.append(cat.age)

    max_age = max(list_ages)

    for cat in cats:
        if cat.age == max_age:
            return cat


the_oldest_cat = oldest_cat(yellow_cat, blue_cat, brown_cat)
print(the_oldest_cat.name, the_oldest_cat.age)

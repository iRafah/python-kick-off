class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    # Modify the Dunder method.
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 6

    def __call__(self):
        return ('Yes??')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('blue', 2)

print(action_figure.__str__())
print(len(action_figure))

print(action_figure['has_pets'])

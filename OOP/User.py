class User():

    def sign_in(self):
        print('Logged in')

# Extends User


class Wizard(User):
    def __init__(self, name, power):
        User.__init__(self)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

# Extends User


class Archer(User):
    def __init__(self, name, number_arrows):
        # super().__init__(email)
        self.name = name
        self.arrows = number_arrows

    def attack(self):
        print(f'Attacking with arrows: Arrows left -> {self.arrows}')

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('Ran really fast')

# Multiple inheritance.


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)
    pass


wizard1 = Wizard('Merlin', 250)
archer1 = Archer('Legolas', 25)
hb1 = HybridBorg('Robot', 12, 14)

print(hb1.attack())

# wizard1.attack()
# archer.attack()
# print(isinstance(archer, User))

# Polymorphism


def player_attack(character):
    character.attack()


# player_attack(wizard1)
# player_attack(archer)

# print(wizard1.email)
# print(archer1.email)

# introspection
# print(dir(wizard1))

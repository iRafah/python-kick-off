# OOP
class PlayerCharacter:
    # Class object attribute
    membership = True

    # This is the constructor.
    def __init__(self, name='Robot', age=1000):
        if (age > 18):
            self._name = name  # attributes
            self._age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'My name is {self._name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_more_things(num3, num4):
        return num3 - num4


player1 = PlayerCharacter('Wraith')
player2 = PlayerCharacter('Gibão', 19)
player2.attack = 10

# help(player1)

print(player1.adding_things(2, 6))
# print(player2.shout())
# print(player2.attack)

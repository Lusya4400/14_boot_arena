
class Person:

    def __init__(self, name, hp = 10, base_attak = 1, base_protection = 0.2):
        self.name = name
        self.hp = hp
        self.base_attak = base_attak
        self.base_protection = base_protection

    def __str__(self):
        return f'{self.__class__.__name__}, {self.name}, уровкнь жизни: {self.hp}, атака: {self.base_attak}, процент защиты: {self.base_protection}.'


class Paladin(Person):

    def __init__(self, name):
        super().__init__(name)
        self.hp *= 2
        self.base_protection *= 2


class Warrior(Person):

    def __init__(self, name):
        super().__init__(name)
        self.base_attak *= 2

pers1 = Paladin('Gorr')
pers2 = Warrior('Bishop')

print(pers1)
print(pers2)

class Thing:
    """Класс вещь для усиления персонажей."""
    def __init__(self):
        self.name
        self.protection
        self.attack
        self.life


brone_protection = Thing(name='Brone_protection',
                         protection=0.1, attack=0, life=1)
magic_ring = Thing(name='Magic_ring', protection=0.04,
                   attack=2, life=0)
invisible_coat = Thing(name='Invisible_coat', protection=0.1,
                       attack=0, life=1)
gun = Thing(name='gun', protection=0, attack=1, life=0)
laser_automat = Thing(name='laser_automat', protection=0.01,
                      attack=2, life=0)
magic_helmet = Thing(name='Magic_helmet', protection=0.08,
                     attack=0, life=1)
shining_bomb = Thing(name='shining_bomb', protection=0.01,
                     attack=3, life=0)


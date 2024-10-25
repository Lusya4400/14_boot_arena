from random import choice, randint


class Thing:
    """Класс вещь для усиления персонажей."""
    def __init__(self, name, protection, attack, life):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.life = life

    def __str__(self):
        return self.name


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

things = (brone_protection, magic_ring, invisible_coat, gun,
          laser_automat, magic_helmet, shining_bomb)


def make_things():
    things_random = []
    for _ in range(1, randint(2, 5)):
        thing = choice(things)
        things_random.append(thing)
    return things_random


class Person:

    def __init__(self, name, hp = 10, base_attak = 1, base_protection = 0.2):
        self.name = name
        self.hp = hp
        self.base_attak = base_attak
        self.base_protection = base_protection

    def get_hp(self, attack):
        demage = round(attack - attack * self.base_protection, 0)
        self.hp -= demage
        return demage


    def __str__(self):
        return f'{self.name} уровень жизни: {self.hp}'


    def set_things(self, things):
        for thing in things:
            self.hp += thing.life
            self.base_attak += thing.attack
            self.base_protection += thing.protection


class Paladin(Person):

    def __init__(self, name):
        super().__init__(name)
        self.hp *= 2
        self.base_protection *= 2


class Warrior(Person):

    def __init__(self, name):
        super().__init__(name)
        self.base_attak *= 2

list_pers = []
pers1 = Paladin('Gorr')
pers1.set_things(make_things())
pers2 = Warrior('Bishop')
pers2.set_things(make_things())
pers3 = Warrior('Fork')
pers3.set_things(make_things())
pers4 = Warrior('Snake')
pers4.set_things(make_things())
pers5 = Paladin('Elsa')
pers5.set_things(make_things())
list_pers.append(pers1)
list_pers.append(pers2)
list_pers.append(pers3)
list_pers.append(pers4)
list_pers.append(pers5)

while len(list_pers) > 1:
    pers_attack = choice(list_pers)
    list_pers.remove(pers_attack)
    pers_protect = choice(list_pers)
    list_pers.append(pers_attack)
    dem = pers_protect.get_hp(pers_attack.base_attak)
    print(f'{pers_attack} наносит удар на {dem} урона по {pers_protect}.')
    if pers_protect.hp <= 0:
        print(f'{pers_protect} убит')
        list_pers.remove(pers_protect)

print(f'Победил {list_pers[0]}')

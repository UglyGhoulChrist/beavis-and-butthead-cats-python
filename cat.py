# -*- coding: utf-8 -*-
from termcolor import cprint
from random import randint
import house


class Cat:

    def __init__(self, name):
        self.cat_name = name
        self.cat_fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.cat_name, self.cat_fullness)

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} пришёл с помойки'.format(self.cat_name), color='cyan')

    # Кот ест - сытость увеличивается на 20,
    # кошачья еда в доме уменьшается на 10.
    def cat_eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.cat_name), color='yellow')
            self.cat_fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.cat_name), color='red')

    # Кот спит - сытость уменьшается на 10
    def cat_sleep(self):
        cprint('{} спит'.format(self.cat_name), color='yellow')
        self.cat_fullness -= 10

    # Кот дерет обои - сытость уменьшается на 10,
    # степень грязи в доме увеличивается на 5
    def cat_wallpaper(self):
        cprint('{} дерет обои'.format(self.cat_name), color='yellow')
        self.cat_fullness -= 10
        house.House.dirt()

    def cat_act(self):
        if self.cat_fullness <= 0:
            cprint('{} умер...'.format(self.cat_name), color='red')
            return
        cat_dice = randint(1, 3)
        if self.cat_fullness < 20:
            self.cat_eat()
        elif cat_dice == 1:
            self.cat_eat()
        elif cat_dice == 2:            self.cat_sleep()
        elif cat_dice == 3:
            self.cat_wallpaper()
        else:
            print("Что-то пошло не так...")

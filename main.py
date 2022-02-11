# -*- coding: utf-8 -*-
"""
Симулятор дома. В доме живут люди и коты.
Люди могут работать, отдыхать и т.д.
Коты могут есть, спать и т.д.
Нужно прожить 365 дней.
"""
__author__ = "UglyGhoulChrist"
__version__ = "0.0.1"

from random import randint
from termcolor import cprint


class House:
    """
    Класс Дом. В нём есть деньги на тумбочке, еда в холодильнике. Дом характеризуется чистотой.
    """

    def __init__(self):
        self.food = 50
        self.cat_food = 50
        self.money = 100
        self.dirt = 0

    def __str__(self):
        return 'В холодильнике еды для человека осталось {}, еды для кота осталось {},' \
               ' на тумбочке денег осталось {}, степень загрязненности дома {}.' \
               ''.format(self.food, self.cat_food, self.money, self.dirt)

    def dirt(self):
        self.dirt += 10

    def clean(self):
        self.dirt -= 100


class Man:
    """
    Класс человек.Он может есть, работать, играть, убираться в доме, ходить в магазин.
    У человека есть степень сытости, если сытость < 0 единиц, человек умирает.
    """

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        # Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 100
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            if self.house.food <= 10:
                self.house.money -= 50
                self.house.food += 50
            elif self.house.cat_food <= 10:
                self.house.money -= 50
                self.house.cat_food += 50
            else:
                print("Что-то пошло не так")
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом'.format(self.name), color='cyan')

    def clear_house(self):
        self.fullness -= 20
        House.clean(self=sweet_home)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 20 or self.house.cat_food < 20:
            self.shopping()
        elif self.house.money < 100:
            self.work()
        elif self.house.dirt >= 100:
            self.house.clean()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class Cat:
    """
    Класс кот. У кота есть аттрибуты - сытость и дом (в котором он живет).
    Кот живет с человеком в доме.
    Для кота дом характеризируется - миской для еды и грязью.
    Изначально в доме нет грязи.
    """

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

    def cat_eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.cat_name), color='yellow')
            self.cat_fullness += 10
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.cat_name), color='red')

    def cat_sleep(self):
        cprint('{} спит'.format(self.cat_name), color='yellow')
        self.cat_fullness -= 10

    def cat_wallpaper(self):
        cprint('{} дерет обои'.format(self.cat_name), color='red')
        self.cat_fullness -= 10
        House.dirt(self=sweet_home)

    def cat_act(self):
        if self.cat_fullness <= 0:
            cprint('{} умер...'.format(self.cat_name), color='red')
            return
        cat_dice = randint(1, 3)
        if self.cat_fullness < 20:
            self.cat_eat()
        elif cat_dice == 1:
            self.cat_eat()
        elif cat_dice == 2:
            self.cat_sleep()
        elif cat_dice == 3:
            self.cat_wallpaper()
        else:
            print("Что-то пошло не так...")


# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
people = [
    Man(name='Бивис'),
    Man(name='Батхед'),
]

# Создадим двух котов, живущих в одном доме с Бивисом и Батхедом.
cats = [
    Cat(name='Барсик'),
    Cat(name='Рыжик'),
]

if __name__ == '__main__':
    sweet_home = House()
    for man in people:
        man.go_to_the_house(house=sweet_home)
    for cat in cats:
        cat.go_to_the_house(house=sweet_home)

    for day in range(1, 366):
        print('================ день {} =================='.format(day))
        for man in people:
            man.act()
        for cat in cats:
            cat.cat_act()
        print('--- в конце дня ---')
        for man in people:
            print(man)
        for cat in cats:
            print(cat)
        print(sweet_home)

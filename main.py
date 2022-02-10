# -*- coding: utf-8 -*-
from random import randint

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Человеку и коту надо вместе прожить 365 дней.

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class House:

    def __init__(self):
        self.food = 50  # Еда для человека
        self.cat_food = 50  # Еда для кота
        self.money = 100  # Деньги
        self.dirt = 0  # Степень загрязненности дома

    def __str__(self):
        return 'В доме еды для человека осталось {}, еды для кота осталось {},' \
               ' денег осталось {}, степень загрязненности {}.' \
               ''.format(self.food, self.cat_food, self.money, self.dirt)

    def dirt(self):
        self.dirt += 10

    def clean(self):
        self.dirt -= 100


class Man:

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

    #   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
    def clear_house(self):
        self.fullness -= 20
        House.clean(self=my_sweet_home)

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

        # Доработать класс человека, добавив методы
        # подобрать кота - у кота появляется дом.


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
            self.cat_fullness += 10
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
        cprint('{} дерет обои'.format(self.cat_name), color='red')
        self.cat_fullness -= 10
        House.dirt(self=my_sweet_home)

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


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
]

cats = [
    Cat(name='Кот Белка'),
    Cat(name='Кот Стрелка')
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for cat in cats:
    cat.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()

    for cat in cats:
        cat.cat_act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.

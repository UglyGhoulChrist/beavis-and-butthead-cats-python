# -*- coding: utf-8 -*-


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
        self.dirt += 5

    def clean(self):
        self.dirt -= 100

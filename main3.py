# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint, choice


# Создать модель жизни небольшой семьи.
#
# Все они живут в одном доме, дом характеризуется
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:  # Все они живут в одном доме, дом характеризуется:

    def __init__(self, name):
        self.name = name
        self.many = 100  # денег в тумбочке. + 150 муж после работы.
        self.food_human = 50  # еды в холодильнике для людей.
        self.food_cat = 30  # еды для кота.
        self.dirt = 0  # % кол-во грязи.
        self.total_food_human = 0
        self.total_food_cat = 0
        self.total_many = 0
        self.total_coat = 0

    def __str__(self):
        return f'Я - {self.name}, денег в тумбочке {self.many} рублей, еды в холодильнике {self.food_human}, еды для кота' \
               f' {self.food_cat}, грязи в доме {self.dirt}%.'


class Resident:
    def __init__(self, name):
        self.my_house = house
        self.name = name  # имя.
        self.satiety = 30  # % степень сытости.
        self.happiness = 100  # % степень счастья.

    def eat(self):
        cube = randint(10, 30)
        if house.food_human < cube:
            cprint('Что-то кушать хочется, а нечего...', "red")
        else:
            house.food_human -= cube
            self.satiety += cube
            cprint(f"{self.name} поел.")

    def play(self):  # играть, разные жители играют по разному.
        self.satiety -= 10
        self.happiness += 20
        if self.happiness >= 100:
            self.happiness = 100
        cprint("{} играл целый день.".format(self.name), 'cyan')

    def inspect(self):
        if self.satiety >= 100:
            self.satiety = 100
        if self.happiness >= 100:
            self.happiness = 100

    def __str__(self):
        return f'Я - {self.name}, степень сытости {self.satiety}% , степень счастья {self.happiness}%.'


class Male(Resident):  # Муж

    def __init__(self, name):
        super().__init__(name)
        self.list_action = [self.eat, self.work, self.play]

    def __str__(self):
        return super().__str__()

    def inspect(self):
        super().inspect()

        if house.dirt >= 80:  # Если в доме грязи больше 80 - у людей падает степень счастья каждый день на 10 пунктов,
            self.happiness -= 10
        if self.satiety <= 10:
            self.eat()
            return True
        elif self.happiness <= 20:
            self.play()
            return True
        elif house.many <= 100:
            self.work()
            return True
        elif self.satiety >= 90:
            self.play()
            return True
        else:
            return False

    def eat(self):  # есть, кушают взрослые максимум по 10 единиц еды, степень сытости растет на 10 за 10 еды.
        super().eat()

    def work(self):  # ходить на работу, деньги в тумбочку добавляет муж, после работы - 150 единиц за раз,
        # приводит к уменьшению степени сытости на 10 пунктов
        house.many += 150
        house.total_many += 150
        self.satiety -= 10
        cprint("{} сходил на работу.".format(self.name), 'cyan')

    def play(self):  # играть в WoT, приводит к уменьшению степени сытости на 10 пунктов
        self.satiety -= 10
        self.happiness += 20  # Степень счастья растет от игры в WoT (на 20)
        cprint("{} играл в WoT целый день.".format(self.name), 'cyan')

    def act(self):
        action = choice(self.list_action)
        action()


class Female(Resident):  # Жена

    def __init__(self, name):
        super().__init__(name)
        self.list_action = [self.eat, self.shopping, self.buy_fur_coat, self.clean_house]

    def __str__(self):
        return super().__str__()

    def inspect(self):
        super().inspect()

        if house.dirt >= 80:  # Если в доме грязи больше 80 - у людей падает степень счастья каждый день на 10 пунктов,
            self.happiness -= 10
        if self.satiety <= 10:
            self.eat()
            return True
        elif self.happiness <= 20:
            self.buy_fur_coat()
            return True
        elif house.food_human <= 50 or house.food_cat <= 30:
            self.shopping()
            return True
        elif house.dirt >= 80:
            self.clean_house()
            return True
        else:
            return False

    def eat(self):  # есть, кушают взрослые максимум по 10 единиц еды, степень сытости растет на 10 за 10 еды.
        super().eat()

    def shopping(self):  # покупать продукты, еда стоит 100 денег 100 единиц еды,
        # приводит к уменьшению степени сытости на 10 пунктов

        if house.food_human >= 100:
            cprint("{} пошла в магазин и вспомнила, что холодильник то не резиновый...".format(self.name), "green")
        elif house.many <= 100:
            cprint("{} надумала купить еды, но денег маловато...".format(self.name), "red")
        else:
            house.many -= 100
            house.food_human += 100
            house.total_food_human += 100
            self.satiety -= 10
            cprint("{} купила еды.".format(self.name), "blue")

        if house.food_cat >= 100:
            cprint("У кота еды полно...", "green")
        elif house.many <= 50:
            cprint("{} надумала купить еды коту, но денег маловато...".format(self.name),
                   "red")
        else:
            house.many -= 50
            house.food_cat += 50
            house.total_food_cat += 50
            cprint("{} купила еды для кота.".format(self.name), "blue")

    def buy_fur_coat(self):  # покупать шубу, стоит 350 единиц, приводит к уменьшению степени сытости на 10 пунктов
        if house.many <= 500:
            cprint("{} надумала купить себе шубу, но денег маловато...".format(self.name), "magenta")
        else:
            house.many -= 350
            house.total_coat += 1
            self.satiety -= 10
            self.happiness += 60  # Степень счастья растет от покупки шубы на 60
            cprint("{} купила себе шубу.".format(self.name), "magenta")

    def clean_house(self):  # убираться в доме, приводит к уменьшению степени сытости на 10 пунктов
        if house.dirt <= 50:
            cprint("{} надумала убраться...но дома чисто.".format(self.name), "magenta")
        else:
            house.dirt = 0
            self.satiety -= 10
            cprint("{} убралась в доме.".format(self.name), "magenta")

    def act(self):
        action = choice(self.list_action)
        action()


class Cat(Resident):
    def __init__(self, name):
        super().__init__(name)
        self.list_action = [self.eat, self.sleep_cat, self.soil]

    def eat(self):  # есть, кушают коты максимум по 10 единиц еды, степень сытости растет на 20 за 10 еды.
        cube = randint(1, 10)
        if house.food_cat >= cube:
            house.food_cat -= cube
            self.satiety += 2 * cube
            cprint(f"{self.name} поел.")
        else:
            cprint('Что-то кушать хочется, а нечего...', "red")

    def sleep_cat(self):
        # приводит к уменьшению степени сытости на 10 пунктов
        self.satiety -= 10
        cprint("{} спал целый день.".format(self.name), 'cyan')

    def soil(self):
        # приводит к уменьшению степени сытости на 10 пунктов
        self.satiety -= 10
        house.dirt += 10
        cprint("{} драл обои целый день.".format(self.name), 'cyan')

    def inspect(self):
        if self.satiety >= 100:
            self.satiety = 100
        if self.satiety <= 10:
            self.eat()
            return True
        else:
            return False

    def act(self):
        action = choice(self.list_action)
        action()

    def __str__(self):
        return 'Я - {}, степень сытости {}%.'.format(self.name, self.satiety)


cprint('================== Начало ==================', color='yellow')
house = House("Семейный дом")
cprint(house, color="green")

residents = [Female(name="Beavis"),
             Male(name="Butthead"),
             Cat(name="Кот Васька"),
             Cat(name="Кот Пушок")]

for resident in residents:
    cprint(resident, color='cyan')

for day in range(1, 10):
    cprint('================== День {} =================='.format(day), color='yellow')
    house.dirt += len(residents) * 5

    for resident in residents:
        if resident.inspect() is False:
            resident.act()

    for resident in residents:
        cprint(resident, color='magenta')

    cprint('================== Вечер ===================', color='yellow')
    cprint(house, color='green')

cprint("Всего было заработанно {} руб, куплено еды {} для людей, {} для кота и куплено {} шуб".format(house.total_many,
                                                                                                      house.total_food_human,
                                                                                                      house.total_food_cat,
                                                                                                      house.total_coat))

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
# # TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


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
        self.meal = 50  # еды в холодильнике для людей.
        self.meal_cat = 30  # еды для кота.
        self.dirt = 0  # % кол-во грязи.

    def __str__(self):
        return f'Я - {self.name}, денег в тумбочке {self.many} рублей, еды в холодильнике {self.meal}, еды для кота' \
               f' {self.meal_cat}, грязи в доме {self.dirt}%.'


class Human:

    def __init__(self, name):
        self.my_house = house
        self.name = name  # имя.
        self.satiety = 30  # % степень сытости.
        self.happiness = 100  # % степень счастья.

    def eat(self):  # есть, кушают взрослые максимум по 10 единиц еды, степень сытости растет на 10 за 10 еды.
        if house.meal < 10:
            cprint('Что-то кушать хочется, а в холодильнике мышь повесилась...кто-то вместо еды шубы покупает.', "red")

        else:
            house.meal -= 10
            self.satiety += 10
            if self.satiety > 100:
                self.satiety = 100
            cprint(f"{self.name} поел.")

    def __str__(self):
        return f'Я - {self.name}, степень сытости {self.satiety}% , степень счастья {self.happiness}%.'


class Husband(Human):  # Муж

    def __init__(self, name):
        super().__init__(name)
        self.earnings = 0

    def __str__(self):

        return super().__str__()

    def inspect(self):
        if house.dirt >= 80:  # Если в доме грязи больше 80 - у людей падает степень счастья каждый день на 10 пунктов,
            self.happiness -= 10

        if self.satiety <= 10:
            self.eat()
            return True
        elif self.happiness <= 20:
            self.gaming()
            return True
        elif house.many <= 100:
            self.work()
            return True
        elif self.satiety >= 90:
            self.gaming()
            return True
        else:
            return False

    def act(self):
        cube = randint(1, 3)
        if cube == 1:
            self.eat()
        elif cube == 2:
            self.work()
        elif cube == 3:
            self.gaming()
        else:
            print("Что-то пошло не так...")

    def eat(self):  # есть, кушают взрослые максимум по 10 единиц еды, степень сытости растет на 10 за 10 еды.
        super().eat()

    def work(self):  # ходить на работу, деньги в тумбочку добавляет муж, после работы - 150 единиц за раз,
        # приводит к уменьшению степени сытости на 10 пунктов
        house.many += 150
        self.satiety -= 10
        self.earnings += 150
        cprint("{} сходил на работу.".format(self.name), 'cyan')

    def gaming(self):  # играть в WoT, приводит к уменьшению степени сытости на 10 пунктов
        self.satiety -= 10
        self.happiness += 20  # Степень счастья растет от игры в WoT (на 20)
        if self.happiness >= 100:
            self.happiness = 100

        cprint("{} играл в WoT целый день.".format(self.name), 'cyan')


class Wife(Human):  # Жена

    def __init__(self, name):
        super().__init__(name)
        self.coat = 0

    def __str__(self):
        return super().__str__()

    def inspect(self):

        if house.dirt >= 80:  # Если в доме грязи больше 80 - у людей падает степень счастья каждый день на 10 пунктов,
            self.happiness -= 10
        if self.satiety <= 10:
            self.eat()
            return True
        elif self.happiness <= 20:
            self.buy_fur_coat()
            return True
        elif house.meal <= 50 or house.meal_cat <= 30:
            self.shopping()
            return True
        elif house.dirt >= 80:
            self.clean_house()
            return True
        else:
            return False

    def act(self):
        cube = randint(1, 4)
        if cube == 1:
            self.eat()
        elif cube == 2:
            self.shopping()
        elif cube == 3:
            self.buy_fur_coat()
        elif cube == 4:
            self.clean_house()
        else:
            print("Что-то пошло не так...")

    def eat(self):  # есть, кушают взрослые максимум по 10 единиц еды, степень сытости растет на 10 за 10 еды.
        super().eat()

    def shopping(self):  # покупать продукты, еда стоит 100 денег 100 единиц еды,
        # приводит к уменьшению степени сытости на 10 пунктов

        if house.meal >= 100:
            cprint("{} пошёл в магазин и вспомнил, что холодильник то не резиновый...".format(self.name), "magenta")

        elif house.many <= 100:
            cprint("{} надумал купить еды, но денег маловато...кто-то мало зарабатывает.".format(self.name), "magenta")
        else:
            house.many -= 100
            house.meal += 100
            self.satiety -= 10
            cprint("{} сходил в магазин за едой.".format(self.name), "magenta")
        if house.meal_cat >= 100:
            cprint("...у кота еды полно...", "magenta")
        elif house.many <= 50:
            cprint("{} надумал купить еды коту, но денег маловато...кто-то мало зарабатывает.".format(self.name),
                   "magenta")
        else:
            house.many -= 50
            house.meal_cat += 50
            cprint("{} сходил в магазин за едой коту.".format(self.name), "magenta")

    def buy_fur_coat(self):  # покупать шубу, стоит 350 единиц, приводит к уменьшению степени сытости на 10 пунктов
        if house.many <= 500:
            cprint("{} надумал купить себе шубу, но денег маловато...кто-то мало зарабатывает.".format(self.name),
                   "magenta")

        else:
            house.many -= 350
            self.coat += 1
            self.satiety -= 10
            self.happiness += 60  # Степень счастья растет от покупки шубы на 60
            if self.happiness >= 100:
                self.happiness = 100
            cprint("{} купил себе шубу.".format(self.name), "magenta")

    def clean_house(self):  # убираться в доме, приводит к уменьшению степени сытости на 10 пунктов
        if house.dirt <= 50:
            cprint("{} надумал убраться...но дома чисто.".format(self.name), "magenta")

        else:
            house.dirt = 0
            self.satiety -= 10
            cprint("{} убрался в доме.".format(self.name), "magenta")


class Cat:
    def __init__(self, name):
        self.my_house = house
        self.name = name  # У котов есть имя
        self.satiety = 30  # У котов есть степень сытости (в начале - 30)

    def eat(self):  # есть, кушают коты максимум по 10 единиц еды, степень сытости растет на 20 за 10 еды.
        if house.meal < 10:
            cprint('Что-то кушать хочется, а в холодильнике мышь повесилась...кто-то вместо еды шубы покупает.',
                   "red")

        else:
            house.meal_cat -= 10
            self.satiety += 20
            cprint("{} поел.".format(self.name))

    def sleep_cat(self):
        # приводит к уменьшению степени сытости на 10 пунктов
        self.satiety -= 10
        cprint("{} спал целый день.".format(self.name), 'cyan')

    def tear_up_wallpaper(self):
        # приводит к уменьшению степени сытости на 10 пунктов
        self.satiety -= 10
        house.dirt += 10
        cprint("{} драл обои целый день.".format(self.name), 'cyan')

    def inspect(self):
        if self.satiety <= 10:
            self.eat()
            return True
        else:
            return False

    def act(self):
        cube = randint(1, 3)
        if cube == 1:
            self.eat()
        elif cube == 2:
            self.sleep_cat()
        elif cube == 3:
            self.tear_up_wallpaper()
        else:
            print("Что-то пошло не так...")

    def __str__(self):
        return 'Я - {}, степень сытости {}% .'.format(self.name, self.satiety)


cprint('================== Начало ==================', color='red')
house = House("Семейный дом")
cprint(house, color="green")

residents = [Wife(name="Beavis"),
             Husband(name="Butthead"),
             Cat(name="Васька"),
             Cat(name="Пушок")]

for resident in residents:
    cprint(resident, color='cyan')

for day in range(1, 10):
    cprint('================== День {} =================='.format(day), color='red')
    house.dirt += len(residents) * 5

    for resident in residents:
        if resident.inspect() is False:
            resident.act()

    for resident in residents:
        cprint(resident, color='magenta')

    cprint('================== Вечер ===================', color='white')
    cprint(house, color='green')

cprint("Всего было заработанно {} руб и куплено {} шуб".format(residents[1].earnings, residents[0].coat))

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

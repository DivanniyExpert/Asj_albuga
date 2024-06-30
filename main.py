import random
import fight
import shop
import statistika



class player:
    hp = 100
    fix_hp = 100
    damage = 1

pl = player

class Enemy1:
    hp = random.randint(10, 25)
    damage = random.randint(2, 5)

e1 = Enemy1

class Enemy2:
    hp = random.randint(50, 100)
    damage = random.randint(5, 10)

e2 = Enemy2

class Enemy3:
    hp = random.randint(150, 200)
    damage = random.randint(15, 20)

e3 = Enemy3

def run():

    while True:
        print('1 - В бой \n 2 - Магазин \n 3 - Статистика')
        menu = int(input('Выбор: '))
        if menu == 1:
            fight.f_menu()
        elif menu == 2:
            shop.shop_menu(pl.hp, pl.fix_hp)
        elif menu == 3:
            statistika.menu_stats(pl)

run()
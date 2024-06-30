import main


def shop_menu(hp, fix_hp):
    print("1) Защита \n 2) Оружие")
    vibr = int(input('Ваш выбор: '))
    if vibr == 1:
        print('Бронежилеты: \n 1 класс (50) \n 2 класс (100)')
        bronik = int(input("Ваш выбор: "))
        k = 1
        if bronik == 1 and k == 1:
            fix_hp = hp + 30
            k = 0
        elif k == 0:
            print('Уже приобретено')
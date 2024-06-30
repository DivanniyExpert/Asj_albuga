import random
import main



def f_menu():
    print('1) Начинающий каратист \n 2) Уличный боец \n 3) Проффессиональный боксер')
    vibor = int(input('Ваш выбор: '))
    if vibor == 1:
        while main.e1.hp > 0:
            print(f"Ваше здоровье: {main.pl.hp} Ваш урон: {main.pl.damage}")
            print(f"Вран hp: {main.e1.hp} damage: {main.e1.damage}")
            print("=========================================")
            print("1) Удар \n 2) Восстановить здоровье")
            n = int(input("Ваш выбор: "))
            if n == 1:
                main.e1.hp -= main.pl.damage
                print(f"Вы атаковали противника, у него осталось {main.e1.hp} hp")
                main.pl.hp -= main.e1.damage
                print(f"Противник атаковал вас, у вас осталось {main.pl.hp} hp")

            if n == 2:
                main.pl.hp += random.randint(0,5)
                if main.pl.hp > main.pl.hp:
                    main.pl.hp = 100

                print(f"Ваши хп {main.pl.hp}")

            else:
                print("Чего ждем?")
            if main.pl.hp < 0:
                print("Вы проиграли")
            if main.e1.hp < 0:
                print("Вы победили")

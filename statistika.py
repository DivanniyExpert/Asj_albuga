import main


def menu_stats(pl):
    print('================================================')
    print("ВАША СТАТИСТИКА")
    print("================================================")
    print("hp %s."%(main.pl.hp))
    print(f"Ваше здоровье: {main.fix_hp}")
    print("Урон %s."%(main.pl.damage))
    input("Нажмите Enter для продолжения.")
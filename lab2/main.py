from game_objects import Archer, Fort, MobileHouse


def main():
    print("Лабораторная работа 2. Основы ООП\n")

    archer = Archer(1, "Робин", 0, 0)
    enemy = Archer(2, "Разведчик", 5, 3, 80.0)
    fort = Fort(3, "Северная", 4, 4)
    house = MobileHouse(4, "Обоз", 1, 1, True)

    objects = [archer, enemy, fort, house]

    print("Начальное состояние объектов:")
    for gameObject in objects:
        print(gameObject.getInfo())

    archer.moveTo(2, 3)
    house.moveTo(3, 3)
    print(f"\nЛучник переместился в ({archer.getX()}, {archer.getY()}).")
    print(f"Дом переместился в ({house.getX()}, {house.getY()}).")

    fort.attack(enemy)
    print(f"Атака недостроенной крепости: HP противника = {enemy.getHp():g}.")

    archer.attack(enemy)
    print(f"Лучник нанёс 20 урона: HP противника = {enemy.getHp():g}.")

    fort.finishConstruction()
    fort.attack(enemy)
    print(f"Крепость достроена и нанесла 35 урона: HP = {enemy.getHp():g}.")

    fort.attack(enemy)
    print(f"Повторная атака крепости: HP = {enemy.getHp():g}, жив: {enemy.isAlive()}.")

    enemy.moveTo(10, 10)
    print(f"Мёртвый юнит остался в ({enemy.getX()}, {enemy.getY()}).")

    print("\nПолиморфный вызов getInfo():")
    for gameObject in objects:
        print(gameObject.getInfo())


if __name__ == "__main__":
    main()

from abc import ABC, abstractmethod
from math import isfinite


class GameObject(ABC):
    def __init__(self, objectId, name, x, y):
        if not isinstance(objectId, int) or objectId <= 0:
            raise ValueError("Идентификатор должен быть положительным целым числом.")

        if name is None or name.strip() == "":
            raise ValueError("Имя объекта не должно быть пустым.")

        self._id = objectId
        self._name = name.strip()
        self._setPosition(x, y)

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def _setPosition(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Координаты должны быть целыми числами.")

        self._x = x
        self._y = y

    @abstractmethod
    def getInfo(self):
        pass


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def moveTo(self, x, y):
        pass


class Unit(GameObject):
    def __init__(self, objectId, name, x, y, hp):
        super().__init__(objectId, name, x, y)

        if not isfinite(hp) or hp <= 0:
            raise ValueError("Начальное здоровье должно быть положительным числом.")

        self._hp = float(hp)

    def isAlive(self):
        return self._hp > 0

    def getHp(self):
        return self._hp

    def receiveDamage(self, damage):
        if not isfinite(damage) or damage < 0:
            raise ValueError("Урон должен быть конечным неотрицательным числом.")

        self._hp = max(0.0, self._hp - damage)


class Building(GameObject):
    def __init__(self, objectId, name, x, y, built=False):
        super().__init__(objectId, name, x, y)
        self._built = bool(built)

    def isBuilt(self):
        return self._built

    def finishConstruction(self):
        self._built = True


class Archer(Unit, Attacker, Moveable):
    def __init__(self, objectId, name, x, y, hp=100.0, damage=20.0):
        super().__init__(objectId, name, x, y, hp)

        if not isfinite(damage) or damage <= 0:
            raise ValueError("Сила атаки должна быть положительным числом.")

        self._damage = float(damage)

    def attack(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError("Атаковать можно только юнита.")

        if not self.isAlive() or unit is self or not unit.isAlive():
            return

        unit.receiveDamage(self._damage)

    def moveTo(self, x, y):
        if not self.isAlive():
            return

        self._setPosition(x, y)

    def getInfo(self):
        return f"Лучник {self._name}: id={self._id}, ({self._x}, {self._y}), HP={self._hp:g}"


class Fort(Building, Attacker):
    def __init__(self, objectId, name, x, y, built=False, damage=35.0):
        super().__init__(objectId, name, x, y, built)

        if not isfinite(damage) or damage <= 0:
            raise ValueError("Сила атаки должна быть положительным числом.")

        self._damage = float(damage)

    def attack(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError("Атаковать можно только юнита.")

        if not self.isBuilt() or not unit.isAlive():
            return

        unit.receiveDamage(self._damage)

    def getInfo(self):
        state = "построена" if self.isBuilt() else "строится"
        return f"Крепость {self._name}: id={self._id}, ({self._x}, {self._y}), {state}"


class MobileHouse(Building, Moveable):
    def moveTo(self, x, y):
        if not self.isBuilt():
            return

        self._setPosition(x, y)

    def getInfo(self):
        state = "построен" if self.isBuilt() else "строится"
        return f"Дом на колёсах {self._name}: id={self._id}, ({self._x}, {self._y}), {state}"

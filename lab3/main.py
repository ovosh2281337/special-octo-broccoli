from singleton import Singleton
from factory_method import FileLoggerFactory, ConsoleLoggerFactory
from abstract_factory import Application, WindowsFactory, MacFactory
from builder import HawaiianPizzaBuilder, PizzaDirector


def main():
    print("1. Singleton")
    first = Singleton.getInstance()
    second = Singleton.getInstance()
    print("Один и тот же объект:", first is second)

    print("\n2. Factory Method")
    FileLoggerFactory().logMessage("Hello")
    ConsoleLoggerFactory().logMessage("Hello")

    print("\n3. Abstract Factory")
    Application(WindowsFactory()).paint()
    Application(MacFactory()).paint()

    print("\n4. Builder")
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)
    director.constructPizza()
    print(builder.getResult())


if __name__ == "__main__":
    main()

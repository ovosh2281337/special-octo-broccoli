class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""

    def __str__(self):
        return f"Pizza: {self.dough}, {self.sauce}, {self.topping}"


class HawaiianPizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def buildDough(self):
        self.pizza.dough = "cross"

    def buildSauce(self):
        self.pizza.sauce = "mild"

    def buildTopping(self):
        self.pizza.topping = "ham+pineapple"

    def getResult(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def constructPizza(self):
        self.builder.buildDough()
        self.builder.buildSauce()
        self.builder.buildTopping()

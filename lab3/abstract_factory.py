class WindowsButton:
    def paint(self):
        print("Windows button")


class MacButton:
    def paint(self):
        print("Mac button")


class WindowsCheckbox:
    def paint(self):
        print("Windows checkbox")


class MacCheckbox:
    def paint(self):
        print("Mac checkbox")


class GUIFactory:
    def createButton(self):
        raise NotImplementedError

    def createCheckbox(self):
        raise NotImplementedError


class WindowsFactory(GUIFactory):
    def createButton(self):
        return WindowsButton()

    def createCheckbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def createButton(self):
        return MacButton()

    def createCheckbox(self):
        return MacCheckbox()


class Application:
    def __init__(self, factory):
        self.button = factory.createButton()
        self.checkbox = factory.createCheckbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

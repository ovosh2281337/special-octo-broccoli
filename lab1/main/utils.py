def getGreeting(name):
    if name is None:
        return "Привет!"

    name = name.strip()

    if name == "":
        return "Привет!"

    return "Привет, " + name + "!"

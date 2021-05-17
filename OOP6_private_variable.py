print("Latihan object Oriented Programming (OOP)")
print("     <Private & Protected>")

class Hero:

    #class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private(dengan dua underscore)
        self.__private = "private"
        # variable instance protected(dengan satu underscore)
        self._protected ="protected"

lina = Hero("lina", 100)

print(lina.__dict__)

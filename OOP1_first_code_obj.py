print("Latihan object Oriented Programming (OOP)")

#Membuat class object pada python
class Hero:
    def __init__(self, InputName, InputAge, InputPos):
        #instance variable
        self.name = InputName
        self.age = InputAge
        self.position = InputPos

#Mengisi propertynya
hero1 = Hero("Miranda", 20, "Jr. Engineer")
hero2 = Hero("budi", 27, "Reservoir Engineer")
hero3 = Hero("Fandi", 29, "Manager area")

#Print
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
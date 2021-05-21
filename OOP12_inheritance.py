print("Latihan object Oriented Programming (OOP)")
print("     <Inheritance-pewarisan>")
print("     <Superclass Vs Subclass atau anaknya si class utama>")


#Membuat class utama
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

 #membuat sub class yang mewarisi sifat class utama
class Hero_intelligent(Hero):
    pass

class Hero_strenght(Hero):
    pass

#Membuat objek
dudung = Hero('Dudung', 100)            #dari class utama
maman = Hero_intelligent('maman', 98)   #dari sub class
cepi = Hero_strenght('cepi', 80)        #dari sub class

#panggil
print(dudung.name)
print(maman.name)
print(cepi.name)
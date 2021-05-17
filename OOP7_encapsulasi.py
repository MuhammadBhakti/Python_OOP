print("Latihan object Oriented Programming (OOP)")
print("     <Encapsulasi = membuat semua variable menjadi private, menjaga namanya supaya tidak berubah>")
print("     <Setter & Getter>")

class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # Setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self,nilaibaru):
        self.__attPower = nilaibaru

#awal dari game, set nama karakter
budi = Hero("Budi", 100, 10)

#game berjalan
print(str(budi.getName()) + " dengan nilai awal " + str(budi.getHealth()))

#perubahan
budi.diserang(10) #nilai serangan = 10
print(budi.getHealth())
budi.diserang(12) #serangan kedua
print(budi.getHealth())
budi.diserang(7) #serangan ketiga
print(budi.getHealth())
budi.diserang(8) #serangan keempat
print(budi.getHealth())


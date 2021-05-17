print("Latihan object Oriented Programming (OOP)")
print("     <static method & classmethod>")

class Hero:

    #private class variabel
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    #method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    #method ini tidak hanya berlaku untuk objek tapi juga class
    def getJumlah1():
        return Hero.__jumlah

    #method static, nempel untuk class dan object
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    #class method
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

#nama karakter
budi = Hero('budi')
#print pertama
print(Hero.getJumlah2())

#nama karakter
doni = Hero('doni')
#print kedua
print(Hero.getJumlah2())

#nama karakter
yandi = Hero('yandi')
#print ketiga
print(Hero.getJumlah3())
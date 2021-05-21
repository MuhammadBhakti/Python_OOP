print("Latihan object Oriented Programming (OOP)")
print("     <Latihan encapsulasi>")
print("     <Menambah experience pada variable>")
print("     <perhitungan on the fly tanpa diketahui oleh client>")

class Hero:

    #private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healtMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healtMax
        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}: \n\thealth = {}/{} \n\tattack ={} \n\tarmor ={}".format(self.__name,self.__level, self.__health, self.__healtMax, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass
    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -=100

            self.__healtMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    #Method
    def attack(self, musuh):
        self.gainExp = 50


dadang = Hero('dadang', 100,5,10)
maman = Hero('maman', 100, 5, 10)
print(dadang.info)

#case
dadang.attack(maman)
dadang.attack(maman)
dadang.attack(maman)
print(dadang.info)
print("Latihan object Oriented Programming (OOP)")
print("     <Getter & Setter>")
print("     <Merubah variabel/properties nya on the fly>")

class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    #property bisa di update diluar method init
    #membuat method info supaya bisa di panggil name nya dan healthnya
    @property
    def info(self):
        return "name {}: \n\thealth {}:".format(self.name,self.__health)

    #bagian ini adalah membuat property yang bersifat private agar bisa dirubah, tahapannya ada 3 yaitu:
    #1. membuat method armor tapi di pass dulu
    @property
    def armor(self):
        pass
    #2. membuat fungsi getter untuk armor, memanggil si property private armor
    @armor.getter
    def armor(self):
        return self.__armor
    #3. membuat fungsi yang bisa membuat si armor dapat dirubah dengan variabel input yang baru
    @armor.setter
    def armor(self,input):
        self.__armor = input

#set si characternya
sniper = Hero('sniper',100,10)

#coba print info(name,health)
print('merubah info')
print(sniper.info)
#merubah nama karakter, karena nama tidak di privage bisa langsung aja
sniper.name = 'andi'
print(sniper.info)

#cek sebentar apakah ada perubahan?
print('getter dan setter untuk armor: ')
print(sniper.armor)
print(sniper.__dict__)
#merubah armor yang di private, lalu print
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)



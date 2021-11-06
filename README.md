# Python_OOP

```python 3.8``` 


Some example project using object oriented programming (OOP)

```{python}
class Hero:

    def __init__(self, name, healt, attackPower, armorNumber):
        self.name = name
        self.health = healt
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attackPower) #dibuat setelah methods yang dibawah dibuat dulu

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + " Diserang " + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('serangan terasa: ' + str(attack_diterima))
        self.health -= attack_diterima
        print("darah " + self.name + " Tersisa " + str(self.health))

#ACTION - nama karakternya
sniper = Hero("Sniper",100, 10, 5)
rikimaru = Hero("rikimaru", 100, 20, 10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
print("\n")
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
print("\n")
```

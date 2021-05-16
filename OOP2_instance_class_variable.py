print("Latihan object Oriented Programming (OOP)")
print("     Instance & Class Variable")

#Membuat class object pada python
class Pegawai:
    jumlah = 0 #class variable
    def __init__(self, InputName, InputAge, InputPos):
        #instance variable
        self.name = InputName
        self.age = InputAge
        self.position = InputPos
        Pegawai.jumlah += 1
        print("membuat objek baru dengan nama", InputName)

#Mengisi propertynya
Pegawai1 = Pegawai("Miranda", 20, "Jr. Engineer")
print(Pegawai.jumlah)
Pegawai2 = Pegawai("budi", 27, "Reservoir Engineer")
print(Pegawai.jumlah)
Pegawai3 = Pegawai("Fandi", 29, "Manager area")
print(Pegawai.jumlah)

#Print
print(Pegawai1.__dict__)
print(Pegawai2.__dict__)
print(Pegawai3.__dict__)
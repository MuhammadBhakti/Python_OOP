print("Latihan object Oriented Programming (OOP)")
print("     <METHOD>")

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

    #Membuat METHOD, ada 3 jenis:
    # 1.Void, method tanpa return
    def siapa(self):
        print("Namaku adalah " + self.name)

    # 2. Method dengan argumen
    def ageUp(self, up):
        self.age += up

    # 3. Method dengan return
    def getAge(self):
        return self.age

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

#Print Method
Pegawai1.siapa()
Pegawai2.siapa()
Pegawai3.siapa()

#Penambahan umur dari method ke-2
Pegawai1.ageUp(10)
#Update umur dari Method ke-3
print(Pegawai1.getAge())
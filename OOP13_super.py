print("Latihan object Oriented Programming (OOP)")
print("     <Inheritance-pewarisan>")
print("     <Superclass Vs Subclass atau anaknya si class utama>")
print("     <Lanjutan>")

class Idcard:
    def __init__(self, name, company, score):
        self.name = name
        self.company = company
        self.score = score
    def showInfo(self):
        print("{} berasal dari anak perusahaan: {}".format(self.name, self.company))

class Idcard_brsoematra(Idcard):
    def __init__(self, name):
        #Idcard.__init__(self, name) #seharusnya sih pakai cara ini, tapi bisa diganti super()
        super().__init__(name,'Branch Sumatra',80) #diambil dari superclass
        super().showInfo()

class Idcard_brjava(Idcard):
    def __init__(self, name):
        #Idcard.__init__(self, name) #seharusnya sih pakai cara ini, tapi bisa diganti super()
        super().__init__(name,'Branch Jawa', 87)
        super().showInfo()

aji = Idcard_brsoematra('Aji')
dimas = Idcard_brjava('dimas')

print(aji.name, ' : ', aji.company,' score: ', aji.score)
print(dimas.name, ' : ', dimas.company,' score: ', dimas.score)
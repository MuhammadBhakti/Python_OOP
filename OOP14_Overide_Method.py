print("Latihan object Oriented Programming (OOP)")
print("     <Override Method>")
print("     <Menimpa yang ada di superClass>")


class Pegawai:

    def __init__(self, nama, alamat, kantor):
        self.nama = nama
        self.alamat = alamat
        self.kantor = kantor

    def showInfo(self):
        print("{} alamat: {} kantor: {}".format(
            self.nama,
            self.alamat,
            self.kantor
            )
        )

class Pegawai_prestasi(Pegawai):
    def __init__(self,nama):
        super().__init__(nama,"Jakarta", "Bandung")

    #Override superclass untuk fungsi showInfo
    def showInfo(self):
        print("{} \n\tTipe: Pegawai_Prestasi \n\talamat: {} \n\tkantor:{}".format(self.nama,self.alamat,self.kantor))

class Pegawai_senior(Pegawai):
    def __init__(self, nama):
        super().__init__(nama,"balikpapan","Riau")

agung = Pegawai_prestasi('Agung')
zai = Pegawai_senior("Zai")

zai.showInfo()
agung.showInfo()
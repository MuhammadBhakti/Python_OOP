#Magic method yang ada di Python
print("\n================================")
class Nama1:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
#dari Nama1
dani = Nama1('dani', 27)
print("Dari Class Nama1 : \n\tnama :{}\n\tumur :{}".format(dani.nama,dani.umur))
print("\n================================")

class Nama2:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def __repr__(self):
        return "Dari Class Nama2 :\n\tNama : {} \n\tUmur : {}".format(self.nama,self.umur)

#dari Nama2
dadan = Nama2('dadan',32)
print(dadan)
print("\n================================")

class Nama3:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def __add__(self,objek):
        return self.umur + objek.umur

#Dari Nama3
tunu = Nama3('tunu',24)
aris = Nama3('aris',34)
print("Dua orang teman yaitu {} umur {} dan {} umur {}, rata rata usia mereka adalah :".format(tunu.nama, tunu.umur, aris.nama, aris.umur))
print((tunu + aris)/2)
print("\n================================")

class Nama4:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    @property
    def __dict__(self):
        return " objek ini mempunyai nama dan jumlah"
fadhil = Nama4('Fadhil', 26)
print(fadhil.__dict__)
print("\n================================")
#Method Resolution Order - Multiple Inheritance

class A:

    def show(self):
        print("Ini adalah Method A")

class B:
    def show(self):
        print("Ini adalah Method B")

# jika method di A sama namanya dengan class B, maka diambil berdasarkan urutan
class C(A,B):
    pass

class D(B,A):
    pass

metode1 = C()
metode2 = D()

metode1.show()
metode2.show()
#diamond problem dalam Inheritance

class A:
    def show(self):
        print("Ini adalah class A")

class B(A):
    def show(self):
        print("Ini adalah class B")

class C(A):
    def show(self):
        print("Ini adalah class C")

class D(B,C):
    pass

metode = D()

#Hasilny akan diurutkan dari D - B - C - A
metode.show()
print("Latihan object Oriented Programming (OOP)")
print("     <Multiple Inheritance>")

#Class Utama 1
class A:
    def Method_A(self):
        print("Ini adalah Method A")

#Class Utama 2
class B:
    def Method_B(self):
        print("Ini adalah Method B")

#Sub class mengambil dari dua main class
class C(A,B):
    pass

PilihMethod = C()

PilihMethod.Method_A()
PilihMethod.Method_B()




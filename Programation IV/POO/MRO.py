
class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    def hablar(self):
        print("Hola desde B")


class C(B):
    def hablar(self):
        print("Hola desde C")

        
class D(C):
    def hablar(self):
        print("Hola desde D")


d = D()
print(D.mro())
d.hablar()
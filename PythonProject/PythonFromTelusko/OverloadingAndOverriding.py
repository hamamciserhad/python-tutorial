class Student:
    # python da method overloading yoktur
    # topla(self,a,b)
    # topla(self,a,b,c) yazamasin biz de if else felan kullanacaz iste
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None and c == None:
            return a + b
        else:
            return a


s1 = Student(23, 11)
s2 = Student(24, 12)

print(s1.sum(23))


class A:
    def show(self):
        print("in a show")


class B(A):
    def show(self):
        print("in b show")


a1 = B()
a1.show()

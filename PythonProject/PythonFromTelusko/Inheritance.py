class A:
    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")


class B : # b sub class oldu

    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")

class C(A,B):
    def feature5(self):
        print("Feature 5")

a1 = A()
a1.feature1()
b1 = B()
b1.feature3()
c1 = C()
c1.feature1()

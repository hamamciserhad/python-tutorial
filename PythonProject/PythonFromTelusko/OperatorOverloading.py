a = 5
b = 5
print(a + b)
print(int.__add__(a, b))


# simdi söyle syntactic sugar denen bir sey var o ney
# pythonda islev olarak ayni ama daha tatli bir yazilimi yapmayi saglar yukarda ki gibi biz aslinda
# + operatorunu kullandigimizda normalde add() metodu geliyor

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)  # burdan geliyor

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        return Student(m1, m2)

    def __gt__(self, other):
        if self.m1 + self.m2 > other.m1 + other.m2:
            return True
        else:
            return False
    def __str__(self):
        return "{} {}".format(self.m1, self.m2) # tuple



s1 = Student(12, 23)  # Student.__init__(s1, 12, 23)
s2 = Student(24, 22)

s3 = s1 + s2  # bu aslinda sudur : Student.__add__(s1,s2) biz  burda yeni bir obje olusturuyoruz ve parametreleri s1 ve s2 nin m1 ve m2 lei toplami
print(s3.m1, s3.m2)
s4 = s1 - s2
print(s4.m1, s4.m2)

if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")

# abi biz mesela a =0 icin print a yazinca 0 cikiyor
# ama biz print s1 yazarsak adressi aliriz biz bunu degistirebilirz
a = 0
print(a)
# bu aslinda sudur
print(str(a))
# ya da su
print(a.__str__())
# bizim adres almamak icin bu str i sinif icinde tanimalamamiz lazim
print(s1)
# python da bu operatorler sadece int str gibi sinfilar icin tanimlidir kendimiz overloading edecez

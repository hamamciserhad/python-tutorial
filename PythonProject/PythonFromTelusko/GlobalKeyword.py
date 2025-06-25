a = 10  # global buna fonksiyonun icin den de erisebilirsin


def something():
    global a
    a = 12  # local variable idi yukaridan sonra global oldu
    # peki ben global olan a nin degerini degistirmek istersem o zaman global yazarim
    # peki ben hem a diye local bir variable tanimlayip sonr
    print("in func", a)


something()
print("outside", a)  # bu global olan a

# peki ben hem a diye local bir variable tanimlayip sonra da fonksiyonun icinde global olan a nin da degerini degistirmek icin ne yaparim

b = 10
c = 11
print(id(b))


def something2():
    b = 13
    x = globals()["b"]
    print(id(x))
    x = 12
    globals()["b"] = 15  # globals bütün global leri cagirir bizim belirtmemiz lazim hangisi oldugunu
    print("in func", b)


something2()
print("outside", b)

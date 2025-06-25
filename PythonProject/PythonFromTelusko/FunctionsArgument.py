# python da pass by value ve pass by referance yoktur onlar ne peki
# value fonksiyon direk degeri alir yani adresleri farkli olur
# referande da adressi alir value yu degistirirsen orjinal value da degisir
def update(x):
    # python da her sey object tir id lerine bakalim
    print(id(x))  # bunlar ayni yeri gösterir ram de
    x = 8
    print(id(x))  # ama biz degistkenin degerini degistirsek bu sefer adress de degisir ama a nin degerini etkilemez
    # yani bu pass by referance da degil
    # ama int stirng türleri immutable dir biz bunun yerine mutable bir tip mesela list kullansak bu sefer pass by referance olur
    print("x: ", x)


a = 10
print(id(a))
update(a)
print("a:", a)


def updateMutable(x):
    print(id(x))
    x[1] = 2
    print(id(x))
    print("x: ", x)

a = [3,4,5,6]
print(id(a))
updateMutable(a)
print("a:", a)
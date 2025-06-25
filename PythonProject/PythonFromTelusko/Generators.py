def topten():
    # Bu fonksiyon bir generator'dır.
    # yield ifadesi sayesinde her seferinde bir değer üretir.
    # return gibi çalışır ama fonksiyonun çalışmasını durdurmaz.
    yield 4  # yield return u generator halidir value yu iterator formatinda döndürür bi bak adresi döndürüyor bu return gibi degil yani
    # yield in return gibi 1 statment olmasi lazim degil birden fazla yield yazabilirsin
    yield 1
    yield 3


def topten2():
    # Bu fonksiyon normal bir fonksiyondur ve direkt olarak bir değer döner.
    # yield yerine return kullanıldığı için generator değildir.
    return 4


def sqr():
    # Bu generator fonksiyonu 1'den 10'a kadar sayıların karelerini üretir.
    # Bellekte hepsini tutmaz, her seferinde bir tane üretir.
    n = 1
    while n <= 10:
        yield n * n
        n += 1


# topten fonksiyonundan bir generator objesi alıyoruz
value = topten()
# Generator objesi bellekteki adresiyle temsil edilir
print(value)
values = topten2()
print(values)
# __next__() ile generator'dan sıradaki değeri alırız
# İlk çağrı 4 verir, sonra fonksiyon durduğu yerden devam eder
print(value.__next__())
# Kalan değerleri döngü ile alabiliriz
for i in value:
    print(i)
# sqr fonksiyonu ile 1'den 10'a kadar sayıların karelerini üretip yazdırıyoruz
valuee = sqr()
for i in valuee:
    print(i)

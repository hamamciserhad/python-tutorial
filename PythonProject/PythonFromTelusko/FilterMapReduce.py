# simdi senle bir listedeki cift numaralari yazdiracaz sonra da göreceksin tek satir oldgunu
# fonksiyonu lambda kullanarak yazacaz
from functools import reduce


def even(x):
    return x % 2 == 0 # bu fonksiyonu kullanmadik sadece anla diye yazdim ne yazdigimizi aslinda

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(lambda x : x%2 == 0, a)
# filter bir iterator döndürür bu da sadece bir defa kullanilir biz sunu yazarsak buraya sonrasinda b yi tüketmis oluruz = print(list(b)) ama list e type casting yaparsan bunu bu durumu yasamazsin
#We can combine filter() with other Python functions like map() or use it in a pipeline to process data efficiently.
def carp(x):
    return x * 2 # bu fonksiyonu da kullanmadik
c = map(lambda x : x*2, b) # iki ile carptik burda
#print(list(c))

# bir de reduce diye bir fonksiyon var map ile farki
# map her eleman üzerinde tek tek islem yapar
# reduce iki argüman alan bir fonksiyon alir bütün elemanlari birlestirir ve bir deger üretir
def add_all(a,b):
    return a + b
# üsttekini kullanmadan lambda kullandik 
d = reduce (lambda a,b : a+b, c)
print(d)
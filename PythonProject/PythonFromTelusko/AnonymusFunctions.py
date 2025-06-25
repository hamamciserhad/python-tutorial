# adsiz fonksiyonlar lambda

def square(x):
    return x * x # tek bir satir var

result = square(4)
print(result)
# bu yukardakini biz asagidaki gibi yazabiliriz  *args bizim parametremizdir
f = lambda a: a*a
print(f(4)) # Çıktı:
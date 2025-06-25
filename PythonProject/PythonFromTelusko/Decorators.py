def div(a, b):
    if a < b:
        a, b = b, a
    return a / b

def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

# ben mesela pay paydadan kücükse ters döndürsün öyle bulsun cevabi istiyorum normalde gidip fonksiyonun icinde bir if statment yaratabiliriz ama
# büyük dosyalarda belki de biz o fonksiyonu degistirmek istemiyebiliriz o zaman da decorators kullannilir
# o fonksiyona dokunmadan biz swap yapacaz
# decorators ile mevcut fonksiyona baska özellikler felan ekleyebilirsin
# decorators bir fonksiyonu parametre olarak alir
# sonra da fonksiyonun icin de bir inner fonction yazilir
# inner fonksiyon(wraper) div ile ayni sayida parametre alir adlari ayni olmak zorunda degil
# wrappper fonksiyonu olusturmazsan func hemen calisir ve biter o yüzden inner fonksiyon kullaniyoruz
# sonrasinda da smart div e div i parametre olarak geicirisin
div1 = smart_div(div)
print(div1(2,4))


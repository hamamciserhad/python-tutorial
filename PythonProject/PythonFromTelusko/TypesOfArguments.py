# parametre yerine python da argument denir
# formal arguman fonksiyonun taniminda kullanilan parametre
# actual argument fonksiyon cagirilirken gönderilen gercek deger
# actual argument 4 türü var :
# position(argumanlar sirasina göre bu bildigimiz)
# keyword (anahtar kelime ile),
# default (fonksiyon imzasinda bir parametreye varsayilan bir deger atanir
# varieble length ( *args : istedigin kadar pozisyonel arguman alir (tuple), **kwarghs : istedigin kadar anahtar deger aragumani alir(dict) )

def person(name, age=19):
    print("name:", name)
    print("age:", age + 2)


person(name="Serhad")  # keyword


# ben 2 degil de bircok sayiyi eklemek istiyorum variable length kullanacaz argumentin aldigi variable ler fix degildir
def my_sum(a, *b):
    c = a + sum(b)
    print(c)


my_sum(1, 2, 3, 4, 5, 6)

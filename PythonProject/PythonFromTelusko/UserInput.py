x = int(input("Enter a number: "))  # input her zaman string deger verir biz casting yapacaz
y = int(input("Enter another number: "))
# z = int(x)+int(y) bu da olurdu
z = x + y
print(z)

# bir de char yok ya python da biz bir karakter yazdirmak istersek index kullaniriz

t = input("Enter a character: ")[0]
print(t)


# eval fonksiyonu

result = eval(input("Enter a number: "))
print(result)
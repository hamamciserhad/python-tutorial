# bi de continue yu yapalim
x = int(input("Get a number: "))
i = 1
while i <= x:
    if i % 3 == 0 or i % 5 == 0:
        i +=1
        continue # döngüde asagidaki adimlari atlar
    print(i)
    i += 1

for i in range(1, 12):
    if (i % 2 != 0):
        pass ## biz tek sayilari yazdirmak istemiyoruz ama if in de statment i olmali ama yazacak bir seyimiz yoksa o zaman pass yazariz
    else:
        print(i)

import array

arr = array.array('i', [])

# önce bir length soracaz user a

n = int(input("Enter length of array: "))
for i in range(n):
    arr.append(int(input("Enter number {}: ".format(i + 1)))) # burda format fonksiyounu dinamik sekilde calisir enter number 1 sonra 2 diye gider

print(arr)

# simdi de user bize bir numara diyecek biz de o numaranin indexini bulacagiz

val = int(input("Enter number search: "))
for i in range(n):
    if arr[i] == val:
        print(i)

# veya direk print(arr.index(val)) fonksiyonu ile de yapilabilirdi
# python da default 2d array felan yok numpy diye bir library indirmen lazim onu da simdi gerek yok
import array

arr = array.array('i', [1, 2, 3, 4, -1, 5])
print(arr)
print(arr.buffer_info())
print(arr.typecode)

arr.reverse()
print(arr)

for i in range(len(arr)):
    print(arr[i])

# yeni array oluştur
newArray = array.array(arr.typecode, (a * a for a in range(0, len(arr))))

for i in range(len(newArray)):
    print(newArray[i])
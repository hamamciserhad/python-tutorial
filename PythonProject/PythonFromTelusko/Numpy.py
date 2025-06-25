import numpy as np

arr = np.array([1, 2, 3, 4, -1, 5])
arr2 = np.array([12, 22, 23, 42, 12, 25])
# array copy
arr = arr + 3
print(arr)
# array toplama
arr3 = arr + arr2
print(arr3)
# mat ifadeleri de tanimli hale gelir cos sin log
print(np.log(arr))
print(np.min(arr))
# iki arrayi birlestirme
arrCon = np.concatenate((arr, arr2), axis=0)
print(arrCon)
# söyle biz bir array in kopyasini direk esitleyerek atariz
# ama öyle yaparsak ayni adressi gösterirler
# view() fonksiyonunu kullanacaz

arrCopy = arr.view()
arr[1]= 8
print(arrCopy)
print(id(arrCopy))
print(id(arr))
# söyle simdi bu shallow  copy oluyor
# deep copy icin ise copy() kullanilir
arrDeepCopy = arr.copy()
arr[1]= 9 # görürüsun zaten ciktida degismiyor 
print(arrDeepCopy)
print(id(arrDeepCopy))
print(id(arr))


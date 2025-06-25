import numpy

arr = numpy.array([[1, 2, 3, 32, 4, 5], [4, 5, 3, 2, 1, 6]])
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

# arr2 kur ama 1d olsun arr dan al flatten()
arr2 = arr.flatten()
print(arr2)

# 1d den 2d ye

arr3 = arr2.reshape(2, 2, 3)
print(arr3)

# bir de matrix diye bir fonksiyon varmis onu da yazalim

m = numpy.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m1 = numpy.matrix([[1, 3], [1, 3], [4, 5]])
print(m)
# bu matrix in icinden sadece diagonal(kösegen) olanlari sec mek icin diagonal()
print(m.diagonal())
print(m.max())
# carpma islemi
print(m * m1)

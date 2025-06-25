def search(array, index):
    for i in range(len(array)):
        if array[i] == index:
            return i
    else:
        return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
index = search(array, 8)
print(index)
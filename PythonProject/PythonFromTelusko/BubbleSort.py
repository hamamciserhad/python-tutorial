def bubble_sort(array):
    for i in range (len(array)-1):
        for j in range (len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


array = [5, 6, 1, 3]
bubble_sort(array)
for i in range (len(array)):
    print(array[i])


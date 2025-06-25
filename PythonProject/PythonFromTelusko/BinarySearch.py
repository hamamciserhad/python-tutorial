def binary_search(array, numberToFind):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2 # bu integer division icin kullanilir

        if array[mid] < numberToFind:
            low = mid + 1
        elif array[mid] > numberToFind:
            high = mid - 1
        else:
            return mid
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
i= int(input("Bir sayi giriniz: "))
index = binary_search(array, i)
if index != -1:
    print(f"Number {i} found at index: {index}")
else :
    print(f"Number {i} not found")

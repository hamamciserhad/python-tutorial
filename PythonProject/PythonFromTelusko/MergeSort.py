def merge_sort(array, left, right, tempArray):
    if (right - left > 1):
        mid = (left + right) // 2
        merge_sort(array, left, mid, tempArray)
        merge_sort(array, mid , right, tempArray)
        merge(array, left, mid, right, tempArray)


def merge(array, left, mid, right, tempArray):
    i = left
    j = mid
    k = 0
    while i < mid and j < right:
        if array[i] < array[j]:
            tempArray[k] = array[i]
            i = i + 1
            k = k + 1
        else:
            tempArray[k] = array[j]
            j = j + 1
            k = k + 1

    # a[start:end] = b[start:end] kullanacaz simdi temparray deki leri arraya copy etmek icin

    tempArray[k:k + (mid - i)] = array[i:mid] # sol kisimi arraya kopyaladik
    tempArray[k:k + (right - j)] = array[j:right] # sag kismi arraya kopyaladik
    array[left:right] = tempArray[0:right - left] # bastan sona


def helper_merge_sort(array):
    tempArray = [0] * len(array)
    merge_sort(array, 0, len(array), tempArray)



nums = [3,2,1,5,33,6]
helper_merge_sort(nums)
print(nums)
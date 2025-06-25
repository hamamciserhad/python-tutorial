def count(lst):
    even = 0
    odd = 0
    for item in lst:
        if item % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd) # bu bir tuple döner



cift, tek = count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Even: {} and Odd: {}".format(cift, tek))



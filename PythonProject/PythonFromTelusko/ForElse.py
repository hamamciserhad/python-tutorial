nums = [1, 2, 3, 4, 5]
# 5 e bölünebilen bir sey var mi diye bakalim
for num in nums:
    if num % 5 == 0:
        print(num)
        break
    # else i tüm for bittikten sonra yazdirmak icin tabi break kullanilmamisa else i sola yakin yazariz
else:
    print("Not found")
    # bildigin iteratör javadaki
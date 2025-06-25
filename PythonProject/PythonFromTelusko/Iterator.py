from numpy.f2py.crackfortran import expectbegin


class EvenNumbers:
    def __init__(self, limit,number=0):
        self.limit = limit
        self.number = number



    def __iter__(self):
        return self

    def __next__(self):
        if self.number < self.limit:
            result = self.number
            self.number += 2
            return result
        else :
            raise StopIteration

nums = EvenNumbers(10) # evenNumbers adli bir nesne olusturduk ve limit 10 oldu number 0
# iter fonksiyonunu cagir ve nums objesini parametre olarak ata
it = iter(nums) # bu aslinda sudur : it = nums.__iter__() biz su an nums nesnesini it ye atadik aslinda ama bizim it miz su an iterator destekli  aslinda bu satiri cikarip sonra next e direk nums parametresi ataybilirdik de neyse ama mesela bu bizim ozel olusturdugumuz sinif normal bir liste den bir iterator olustursak orda mantikli olur bir it obj si olusturmak cunku diger fonksiyonlara da erisiriz
while True:
    try:
        print(next(it)) # it.__next__()
    except StopIteration:
        print("Bitti.")
        break
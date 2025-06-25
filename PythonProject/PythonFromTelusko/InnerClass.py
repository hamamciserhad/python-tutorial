class Student:
    def __init__(self, name, rollno,):
        self.name = name
        self.rollno = rollno
        self.comp = self.Comp("HP", "i5", 8)

    def show(self):
        print(self.name, self.rollno)
        self.comp.show()

    # student in bir de laptop u olsun ama laptop un configi fazla init icine o kadar özellik yazacagimiza ya class kurup import ederiz veya inner class cünkü sadece bu student modulunde kullanacaz
    class Comp:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
            # bu comp sinifinin obj sini biz gidip dis sinifin constr da tanimalariz veya cagirirken Student.Comp olarak arariz

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Sam", 2)
s1.show()
Student.Comp("HP", "i5", 8).show()
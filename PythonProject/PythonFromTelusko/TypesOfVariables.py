class Car:
    wheels = 4  # class variable: shared across all instances static variable de denir 

    def __init__(self, mil, company):
        self.mil = mil         # instance variable
        self.company = company # instance variable

    def display(self):
        return f"{self.mil}, {self.company}, {self.wheels}"


# instance variable her nesneye özeldir init icinde tanimlanir
# class variable lar tüm nesneler icin ortaktik init disinda tanimlanir

c1 = Car(23, 186)
c1.wheels = 5
print(c1.display())

c2 = Car(2, 186)
print(c2.display())

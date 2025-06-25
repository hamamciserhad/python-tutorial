# cok bicimlilik demek               # Polymorphism: Aynı method farklı sınıflarda farklı işler yapabilir
# duck typing                       # Tipten çok nesnenin davranışına göre işlem yapılır (örneğin: hasattr ile kontrol)
# operator overloading             # Operatörleri (örneğin +) sınıf içinde yeniden tanımlayarak farklı anlamlar yüklenebilir
# method overloading               # Aynı isimli methodların farklı parametrelerle tanımlanması (Python'da default argümanlarla yapılır)
# method overriding                # Alt sınıf, üst sınıftaki methodu aynı isimle yeniden tanımlar
from PythonFromTelusko.FilterMapReduce import add_all

# bi kus ördegin butun özelliklerini kapsiyor ise o bir ördektir
x = 5
print(type(x))
x = "Serhad"
print(type(x))


# Duck Typing Example: Farklı sınıflar aynı methodu içerdiği sürece, nesne tipi önemli değildir.
class Pycharm:
    def execute(self):
        print("Compiling in Pycharm")
        print("Running in Pycharm")


class VSCode:
    def execute(self):
        print("Compiling in VSCode")
        print("Running in VSCode")


class Laptop:
    def code(self, ide):
        # Duck typing: ide can be any object with an 'execute' method
        ide.execute()  # bana gelen ide nesnesinde execute varsa calistiririm, ne türden oldugu önemli degil


# Demonstration
ide1 = Pycharm()
ide2 = VSCode()

lap = Laptop()
lap.code(ide1)  # Works because Pycharm has execute()
lap.code(ide2)  # Also works because VSCode has execute()
# bunu java da yapmak icin interface olusturur sonra onu implement eden ide ler olusturup sonra da o interface i olusturmak icin de gidip o siniflari kullaniriz



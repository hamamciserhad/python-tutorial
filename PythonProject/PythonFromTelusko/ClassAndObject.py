class Computer:
    # bir sinfin variable i ve metodlari olur
    # python da constructor __init__ sekilinde tanimlanir istedigin parametreleri ve de self i girersin bu self aslind java da ki this e benziyor
    # o nesnenin kendisi
    def __init__(self, cpu, ram, gb):
        self.cpu = cpu
        self.ram = ram
        self.gb = gb

    def config(self):
        # simdi bir tane f string diye bir özellik varmis onu kullanacam Bunun sayesinde süslü parantez {} içine değişken, ifade veya fonksiyon yazabilirsin.Yani "" icinde bile.
        print(
            f"{self.cpu}, {self.ram} gb ram, {self.gb} Memory")  # burdaki self metodu cagiran nesneyi(instance) temsil eder asagida bir com1 nesnesi mesela bunu cagiriyor aslinda oradaki kullanimi su sekil Computer.config(com1) biz bu sekilde de yazabiliriz ama benim yazdigim sekilde de python kendisi otobmatik zaten cevirir


a = "i"  # bu da mesela string sinifina ait bir obje aslinda
print(type(a))

# biz bir tane variable in türünü sinif in türünde istiyorsak söyle yapariz
com1 = Computer("m2", 16, "1 tb")  # bu bize obj sini verir computer in
print(type(com1))
com1.config()


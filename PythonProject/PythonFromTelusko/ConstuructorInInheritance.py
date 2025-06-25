# ----------------------------
# Constructor and Inheritance in Python (Tutorial Style)
# ----------------------------

# Yardımcı çizgi fonksiyonu (görsel ayrım için)
def line(): 
    print("-" * 40)

# Base class A
class A:
    def __init__(self):
        print("in A init")  # A sınıfının yapıcısı

    def feature1(self):
        print("feature1 from A")

    def feature2(self):
        print("feature2 from A")

# Base class B
class B:
    def __init__(self):
        # Çoklu kalıtımda etkili olan bir çağrı
        super().__init__()
        print("in B init")  # B sınıfının yapıcısı

    def feature1(self):
        print("feature1 from B")

    def feature3(self):
        print("feature3 from B")

    def feature4(self):
        print("feature4 from B")

# Derived class C (inherits from both A and B)
class C(A, B):
    def __init__(self):
        # MRO'ya göre A'nın constructor'ı önce gelir
        super().__init__()
        print("in C init")

    def feat(self):
        super().feature2()

# Nesne oluşturup yapıcıların nasıl çalıştığını görelim
line()
a1 = C()
line()

# feature1 metodu hem A hem B'de var.
# MRO'ya göre A önce geldiği için A'nınki çalışır.
a1.feature1()
a1.feat()
line()
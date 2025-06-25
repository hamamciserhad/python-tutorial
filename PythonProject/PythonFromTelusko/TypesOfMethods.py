# 3 metod türü vardir
# instance , class, static methods
# instance nin de accessor ve mutator diye iki metod a ayrilir
# cok önemli bir sey yazacam
# biz eger class variable ile  class metod u calisacaksak cls
# instance variable ile calisacaksak self key ini kullaniriz
# -----------------------------
# Python Method Types Tutorial
# -----------------------------
# In Python, there are three main types of methods:
# 1. Instance Methods  → use 'self' and can access instance variables
# 2. Class Methods     → use 'cls' and can access class variables
# 3. Static Methods    → don't use 'self' or 'cls'; they behave like normal functions in a class
#
# Instance methods can be further divided into:
# - Accessor methods → return values from instance variables
# - Mutator methods  → modify instance variables

class Student(object):
    # Class variable: shared across all instances
    school = "Telusko"

    def __init__(self, m1, m2, m3):
        # Instance variables: unique to each object
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # -----------------------------
    # Instance Methods
    # -----------------------------

    # Accessor method: returns the average of marks
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Accessor method: returns m1 value
    def get_m1(self):
        return self.m1

    # Mutator method: sets a new value for m1
    def set_m1(self, m1):
        self.m1 = m1

    # -----------------------------
    # Class Methods
    # -----------------------------
    # Class method: accesses the class variable
    @classmethod
    def get_school(cls):
        return cls.school

    # -----------------------------
    # Static Methods
    # -----------------------------
    # Static method: general utility, doesn't access instance or class data
    @staticmethod
    def info():
        print("This is student class in abc module")

# -----------------------------
# Demo / Test Section
# -----------------------------
s1 = Student(23, 33, 23)
s2 = Student(23, 22, 13)

print(s1.avg())              # Average of s1's marks
print(s2.avg())              # Average of s2's marks
print(Student.get_school())  # Accessing class variable through class method
Student.info()               # Calling static method
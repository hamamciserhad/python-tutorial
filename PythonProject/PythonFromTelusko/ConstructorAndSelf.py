class Computer:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def display(self):
        print(self.name, self.age, self.height)

    def compare(self, other):
        return (self.age == other.age and self.height == other.height and self.name == other.name)


c1 = Computer("Serhad", 23, 186)
c1.display()
c2 = Computer("Serhad", 23, 186)
c2.display()

# iki tane ayni consturctor u olan objenini adresleini degil desadece variablelerine göre compare edelim
if c1.compare(c2):
    print("equal")
else:
    print("not equal")

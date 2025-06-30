def add():
    print("result 1 is", __name__)


def sub():
    print("result 2 is")

def main():
    add()
    sub()

if __name__ == "__main__":
    main() # böyle yapmazsan bunu import ettgin zaman main fonksiyonu her zaman calisir 
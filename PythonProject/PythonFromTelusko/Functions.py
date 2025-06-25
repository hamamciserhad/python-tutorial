def greet():
    print("Hello")


greet()
greet()

# add ve sub fonks
# python da birden fazla deger dönebilir bi fonks

def add_sub(x,y):
    return x+y, x-y

print(add_sub(1,2))
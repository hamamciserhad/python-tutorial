def fibonacci(n):
    if n < 0:
        raise ValueError("Negatif sayı için Fibonacci tanımsızdır.")
    elif n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


x = int(input("Bir sayi girin: "))
for i in range(x):
    print(fibonacci(i))

y = int(input("Bir sayi girin: "))
print(fibonacci(y))

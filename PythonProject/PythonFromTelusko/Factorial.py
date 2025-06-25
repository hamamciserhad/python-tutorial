def factorial(n):
    if n < 0:
        raise ValueError("Negatif sayının faktöriyeli tanımsızdır.")
    elif n < 2:
        return 1
    else:
        return n * factorial(n - 1)

x = int(input("Bir sayi giriniz:"))
print(factorial(x))
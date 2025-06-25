a = 0
b = 0
try:
    print("Resource open")
    print(a / b)
except ZeroDivisionError as e:
    print(f"Bölme hatası: {e}")

try:
    k = int(input("Enter num:"))
    print(k)
except ValueError as e:
    print(f"Geçersiz sayı girdiniz: {e}")
finally:
    # bu blok exceptions alsak da almasak da calisir
    print("Resource closed")

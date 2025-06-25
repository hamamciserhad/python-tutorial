x = int(input("Enter a number: "))
if x % 2 == 0:
    print("cift ")  # ← bu satır girintili, if bloğunun içindedir, 4(standart tab kullan o da 4) atiyorum girintisi o zaman digerinin de girintsi 3 olmali blok icinde
    if x > 5 :
        print("great")
    else:
        print("not great")
elif x % 1 == 0:  # bu elif else if java daki, elif su üstteki if yanlissa calisir dogru ise direk atlanir
    print("tek ")

print("Bitti")  # ← bu satır artık if bloğunun dışındadır

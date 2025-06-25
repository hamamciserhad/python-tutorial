a = 5
b = 6
temp = a
a = b
b = temp

print(a)
print(b)
print(temp)


# bu isi temp kullanmadan da yapabiliriz

c = 3
d = 8

c = c + d
d = c - d
c = c - d

print(c)
print(d)


# daha kolayi da var python da

f = 8
g = 7
f,g = g,f
print(f)
print(g)
# File Handling Tutorial in Python

# Open 'MyData' file in read mode and read first 4 characters
with open("MyData", "r") as f:
    print(f.readline(4), end="")

# Open 'Abc' file in write+read mode
# Write "Laptop" to it and then read back from the beginning
with open("Abc", "w+") as f1:
    f1.write("Laptop")
    f1.seek(0)
    print(f1.read())

# Open 'Laptop' file in append+read mode
# Write "abd", move to beginning, and print contents
with open("Laptop", "a+") as f2:
    f2.write("abd")
    f2.seek(0)
    print(f2.read())

# Copy content from 'MyData' into 'Laptop'
with open("MyData", "r") as f_read, open("Laptop", "a") as f_write:
    for line in f_read:
        f_write.write(line)

# Binary file copy: copy an image to a new file
with open("Fotoğraf - 08.11.24 22.28.jpg", "rb") as image_in, open("new Pig.jpeg", "wb") as image_out:
    for chunk in image_in:
        image_out.write(chunk)
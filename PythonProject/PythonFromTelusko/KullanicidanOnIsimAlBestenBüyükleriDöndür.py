def count(lst):
    more = 0
    less = 0
    for x in range(len(lst)):
        if len(lst[x]) > 5:
            more += 1
        else:
            less += 1
    return (more, less)


lst = []
for i in range(10):
    name = input("Enter name {}:".format(i+1))
    lst.append(name)
more,less = count(lst)
print("Less than 5: {} and more than 5: {}".format(more, less))
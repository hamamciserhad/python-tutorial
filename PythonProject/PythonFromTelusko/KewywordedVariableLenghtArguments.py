def person(name, **data):
    print(name)
    for key, value in data.items():
        print(key, value)


person("Navin", age=23, city="Mumbai", mob=2343)
 
class Person:
    def __init__(self, name, age, het):
        self.name = name
        self.age = age

    def sayName(self):
        print("Hello my name is "+ self.name)


bim = Person("bim", "29", 123)
print(bim.name)
print(bim.sayName())

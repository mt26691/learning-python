class Person:
    def __init__(self, name, age):
        print("init function is called")
        self.name = name
        self.age = age

    def getName(self):
        print("Person name is "+self.name)


bim = Person("bim",28)
bim.getName()
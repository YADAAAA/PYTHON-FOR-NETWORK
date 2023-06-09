class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def PrintName(self):
        print("name :" , self.name , " age :", self.age)

class Student(Person):
        pass

myStudent = Student("yada", 20)
myStudent.PrintName()
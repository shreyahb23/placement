from abc import ABC, abstractmethod

# Abstract Class
class Person(ABC):

    def __init__(self, name, age):
        self.name = name      # Instance Variable
        self.age = age

    @abstractmethod
    def display(self):
        pass


# Inheritance
class Student(Person):

    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.__marks = marks      # Private Variable

    def get_marks(self):
        return self.__marks

    # Polymorphism
    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Roll No :", self.roll_no)
        print("Marks :", self.__marks)


class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # Polymorphism
    def display(self):
        print("\nTeacher Details")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Subject :", self.subject)


# Main Program
s1 = Student("Shreya", 20, 101, 95)
t1 = Teacher("Ravi", 35, "Python")

# Polymorphism
people = [s1, t1]

for person in people:
    person.display()
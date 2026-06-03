class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def introduce(self):
        return (f"hi i'm {self.name},"
                f" i am {self.age} "
                f"years old and my grade is {self.grade}.")
        
s1 = Student("Alice", 20, "A")
s2 = Student("Bob", 22, "B")
print(s1.introduce())

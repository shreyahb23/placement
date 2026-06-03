class Duck:
    def sound(self):
        print("Quack Quack!")

class cat:
    def sound(self):
        print("Meow Meow!")

class Person:
    def sound(self):
        print("Hello!")

def make_sound(obj):
    obj.sound()

make_sound(Duck())
make_sound(cat())
make_sound(Person())

print(len("Hello "))
print(len([1, 2, 3]))
print(3 + 5)
print("A" + "B")
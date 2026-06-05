stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.append(60)
print("Stack:", stack)

print("top element:", stack[-1])

popped = stack.pop()
print("Popped element:", popped)
print("Stack after pop:", stack)

print("Is empty:", len(stack) == 0)

#stack using class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")
print(s.peek())
print(s.pop())
print(s.peek())

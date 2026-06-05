# Find Second Largest Element

arr = [10, 20, 4, 45, 99, 99]

largest = second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest Element:", second_largest)

# Remove Duplicates while maintaining order

arr = [1, 2, 3, 2, 4, 1, 5]

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Unique Elements:", unique)

# Count occurrences of a target element

arr = [1, 2, 3, 2, 4, 2, 5]
target = 2

count = 0

for num in arr:
    if num == target:
        count += 1

print("Occurrences:", count)

# Count number of nodes in Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

count = 0
temp = head

while temp:
    count += 1
    temp = temp.next

print("Length of Linked List:", count)

# Reverse a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

prev = None
current = head

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

head = prev

print("Reversed Linked List:")

temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next

    # Reverse String using Stack

text = "Python"

stack = []

for ch in text:
    stack.append(ch)

reversed_string = ""

while stack:
    reversed_string += stack.pop()

print("Reversed String:", reversed_string)

# Check Balanced Brackets

expression = "{[()]}"

stack = []
pairs = {')': '(', '}': '{', ']': '['}

balanced = True

for ch in expression:
    if ch in "({[":
        stack.append(ch)

    elif ch in ")}]":
        if not stack or stack.pop() != pairs[ch]:
            balanced = False
            break

if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")

# 8. simulate
from collections import deque

# Create an empty queue
printer_queue = deque()

# Take number of print jobs from user
n = int(input("Enter number of print jobs: "))

# Add jobs to the queue
for i in range(n):
    job = input(f"Enter print job {i+1}: ")
    printer_queue.append(job)

print("\nProcessing Print Jobs:")

# Process jobs in FIFO order
while printer_queue:
    job = printer_queue.popleft()  # Remove from front
    print("Printing:", job)


# Find Middle Node using Slow and Fast Pointers

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print("Middle Element:", slow.data)


from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, data):
        self.q2.append(data)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1:
            return self.q1.popleft()

    def peek(self):
        if self.q1:
            return self.q1[0]

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top Element:", stack.peek())
print("Popped:", stack.pop())
print("Top After Pop:", stack.peek())
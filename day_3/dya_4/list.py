class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")    

    def insert_at_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head =new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node     

    def delete(self,key):
        current=self.head
        if current and current.data==key:
            self.head=current.next
            return
        prev=None
        while current and current.data!=key:
            prev=current
            current=current.next
        if current:
            prev.next=current.next   
    
ll=LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_front(5)
ll.traverse()
ll.delete(20)
ll.traverse()
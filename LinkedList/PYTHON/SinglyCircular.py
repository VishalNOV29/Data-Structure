class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertLast(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.head.next=self.head
            print("Inserted ",newNode.data)
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newNode
    def display(self):
        if self.head==None:
            print("Linked list is empty.")
        else:
            temp=self.head
            while temp!=self.head:
                print(temp.data,end="-> ")
                temp=temp.next

obj=LinkedList()
obj.insertLast(10)
obj.insertLast(20)
obj.insertLast(30)
obj.insertLast(40)
obj.insertLast(50)
obj.display()
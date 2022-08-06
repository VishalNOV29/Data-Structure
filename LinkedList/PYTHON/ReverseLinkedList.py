class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insertFirst(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="-> ")
            temp=temp.next
        print("Null")
    def reverse(self):
        newHead=self.head
        while newHead.next!=None:
            newHead=newHead.next
        currentNode=newHead
        while currentNode!=self.head:
            temp=self.head
            while temp.next!=currentNode:
                temp=temp.next
            currentNode.next=temp
            currentNode=temp
        self.head=newHead
        currentNode.next=None
obj1=LinkedList()
obj1.insertFirst(10)
obj1.insertFirst(20)
obj1.insertFirst(30)
obj1.insertFirst(40)
obj1.insertFirst(50)
obj1.display()
obj1.reverse()
obj1.display()
print(obj1.head.data)
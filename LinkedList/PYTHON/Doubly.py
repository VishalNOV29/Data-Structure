class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insertion(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def delete(self):
        if self.head==None:
            print("Linked list is empty.")
        else:
            self.head=self.head.next
    def insertLast(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            print("Inserted ",newNode.data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            newNode.prev=temp
            temp.next=newNode
            print("Inserted ",newNode.data)
    def deleteLast(self):
        if self.head==None:
            print("Linked list is empty.")
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            # new=temp.prev
            # new.next=None
            temp.prev.next=None
    def display(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="-> ")
                temp=temp.next
            print()
    def displayBackward(self):
        if self.head==None:
            print("Linked list is empty.")
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            currentNode=temp
            while currentNode!=self.head:
                print(currentNode.data,end="--> ")
                currentNode=currentNode.prev
            print(self.head.data)
obj=LinkedList()
obj.insertLast(10)
obj.insertLast(20)
obj.insertLast(30)
obj.insertLast(40)
obj.insertLast(50)
obj.insertLast(60)
obj.display()
obj.deleteLast()
obj.display()
obj.displayBackward()
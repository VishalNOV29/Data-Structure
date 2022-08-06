class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertFirst(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            print("Inserted ",newNode.data)
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
            print("Inserted ",newNode.data)
    def insertLast(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            print("Inserted ",newNode.data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp
            print("Inserted ",newNode.data)
    def display(self):
        temp=self.head.next
        while temp.next!=None:
            print("current value",temp.data)
            print("next value",temp.next.data)
            print("previous value",temp.prev.data)
            temp=temp.next
        

obj=LinkedList()
obj.insertLast(10)
obj.insertLast(11)
obj.insertLast(12)
obj.insertLast(13)
obj.display()

        
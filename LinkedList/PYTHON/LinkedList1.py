class Node:
    def __init__(self,data,):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insertLast(self,value):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    def view(self):
        temp=self.head
        while temp.next!=None:
            print(temp.data,end=" ")
            temp=temp.next
obj1=LinkedList()
obj1.insertLast(10)
obj1.insertLast(20)
obj1.insertLast(30)
obj1.insertLast(40)
obj1.view()
            

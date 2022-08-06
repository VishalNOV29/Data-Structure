''' Here push and pop operation will be performed on the tail of the linked list.
It will take more time than the one in which push and pop operation is performed on head of the linked list.'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class StakcUsingLinkedList:
    def __init__(self):
        self.head=None
        self.top=-1
    def push(self,item):
        newNode=Node(item)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            self.top=newNode
    def pop(self):
        temp=self.head
        while temp.next!=self.top:
            temp=temp.next
        self.top=temp
        
    def peak(self):
        return self.top.data

    def isEmpty(self):
        print(self.top==-1)

    def display(self):
        
        temp=self.head
        while True:
            if temp==self.top:
                break
            print(temp.data)
            temp=temp.next
obj=StakcUsingLinkedList()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.display()
obj.isEmpty()
# print(obj.peak())
obj.pop()
print("Displaying after using pop method.")
obj.display()


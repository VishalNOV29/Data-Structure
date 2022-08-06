''' Here I am going to implement the stack using singly linked list.
I have implemented this in anoter file but there is a difference in the both.
In this push and pop operation will on the head of a linked list that will take less time than the push and 
pop operation of the tail of the linked list.'''


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
        self.top=-1
    def push(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.top+=1
            print("Inserted ",newNode.data)
            print("First value",self.top)
            
        else:
            newNode.next=self.head
            self.head=newNode
            self.top+=1
            print("Inserted ",newNode.data)
            print("Second value",self.top)
    def pop():
        pass
obj=Stack()
obj.push(50)
obj.push(60)
obj.push(70)
obj.push(80)
print(obj.head.data)
print(obj.top)
        


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
    def enqueue(self,val):
        newNode=Node(val)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while (temp.next!=None):
                temp=temp.next
            temp.next=newNode
    def dequeue(self):
        item=self.head
        self.head=self.head.next
        return item.data
    def isEmpty(self):
        return self.head==None

appts=Queue()
appts.enqueue("John")
appts.enqueue("Annie")
appts.enqueue("Sandy")
print(appts.dequeue())
print(appts.dequeue())
print(appts.dequeue())
print(appts.isEmpty())

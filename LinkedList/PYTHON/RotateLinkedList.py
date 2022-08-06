from email import header


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            ptr1 = self.head
            while (ptr1.next != None):
                ptr1 = ptr1.next
            ptr1.next = newNode

    def display(self):
        ptr1 = self.head
        while (ptr1 != None):
            print(ptr1.data, end="->")
            ptr1 = ptr1.next
        print(None)

    def rotate(self, k):
        length = 1
        ptr1 = self.head
        while (ptr1.next != None):
            ptr1 = ptr1.next
            length += 1
        print(ptr1.data)
        print(length)
        k=k%length
        print(k)
        ptr1.next=self.head
        newHead=ptr1
        i=0
        while (i<k):
            


obj = LinkedList()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.display()
obj.rotate(8)

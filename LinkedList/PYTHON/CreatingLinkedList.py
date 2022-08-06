# from typing import NewType
from email import header


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertLast(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            print("Inserted ", item)

        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            print("Inserted ", item)

    def delLast(self):
        temp = self.head
        while (temp.next.next != None):
            temp = temp.next
        temp.next = None

    def insertFirst(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        print("Inserted ", item)

    def removeFirst(self):
        print("Removed ", self.head.data)
        self.head = self.head.next

    def view(self):
        temp = self.head
        while True:
            print(temp.data, end="->")
            if temp.next == None:
                break
            temp = temp.next
        print(None)

    def removeElement(self,head, val):
        if self.head == None:
            return self.head
        if self.head.data == val:
            return self.removeElement(self.head.next, val)
        self.head.next = self.removeElement(self.head.next, val)
        return self.head


obj = LinkedList()
obj.insertLast(10)
obj.insertLast(20)
obj.insertLast(30)
obj.insertLast(40)
obj.insertLast(50)
# obj.view()
# print("Linked list after adding 100 at head.")
# obj.insertFirst(100)
# obj.view()
# print("LinkedList after removing head.")
# obj.removeFirst()
obj.view()
# obj.delete(30)
# obj.view()
# obj.delete(50)
# obj.view()
# obj.delete(40)
# obj.view()
# # obj.delete(30)
# # obj.view()
# obj.delete(50)
# obj.view()
# obj.delLast()
# obj.view()
obj.removeElement(50)
obj.view()

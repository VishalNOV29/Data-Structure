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
            # print("Inserted ",item)

        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            # print("Inserted ",item)

    def insertFirst(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        # print("Inserted ",item)

    def removeFirst(self):
        # print("Removed ",self.head.data)
        self.head = self.head.next

    def view(self,head):
        temp = head
        while True:
            print(temp.data, end="->")
            if temp.next == None:
                break
            temp = temp.next
        print(None)
    # def recMerging(self,head1,head2):
    #     head=Node(None)
    #     temp=head
    #     if (head1.data<head2.data):
    #         temp.next=


obj = LinkedList()
obj.insertLast(10)
obj.insertLast(20)
obj.insertLast(30)
obj.insertLast(40)
obj.insertLast(60)
obj.view(obj.head)
obj2 = LinkedList()
obj2.insertLast(50)
obj2.insertLast(70)
obj2.insertLast(80)
obj2.insertLast(90)
obj2.insertLast(100)
obj2.view(obj2.head)
# print(mergeLinkedList(obj.head, obj2.head))
obj3=LinkedList()
head1=obj3.mergeLinkedList(obj.head,obj2.head)
print(head1.data)
obj3.view(head1)

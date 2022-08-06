class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp

    def show(self, head):
        temp = head
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
    def reverse(self,head):
        temp=head
        while temp.next!=None:
            temp=temp.next
        currentHead=temp
        while temp!=None:
            prevNode=temp.prev
            nextNode=temp.next
            temp.next=prevNode
            temp.prev=nextNode
            temp=prevNode
        return currentHead
    def rotate(self,head,num):
        for i in range(num):
            currentNode=head;
            head=head.next
            temp=head
            while temp.next!=None:
                temp=temp.next
            temp.next=currentNode
            currentNode.prev=temp   
        return head         




obj = LinkedList()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.show(obj.head)
obj.show(obj.reverse(obj.head))
obj.show(obj.rotate(obj.head,2))


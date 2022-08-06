class Stack:
    def __init__(self):
        self.top=-1
        self.stack=[]
    def push(self,data):
        self.top+=1
        self.stack.append(data)
    def pop(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            self.stack.pop()
            self.top-=1
    def display(self):
        temp=self.top
        while temp!=-1:
            print(self.stack[temp])
            temp-=1

obj=Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
# obj.display()
obj.pop()
obj.display()


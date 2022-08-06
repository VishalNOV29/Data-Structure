# In python we can define push and pop method by ourself because it has by default append and pop method that do the same
# work that we want. So in this program I have used the basic type. 

class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
        # self.capacity=capacity
    def push(self, item):
        self.top+=1
        self.stack.append(item)
    def pop(self):
        self.stack.pop()
        self.top-=1
    def peak(self):
        if self.top==-1:
            return "Stack is empty."
        else:
            return self.stack[self.top]
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def view(self):
        while self.top>-1:
            print(self.stack[self.top])
            self.top-=1

obj=Stack()
obj.push(20)
print(obj.isEmpty())
print(obj.stack)
print(obj.top)
print(obj.peak())


            

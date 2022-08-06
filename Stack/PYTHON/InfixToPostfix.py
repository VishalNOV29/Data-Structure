class Stack:
    def __init__(self):
        self.stack = []
        self.topPointer = -1

    def push(self, ele):
        self.topPointer += 1
        self.stack.append(ele)

    def pop(self):
        self.topPointer -= 1
        return self.stack.pop()

    def show(self):
        temp = self.topPointer
        print("temp =", temp)
        while temp != -1:
            print(self.stack[temp], temp)
            temp -= 1

    def peak(self):
        return self.stack[self.topPointer]

    def isEmpty(self):
        return self.topPointer == -1

# Conversion form infix to postfix. After reversing this expression we will got prefix expression.
def infixToPostfix(exp):
    operators = ["-", "+", "*", "/"]
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    expression = ""
    obj = Stack()
    for ele in exp:
        if ele == "(":
            obj.push(ele)
        elif ele == ")":
            while obj.peak() != "(":
                expression += obj.pop()
            obj.pop()
        elif ele in operators:
            if obj.isEmpty:
                obj.push(ele)
            elif obj.peak() in operators:
                if precedence[ele] > precedence[obj.topPointer] or obj.isEmpty():
                    obj.stack.push(ele)
                else:
                    while precedence[ele] != precedence[obj.topPointer] or precedence[ele] > precedence[obj.topPointer]:
                        expression += obj.pop()
            else:
                obj.push(ele)
        else:
            expression += ele
    while obj.topPointer != -1:
        expression += obj.pop()
    return expression

# Evaluation a postfix expression.
def evalPostfiex(exp):
    exp=infixToPostfix(exp)
    print(exp)
    obj=Stack()
    operators=["+","-","/","*"]
    for ele in exp:
        if ele not in operators:
            obj.push(ele)
        else:
            second_operand=obj.pop()
            first_operand=obj.pop()
            result=None
            if ele =="+":
                result=int(first_operand)+int(second_operand)
                print("result",result)
            elif ele=="-":
                result=int(first_operand)-int(second_operand)
                print("result",result)
            elif ele=="*":
                result=int(first_operand)*int(second_operand)
                print("result",result)
            else:
                result=int(first_operand)*int(second_operand)
                print("result",result)
            obj.push(result)
            print("stack",obj.stack)
    return obj.pop()
    
print(evalPostfiex("(2+3)*(5-9)"))

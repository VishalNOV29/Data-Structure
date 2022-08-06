# def Sum(num):
#     if num==1:
#         return "hello"
#     else:
#         return num+Sum(num-1)
# print(Sum(10))

def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
print(power(2,3))
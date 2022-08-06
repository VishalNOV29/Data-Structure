# n=int(input("Enter the numebr to find factorial"))
def fact(n):
    if n==0:
        print("Entering in the if condition.")
        return
    else:
        print("Entering in the else codition.")
        return n+fact(n-1)
    print("Final exiting this function.")
print(fact(5))

# def count(n):
#     total=10
#     if n==0:
#         return "completed"
#     else:
#         total+=n
#         print(total)
#         return count(n-1)
# print(count(10))
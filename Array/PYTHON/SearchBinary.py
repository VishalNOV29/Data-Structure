list_len=int(input("How many numbers you want in the list."))
list1=[int(input()) for i in range(list_len)]
item=int(input("Enter the number which you want to find"))
list1.sort()
print("Sorted list is",list1)
lb=0
ub=len(list1)-1
mid=(lb+ub)//2
low=lb
high=ub
while low<=high:
    if list1[mid]==item:
        print("Item found at index ",mid)
        break
    else:
        if list1[mid]>item:
            high=high-1
        else:
            low=low+1
    mid=(low+high)//2
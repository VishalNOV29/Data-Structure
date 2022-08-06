list1=[9,8,7,6,5,4,3,2,1,0]
list1.insert(0,-100)
lb=2
ub=len(list1)-1
for i in range(lb,ub):
    print("Entering outer loop.")
    k=i
    for j in range(k,0,-1):
        print("Entering inner loop.")
        if list1[j]>list1[i]:
            print("Condition matched.")
            x=list1[i]
            y=list1[j]
            list1[i]=y
            list1[j]=x
list1.pop(0)
print(list1)
# Description-- In this method we generally select the smallest element and swap it with firt index,
# and this process continue till the array get sorted.

# -------------- Using For Loop-------------------------
list1=[5,4,3,2,1,23,54,6,8,90,23,54,66]
lb=0
ub=len(list1)-1
for i in range(lb,ub):
    ele=list1[i]
    k=i
    for j in range(k,ub+1):
        if list1[j]<list1[i]:
            x=list1[i]
            y=list1[j]
            list1[i]=y
            list1[j]=x
print(list1)

# Using while loop-----------------------

list1=[5,4,3,2,1]
lb=0
ub=len(list1)-1
i=0
while i<=ub-1:
    ele=list1[i] 
    j=i
    while j<=ub:
        if list1[j]<list1[i]:
            x=list1[i]
            y=list1[j]
            list1[i]=y
            list1[j]=x
        j+=1
    i+=1
print(list1)
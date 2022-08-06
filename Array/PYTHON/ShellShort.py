# def shellShort(arr):
#     gap=len(arr)//2
#     for j in range(gap,)
# import numpy as nd
n1=int(input())
for i in range(n1):
    n_m=list(map(int,input().strip().split()))
    n=n_m[0]
    m=n_m[1]
    arr=[]
    max1=0
    for j in range(n):
        tempArr=list(input().strip().split())
        arr.append(tempArr)
    
    for ele in arr:
        tempMax=0
        for k in range(len(ele)):
            if ele[k]=="#":
                tempMax+=1
            else:
                if max1<tempMax:
                    max1=tempMax
                    tempMax=0
                else:
                    tempMax=0
        if tempMax>max1:
            max1=tempMax
        
    print(max1)


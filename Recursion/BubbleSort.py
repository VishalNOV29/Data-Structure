list1=[1,2,4,3,5,6,7,6,7]
def bubbleSort(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):
            if list1[j]>list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1
print(bubbleSort(list1))

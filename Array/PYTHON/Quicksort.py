#Function for swapping value in the array.
def swap(list1,i,j):

    # print("swap method is being called.")
    num1=list1[i]
    # print(f"i ={i} , arr[i] = {num1}")
    num2=list1[j]
    # print(f"j = {j}, arr[j] = {num2}")
    list1[i]=num2
    list1[j]=num1

def partition(arr,low,high):
    # print("Partition is called.")
    pivot=arr[low] # Considering the first element as a pivot.
    i=low
    j=high # Assigning the value of low and high to i and j.
    # This loop will run until the i will be less than j.
    # This shows that there are atleast two elemets in the array.
    # If i will be equal to j then only element will be left in the array and at that time the array will be sorted.
    while (i<j):
        # Now we have to increase the value of i until we didn't get a higher element than the pivot.
        while (arr[i]<=pivot):
            i+=1
        # Now we have to increase the value of j until we didn't get a lower element than the pivot.
        while (arr[j]>pivot):
            j-=1
        # if i will be less than j it means the array is not fully traversed.
        # Now we will swap the higher element and lower element.
        if (i<j):
            swap(arr,i,j)
    '''This code will run when the value of i will be higher than the value of j.
     It means the list is fully traversed and now we will swap the value of pivot and j.
     Now the element at j is it's original element all the elements left of j will be smaller than j
     right of j will be greater than j.'''
    swap(arr,low,j)
    ''' After swapping this function will return the value of j becaue we have to now divide the array
    from the j in two parts the first one will be of left side and the another will be of right side.
    '''
    # print("j =",j)
    return j 

def quicksort(arr,low,high):
    # print("Quick sort is called.")
    if (low<high):
        fixed_element_index=partition(arr,low,high)
        quicksort(arr,low,fixed_element_index-1)
        quicksort(arr,fixed_element_index+1,high)
    return arr
# arr=[4,4,6,2,5,7,9,1,3]
arr=[9,8,7,6,5,4,3,2,1,0]
print(quicksort(arr,0,len(arr)-1))
# quicksort(arr,0,len(arr)-1)
# print(arr)

    
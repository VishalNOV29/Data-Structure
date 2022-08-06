from turtle import left, right
from cv2 import merge



def mergeArr(arr,low,mid,high):
    # step1- first find the lenght of left part and right part.
    left_len=mid-low+1
    
    right_len=high-mid

    # step2 - now declare two array (left and right part of the parent array.)
    left_arr=arr[low:mid+1]
    right_arr=arr[mid+1:high+1]
   

    # step3 - Start merging left and right array.

    i=j=0 # pointer indicating the first element of the right and left array.
    k=low # pointer indicating the begining of the array that has to be sorted.

    # this loop will continue until the one of the array (either left or right) won't be completely emtpy.
    while (i<left_len and j<right_len):
        if left_arr[i]<right_arr[j]:
            arr[k]=left_arr[i]
            i+=1
            k+=1
        elif (left_arr[i]>right_arr[j]):
            arr[k]=right_arr[j]
            j+=1
            k+=1
    
    # This loop will copies all the elements of left array to main array.
    while (i<left_len):
        arr[k]=left_arr[i]
        i+=1
        k+=1
    
    # This loop will copies all the elements of right array ot main array.
    while (j<right_len):
        arr[k]=right_arr[j]
        j+=1
        k+=1





def mergeSort(arr,low,high):
    if (low<high):

        mid=(low+high)//2
        mergeSort(arr,low,mid) # calling mergesort for the left part.
        mergeSort(arr,mid+1,high)  # calling mergesort for the right part.
        mergeArr(arr,low,mid,high) # finally merging both the array.


arr=[0,9,8,7,6,5,4,3,2,1]
print(arr)
mergeSort(arr,0,9)
print(arr)
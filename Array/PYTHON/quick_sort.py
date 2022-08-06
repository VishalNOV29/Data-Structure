# def swap(arr,i,j):
#     num1=arr[i]
#     num2=arr[j]
#     arr[i]=num2
#     arr[j]=num1
# def partition(arr,low,high):
#     pivot=arr[low]
#     i=low
#     j=high
#     while (i<j):
#         while (arr[i]<=pivot):
#             i+=1
#         while (arr[j]>pivot):
#             j-=1
#         if (i<j):
#             swap(arr,i,j)
#     swap(arr,low,j)
#     return j
# def quicksort(arr,low,high):
#     if (low<high):
#         fixed_element_index=partition(arr,low,high)
#         quicksort(arr,low,fixed_element_index-1)
#         quicksort(arr,fixed_element_index+1,high)
#     return arr
# arr=[1,3,4,5,9,7,10]
# print("Unsorted array: ",arr)
# sorted_arr=quicksort(arr,0,len(arr)-1)
# print("Sorted array: ",sorted_arr)

# from winreg import QueryInfoKey


# def swap(arr,i,j):
#     num1=arr[i]
#     num2=arr[j]
#     arr[i]=num2
#     arr[j]=num1
# def partition(arr,low,high):
#     pivot=arr[low]
#     i=low
#     j=high
#     while (i<j):
#         while (arr[i]<=pivot):
#             i+=1
#         while (arr[j]>pivot):
#             j-=1
#         if (i<j):
#             swap(arr,i,j)
#     swap(arr,low,j)
#     return j
# def quicksort(arr,low,high,k):
#     print("This method is called.")
#     j=partition(arr,low,high)
#     print("j =",j)
#     print("k =",k)
#     if j==k-1:
#         print("Condition satisfied.")
#         return arr[j]
#     elif j>k:
#         print("Condition2")
#         return partition(arr,low,j-1)
#     elif j<k:
#         print("condition3")
#         return partition(arr,j+1,high)
    
# arr=[1,3,4,5,9,7,10]
# # print("Unsorted array: ",arr)
# # sorted_arr=quicksort(arr,0,len(arr)-1)
# # print("Sorted array: ",sorted_arr)
# result=quicksort(arr,0,len(arr)-1,5)
# print(result)
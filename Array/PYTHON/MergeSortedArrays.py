# from statistics import median_grouped


# def mergeArrays(arr1,arr2,n1,n2):
#     i=0;j=0;k=0
#     arr3=[None]*(n1+n2)
#     # After termination of this loop one of the arr will be completely inserted in the sorted array.
#     while i<n1 and j<n2:
#         if arr1[i]<arr2[j]:
#             arr3[k]=arr1[i]
#             k+=1
#             i+=1
#         else:
#             arr3[k]=arr2[j]
#             k+=1
#             j+=1
#     print(i,j,k)

#     # At a time only one loop of the two will be executed.

#     # Loop 1.
#     # This loop will run only when all the elements of arr2 will be inserted in the sorted array.
#     while i<n1:
#         print("First loop is being called")
#         arr3[k]=arr1[i]
#         k+=1
#         i+=1

#     # Loop 2.
#     # This loop will run only when all the elements of arr1 will be inserted in the sorted array.
#     while j<n2:
#         print("SEcond loop is being called.")
#         arr3[k]=arr2[j]
#         j+=1
#         k+=1
#     return arr3
# arr1=[1,2,3,7,8,9]
# arr2=[4,5,6,10,11,12]
# print(mergeArrays(arr1,arr2,len(arr1),len(arr2)))


# def mergeSort(arr):
# 	if len(arr) > 1:
# 		# Finding the mid of the array
# 		mid = len(arr)//2
# 		# Dividing the array elements
# 		L = arr[:mid]
#         print(L)
# 		# into 2 halves
# 		R = arr[mid:]
#         print(R)

# 		# Sorting the first half
# 		mergeSort(L)

# 		# Sorting the second half
# 		mergeSort(R)

# 		i = j = k = 0

# 		# Copy data to temp arrays L[] and R[]
# 		while i < len(L) and j < len(R):
# 			if L[i] < R[j]:
# 				arr[k] = L[i]
# 				i += 1
# 			else:
# 				arr[k] = R[j]
# 				j += 1
# 			k += 1

# 		# Checking if any element was left
# 		while i < len(L):
# 			arr[k] = L[i]
# 			i += 1
# 			k += 1

# 		while j < len(R):
# 			arr[k] = R[j]
# 			j += 1
# 			k += 1

# def printList(arr):
# 	for i in range(len(arr)):
# 		print(arr[i], end=" ")
# 	print()
# arr=[5,4,3,2,1]
# print(arr)
# # print(mergeSort(arr))
# mergeSort(arr)
# print(arr)

# array = [4, 2, 3, 8, 8, 43, 6, 1, 0]
# print("Unosrted array",array)

# def merge_sort(array):
#     ret = []
#     if(len(array) == 1):
#         return array
#     half = len(array) // 2
#     left = array[:half]
#     print("left =", left)
#     lower = merge_sort(left)
#     right = array[half:]
#     print("right =", right)
#     upper = merge_sort(right)

#     lower_len = len(lower)
#     upper_len = len(upper)
#     i = 0
#     j = 0
#     while i != lower_len or j != upper_len:
#         if(i != lower_len and (j == upper_len or lower[i] < upper[j])):
#             ret.append(lower[i])
#             i += 1
#         else:
#             ret.append(upper[j])
#             j += 1
#     return ret

# ar = merge_sort(array)
# print("Sorted array: ",ar)
# def merge(arr,mid):
#     n1=len(arr[:mid])
#     n2=len(arr[mid+1:])
    
#     i=j=k=0
#     while i<n1 and j<n2:
#         if arr[i]<arr[j]:
#             # newArr[k]=arr1[i]
#             arr[k]=arr[i]
#             i+=1
#             k+=1
#         else:
#             # newArr[k]=arr2[j]
#             arr[k]=arr[j]
#             j+=1
#             k+=1
#     while i<n1:
#         # newArr[k]=arr1[i]
#         arr[k]=arr[i]
#         i+=1
#         k+=1
#     while j<n2:
#         # newArr[k]=arr2[j]
#         arr[k]=arr[j]
#         j+=1
#         k+=1
# # print(merge([1,3,5,7],[2,4,6,8]))
# # merge()
# arr=[1,3,5,7,2,4,6,8]
# merge(arr,3)
# print(arr)

def mergeSort(arr):
    if len(arr)>1:
        mid =len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i=j=k=0
        while len(left)>i and len(right)>j:
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
                
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while len(left)>i:
            arr[k]=left[i]
            i+=1
            k+=1
        while len(right)>j:
            arr[k]=right[j]
            j+=1
            k+=1

arr=[9,8,7,6,5,4,3,2,1]
mergeSort(arr)
print(arr)
        



# MergeSort in Python


# def mergeSort(array):
#     if len(array) > 1:

       
#         r = len(array)//2
#         L = array[:r]
#         M = array[r:]

#         # Sort the two halves
#         mergeSort(L)
#         mergeSort(M)

#         i = j = k = 0
#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 array[k] = L[i]
#                 i += 1
#             else:
#                 array[k] = M[j]
#                 j += 1
#             k += 1

#         # When we run out of elements in either L or M,
#         # pick up the remaining elements and put in A[p..r]
#         while i < len(L):
#             array[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(M):
#             array[k] = M[j]
#             j += 1
#             k += 1


# arr=[9,8,7,6,5,4,3,2,1]
# mergeSort(arr)
# print(arr)
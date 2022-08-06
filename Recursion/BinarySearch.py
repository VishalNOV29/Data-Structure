def binarySearch(arr,low,high,ele):
    if low>high:
        return 'element not found'
    else:
        mid=(low+high)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]<ele:
            return binarySearch(arr,mid+1,high,ele)
        elif arr[mid]>ele:
            return binarySearch(arr,low,mid-1,ele)
arr=[1,2,3,4,5]
ele=4
print(binarySearch(arr,0,len(arr)-1,ele))
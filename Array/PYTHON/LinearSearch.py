# Description - In this method we generally search an element in a array and find its index.
# Searching is done in such a way that we go through each element and check that it is equal to desired element or not.

list1=[1,2,3,4,5,6,7,8,9,0]
ele=5
k=None
for i in range(len(list1)):
    if list1[i]==ele:
        k=i
if k==None:
    print("Element doesn't found in the list.")
else:
    print("Element found at index",k)
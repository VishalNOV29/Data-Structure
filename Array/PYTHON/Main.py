# Searching in python array.
# 1.Linear Search.
# arr=[1,2,3,4,5,6,7,87]
# arr=list(map(int,input("Enter elements separated by space.").split()))
# ele=int(input("Enter elemet for searching."))
# index=None
# for i in range(len(arr)):
#     if arr[i]==ele:
#         index=i
#         break
# if index!=None:
#     print("Element found at index ",index)
# else:
#     print("Element doesn't found in tha array.")


# 2.Binary Search.

# def binarySearch(arr,low,high,ele):
#     mid=(low+high)//2
#     while low<=high:
#         if ele==arr[mid]:
#             return mid
#         elif ele<arr[mid]:
#             return binarySearch(arr,low,mid-1,ele)
#         else:
#             return binarySearch(arr,mid+1,high,ele)
#     return None


# ele=int(input("Enter the element to search."))
# arr=[1,2,3,4,5,6,7,8]
# print(binarySearch(arr,0,len(arr)-1,ele))

# Now we are going to discuss the sorting techniques in python.
# 1.Selection Sort in python.
# list1=[9,8,7]
# arr=[9,8,7]
# for i in range(len(arr)-1):
#     minimum=arr[i]
#     for j in range(i,len(arr)):
#         print("Entering second loop.",j)
#         if arr[j]<minimum:

# print(arr)

# lb=0
# ub=len(list1)-1
# for i in range(lb,ub):
#     ele=list1[i]
#     for j in range(i,ub+1):
#         if list1[j]<ele:
#             x=list1[i]
#             y=list1[j]
#             list1[i]=y
#             list1[j]=x
# print(list1)

# for i in range(len(arr)-1):
#     minimum=arr[i]
#     for j in range(i,len(arr)):
#         if arr[j]<minimum:
#             x=arr[i]
#             y=arr[j]
#             arr[i]=y
#             arr[j]=x
# print(arr)

# arr=[5,4,3,2,1]
# for i in range(len(arr)):
#     print("First loop.")
#     minimum=arr[i]
#     print("minimum1 =",minimum)
#     ind=None
#     for j in range(i+1,len(arr)):
#         print("Second loop.")
#         if arr[j]<minimum:
#             ind=j
#             minimum=arr[j]
#             print("minimum2 =",minimum)
#     print("final minimum",minimum)
#     print(f"a[j]= {arr[ind]} , arr[i] = {arr[i]}")
#     arr[ind]=arr[i]
#     print(f"a[j]= {arr[ind]}")
#     arr[i]=minimum
#     print(f"a[i]= {arr[i]}")
#     print(arr)
# print(arr)

# arr=[4,3,2]
# ind=0
# for i in range(len(arr)):
#     Min=arr[i]
#     print("First min =",Min)
#     for j in range(i,len(arr)):
#         if arr[j]<Min:
#             print(f"a[{j}]<{Min}")
#             Min=arr[j]
#             ind=j
#             print("ind =",ind)
#             print("SEcond min =",Min)
#     print("Updated min =",Min)
#     arr[ind]=arr[i]
#     arr[i]=Min
#     print("Updated arr =",arr)
# print(arr)


# Bubble Sort. I am going to write a very efficient bubble sort algorithm.
# arr=[5,4,3,2,1]
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1):
#         if arr[j]>arr[j+1]:
#             x=arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=x
# print(arr)


# Insertion sort.
# arr=[5,4,3,2,1]
# for i in range(1,len(arr)):
#     ele=arr[i]
#     for j in range(i,0,-1):
#         if arr[j-1]>arr[j]:
#             x=arr[j]
#             arr[j]=arr[j-1]
#             arr[j-1]=x
# print(arr)


# print(1<<1)
# num=12
# sh=1
# # print(num&sh)
# count=0
# while True:
#     print("Entering while loop.")
#     num=num&sh
#     if num==sh:
#         break
#     sh=sh*2
#     count+=1

# print(count)


# print(12&2)
# print(12&4)

# num=12
# sh=1
# count=0
# while True:
#     num=num&sh
#     if num==sh:
#         break
#     sh=sh<<1
#     count+=1
# print(count)

# from asyncio import new_event_loop


# arr=[1,2,3,4,5,4,3,2,1,6]
# res=0
# for ele in arr:
#     res=res^ele
# print(res)
# mask=1
# while True:
#     if (res&mask)!=0:
#         break
#     mask=mask<<1
#     print(res&mask)
# print("mask =",mask)
# list_0=[]
# list_1=[]
# for ele in arr:
#     if mask&ele==0:
#         list_0.append(ele)
#     else:
#         list_1.append(ele)

# print("list_0 =",list_0)
# print("list_1 =",list_1)
# new_res=res
# for ele in list_0:
#     new_res=new_res^ele
# # new_res=res^new_res
# print("a =",new_res)
# print("b =",new_res^res)

# number="1111"
# naem
# print(int(number,2))
# string=input("Enter the string: ")
# result=""
# for i in range(len(string)):
#     if string[i] in "0123456789":
#         result+=string[i]
# print(result)
# # print(string.isnumeric())

# class Hotel:
#     def __init__(self):
#         print(f"{'*'*8}Welcome!{'*'*8}")
#         self.dict = {
#             1: ["BOILED EGG", 40.00],
#             2: ["CORNFLEX WITH HOT MILK", 40.00],
#             3: ["BREAD AND MILK", 110.00],
#             4: ["RICE AND CURRY", 150.00],
#             5: ["CHICKEN RICE", 200.00],
#             6: ["BREAD AND VEGETABLE", 120.00],
#             7: ["CHICKEN TIKI", 350.00],
#             8: ["TANDORI ROTI", 200.00],
#             9: ["MILKSAKE", 100.00]
#         }

#     # Method to order food.
#     def orderFood(self):
#         self.order_list = []

#         print('''
# BREAKFAST:-
# 1. BOILED EGG                    40.00
# 2. CORNFLEX WITH HOT MILK        40.00
# 3. BREAD AND MILK                110.00

# LUNCH:-
# 4.RICE AND CURRY                 150.00
# 5.CHICKEN RICE                   200.00
# 6.BREAD AND VEGeTABLE            120.00

# DINNER:-
# 7.CHICKEN TIKK                   350.00
# 8.TANDORI ROTI                   200.00
# 9.MILKSAKE                       100.00''')
#         while True:
#             print()
#             user_choice = int(input("Choose a item number to order: "))
#             self.order_list.append(user_choice)
#             y_n = input("Would you like to add more item? (Y/N) : ")
#             if y_n == "y" or y_n == "y":
#                 continue
#             else:
#                 break
#         self.total_amount = 0
#         print()
#         for ele in self.order_list:
#             self.total_amount += self.dict[ele][1]
#             print(f"{self.dict[ele][0]}         {self.dict[ele][1]}")
#         print("TOTAL :", self.total_amount)
#         print("YOUR ORDER HAVE BEEN PLACED")
#         print()

#     # method to show order.
#     def showOrder(self):
#         total_amount = 0
#         print("YOUR ORDER:-")
#         for ele in self.order_list:
#             total_amount += self.dict[ele][1]
#             print(f"{self.dict[ele][0]}         {self.dict[ele][1]}")
#         print("TOTAL :", total_amount)


# obj = Hotel()
# obj.orderFood()
# obj.showOrder()

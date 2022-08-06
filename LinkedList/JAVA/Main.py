# string="0123"
# print(int(string))
# import calendar
# # date=input("Enter the date: ")
# # Python program to display calendar of
# # given month of the year

# # import module
# import calendar

# yy = 2022
# mm = 3
# date=21

# # display the calendar
# print(calendar.day_name(yy, mm,date))

# from datetime import date
# import calendar
# curr_date = date.today()
# # print(calendar.day_name[curr_date.weekday()])
# import pandas as pd
# today_date=input("Enter date separated by dash: ")
# temp = pd.Timestamp(today_date)
# print(temp.month_name())

# def myFun():
#     print("I am a function.")

# print((27*34)%8)
# print((39+84)%7)
# list1=list(map(int,input("Enter elements separated by space: ").strip().split()))
# def max_two(arr):
#     arr.sort()
#     return [arr[-1],arr[-2]]

# print(max_two(list1))

# num_categories=int(input("Enter how many categories"))
# from random import weibullvariate


# class Main:
#     def __init__(self):
#         self.cat_weight = []
#         self.cat_grades = []
#         self.percentage = 0

#     def myFun(self):
#         num_categories = int(input("How many categories? "))
#         for numbers in range(num_categories):
#             print("For category", numbers+1)
#             weight = int(input("Enter Weight "))
#             self.cat_weight.append(weight)
#             grades = int(input("Enter Grades "))
#             self.cat_grades.append(grades)
#         if sum(self.cat_weight) == 100:
#             for numbers in range(num_categories):
#                 self.percentage += (self.cat_weight[numbers] /
#                                     100)*self.cat_grades[numbers]
#             print(f"Your score is {self.percentage:.2f}")
#             if self.percentage >= 94:
#                 print("You earned an A, keep up the great work!")
#             elif (90 <= self.percentage):
#                 print("You earned an A-, keep up the great work!")
#             elif (87 <= self.percentage):
#                 print("You earned B+, still room for improvement!")
#             elif (84 <= self.percentage):
#                 print("You earned B, still room for improvement!")
#             elif (80 <= self.percentage):
#                 print("You earned B-, still room for improvement!")
#             elif (77 <= self.percentage):
#                 print("You earned C+, so close to a B!")
#             elif (74 <= self.percentage):
#                 print("You earned C, keep working, you can do it!")
#             elif (70 <= self.percentage):
#                 print("You earned C-, keep working you can do it!")
#             elif (67 <= self.percentage):
#                 print("You earned D+, You can do better.")
#             elif (64 <= self.percentage):
#                 print("You earned D, You can do better.")
#             else:
#                 print("Your grade is F, you can do better")
#         else:
#             print("Error:Weights don't add up to 100%")
# obj=Main()
# obj.myFun()

# growth_rates = [1.03, 1.9, 1.36, 1.23, 1.08, 1.12, 1.55, 1.06, 1.05, 0.92]
# mult = 1
# for ele in growth_rates:
#     mult *= ele

# mult = mult**.5

# geo_mean = round(mult, 2)

# print("geo_mean=", geo_mean)

# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.to_string())


# from nltk.tokenize import word_tokenize
# my_list= [{'Sam Collins' : 3},{'Sarah Smith' : 2},{'Ben Hawkins' : 8}]
# new_list=[]
# for ele in my_list:
#     for key in ele:
#         data=word_tokenize(key)
#         for value in data:
#             my_list=[value,ele[key]]
#             new_list.append(my_list)
# print(new_list)

# list1=[]
# boat_count=0
# while len(list1)>0:
#     if len(list1)==1:
#         list1.pop)

# arr1=[1,2,3,4]
# arr2=[0,3,4,5,6,7,8]
# def myFun(arr1,arr2):
#     res=[None]*(len(arr1)+len(arr2))
#     i=j=k=0
#     while i<len(arr1) and j<len(arr2):
#         print(res)
#         print("i =",i,"j =",j)
#         if arr1[i]<arr2[j]:
#             print("Condition 1")
#             print("inner i =",i,"j =",j,'k =',k)
#             print("arr1[i] =",arr1[i])
#             res[k]=arr1[i]
#             i+=1
#         else:
#             print("Condition 2")
#             res[k]=arr2[j]
#             j+=1
#         k+=1
#     while i<len(arr1):
#         res[k]=arr1[i]
#         i+=1
#         k+=1
#     while j<len(arr2):
#         res[k]=arr2[j]
#         j+=1
#         k+=1
#     return res
# obj=myFun(arr1,arr2)
# print(obj)


# arr=[[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
# arr=[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# minSum=0
# arr=[]
# for ele in arr:
#     num=min(ele)
#     if num not in arr:
#        minSum+=num
#        arr.append(num)
#     else:
#         minSum+=max(ele)
#         arr.append(max(ele))
# print(minSum)

# def hello(num):
#     if num>1 and num<10:
#         print(num)
#         # hello(num-1)
#         # return hello(num-1)
#         hello(num-1)
#         print("First functio execution is completed.")
#         hello(num+1),
#     return ("Finally this will be returned")
# hello(5)

# def mergeSort(arr):
#     if len(arr)>1:
#         print("arr =",arr)
#         mid=len(arr)//2
#         L=arr[0:mid]
#         print("L =",L)
#         R=arr[mid:]
#         print("R =",R)
#         print(f"mergeSort({L})")
#         mergeSort(L)
#         # print("Now moves to right part.",L+R,"->",R)
#         print(f"mergeSort({R})")
#         mergeSort(R)
#         # print("Execution is completed.")
# print(f"mergeSort({[1,2,3,4,5,6]})")
# mergeSort([1,2,3,4,5,6])


# sd1={'name':'John','grade':[90,84,64]}
# sd2={'name':'Sarah','grade':[73,80,63]}
# sd3={'name':'Lara','grade':[95,72,83]}
# sd4 = []
# sd4.append(sd1)
# sd4.append(sd2)
# sd4.append(sd3)

# for s in sd4:
#     pass_grade=[]
#     for grade in s['grade']:
#         if grade>=65:
#             pass_grade.append(grade)
#     average=sum(pass_grade)/len(pass_grade)
#     print(f"{s['name']} {' '.join([str(x) for x in pass_grade])} - Avg = {'{:.2f}'.format(average)}",end="\n \n")

# string=input("Enter the string: ")
# def reverseStr(string):
#     if len(string)==0:
#         print("base case reached.")
#         return
#     print("method is called",string)
#     temp=string[0]
#     reverseStr(string[1:])
#     print(temp,end="")
# reverseStr(string)

# string=input('Enter the string: ')
# def showStr(string):
#     if len(string)==0:
#         return
#     temp=string[-1]
#     showStr(string[:len(string)-1])
#     print(temp,end="")
# showStr(string)


# def displayResult():
#     arr = [15, 70, 16, 90, 35, 45, 52, 63]
#     elementToInsert = [60, 85, 74]

#     newArr = []
#     i = 0
#     while i < len(arr):
#         if i == 2:
#             for ele in elementToInsert:
#                 newArr.append(ele)
#                 continue
#         print("i =", i)
#         newArr.append(arr[i])
#         i += 1
#     print(newArr)


# displayResult()

# import numpy
# import pyame


# Binary Search.
# arr=[1,2,3,4,5,6,7,8]
# arr.sort()
# def binarySearch(arr,target,low,high):
#     print("Function is called.")
#     print("low =",low)
#     print("high =",high)
#     mid=(low+high)//2
#     if (low>high):
#         print("low =",low)
#         print("high =",high)
#         return -1
#     else:
#         if (arr[mid]==target):
#             print("Condition 1")
#             print("mid =",mid)
#             return mid
#         elif arr[mid]>target:
#             print("Condition 2")
#             high=mid-1
#             print("mid =",mid)
#             return binarySearch(arr,target,low,high)
#         else:
#             print("Condition 3")
#             low=mid+1
#             print("mid =",mid)
#             return binarySearch(arr,target,low,high)
# print(binarySearch(arr,9,0,len(arr)-1))


# Find peak of an element.
# def findPeak(arr,low,high):
#     mid=(low+high)//2
#     if (low>high):
#         return arr[mid]
#     else:
#         mid=(low+high)//2
#         if arr[mid-1]<arr[mid]>arr[mid+1]:
#             return mid
#         elif arr[mid-1]<arr[mid]<arr[mid+1]:
#             print("condition 1")
#             low=mid+1
#             return findPeak(arr,low,high)
#         else: #(arr[mid-1]>arr[mid]>arr[mid+1])
#             print("condition 2")
#             high=mid-1
#             return findPeak(arr,low,high)
# arr=[1]
# print(findPeak(arr,0,len(arr)-1))


# import random
# char = "0123456789"
# char_list = list(char)
# password = input("Enter your password: ")
# guess_password = ""
# while (guess_password != password):
#     guess_password = random.choices(char_list, k=len(password))
#     print("<=========================="+str(guess_password) +
#           "=============================>")
#     if guess_password == list(password):
#         print("Your password is:"+''.join(guess_password))
#         break


# import random
# char = "abcdefghijklmnopqrstuvwxyz"
# char_list = list(char)
# password = input("Enter your password: ")
# guess_password = ""
# while guess_password != password:
#     guess_password = random.choices(char, k=len(password))
#     print("<=========================="+str(guess_password) +
#           "=============================>")
#     if guess_password==list(password):
#         print("Your password is:",''.join(guess_password))
#         break

# from fileinput import filename


# def main():
#     fielname=input("Enter file name: ")
#     total,count=0,0
#     with open(filename,'r') as f:
#         for line in f:
#             for num in line.strip().split():
#                 total+=float(num)
#                 count+=1
#     print(str(total/count))
# main()

# from statistics import mode


# main()[
#     filename=enter file name
#     total=count=0
#     OPEN filename in read mode
    

# ]

# book_dict={'Abc':20,'ABC':10,'Xyz':5,"XXY":12,"Robin":15,"Robert":40}
# print("TITLE : PRICE")
# for ele in book_dict:
#     if book_dict[ele]<20:
#         print(f"{ele}    ${book_dict[ele]}")


# print(12<<10)

# print(12>>3)

# print(4&1)
# print(5&1)
# print(4|1)
# print(5|1)

# num=int(input("Enter a number: "))
# if 
# print(1<<5)
# print(~1)
# print(N)

# arr=[1,2,3,4,1,2,3]
# res=0
# for ele in arr:
#     res=res^ele
#     # print(res)
# print(res)
# arr = [1, 2, 3,2,1,4,4,3,5] 
# v = 0 
# for i in range(len(arr)): 
#     v = v ^ arr[i] 
# print(v) 

# arr=[1,2,3,4,1,2,3]
# res=0
# for i in range(len(arr)):
#     res=res^arr[i]
# print(res)


# arr=[1,2,3,4,5,6,5,4,3,1]
# res=0
# for ele in arr:
#     res=res^ele
# print(res)
# from hashlib import new


# arr=[1,2,3,4,5,1,2,3]
# even=[ele for ele in arr if ele%2==0]
# odd=[ele for ele in arr if ele%2!=0]
# a=None
# b=None
# res=0
# for ele in arr:
#     res=res^ele
# if res&1==1:
#     new_res=0
#     for ele in even:
#         new_res=new_res^ele
#     a=new_res
#     new_res=0
#     for ele in odd:
#         new_res=new_res^ele
#     b=new_res
#     print(a,b)

    



# import pandas
# print("Hello world")
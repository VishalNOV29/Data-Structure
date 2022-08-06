# def maximumSumSubarray(arr):
#     currentSum=0
#     maxSum=min(arr)
#     start_index=0
#     end_index=0
#     for i in range(len(arr)):
#         currentSum+=arr[i]
#         start_index=i
#         if currentSum>maxSum:
#             maxSum=currentSum
#         if currentSum<0
#             currentSum=0
#     print(start_index)
#     print(end_index)
#     return maxSum

# print(maximumSumSubarray([1,2,3,4,5,-4,-5,-6]))
# print()

# arr=[1,2,3,4,5,6]

# def msi(x):  
#     final_sum=min(arr)
#     arr_index=[]  
#     for i in range(len(x)-1):
#         for j in range(i+1,len(x)+1):
#             temp_arr=x[i:j]
#             current_sum=sum(x[i:j])
#             if current_sum>final_sum:
#                 final_sum=current_sum
#                 arr_index=[i,j]
#     return [arr_index[0],arr_index[1],final_sum]

# arr=[7,-9,5,10,-9,6,9,3,3,9]
# print(msi(arr))

# class Person:
#     def __init__(self,name,yearStarted,program):
#         self.name=name
#         self.yearStarted=yearStarted
#         self.program=program
#     def getName(self):
#         return self.name
#     def changeProgram(self,newProgram):
#         self.program=newProgram
#     def getYear(self):
#         return self.yearStarted
# class Student(Person):
#     courseChange=0
#     def __init__(self,name,yearStarted,program,studentNum):
#         super().__init__(name,yearStarted,program)
#         Student.studentNum=studentNum
#     def changeProgram(self, newProgram):
#         print("This method is called.")
#         print(self.courseChange)
#         if self.courseChange>=1:
#             print("Can't change more than one time per year.")
            
#         else:
#             self.program=newProgram
#             self.courseChange+=1
#     def changeStudentNum(self,newStuNum):
#         Student.studentNum=newStuNum

# class Instructor(Person):
#     def __init__(self,name,yearStarted,program,salary):
#         super().__init__(name,yearStarted,program)
#         self.salary=salary
#     def changeSalary(self,newSalary):
#         self.salary=newSalary

# obj1=Student("XYZ",2019,"CSE",20)
# obj2=Instructor("ABC",2022,"IT",12000)
# print("Instructor name :",obj2.name)

# print("Old Program :",obj1.program)
# obj1.changeProgram("BIOTECH")
# print("New Program :",obj1.program)

# print("Old Salary :",obj2.salary)
# obj2.changeSalary(50000)
# print("New Salary :",obj2.salary)
# obj1.changeProgram("IT")
# print(obj1.program)



        




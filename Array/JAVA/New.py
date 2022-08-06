
# # Function to remove puncutation.
# def clean_punc(source_string):
#     punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     for ele in source_string:
#         if ele in punc:
#             source_string=source_string.replace(ele,"")
#     return source_string

# # Function to detect word.
# def detect_word(source_string, word_to_detect):
#     source_string=clean_punc(source_string)
#     word_list = list(source_string.split())
#     word1=word_to_detect.upper() # for uppercase
#     word2=word_to_detect.lower() # for lowercase
#     word3=word_to_detect.title() # for title
#     if (word1 in word_list) or (word2 in word_list) or (word3 in word_list):
#         return True
#     else:
#         return False
# print(detect_word("I have a PROJECT.","project"))

# def eligibleForSenate(age,lengthOfCitizenship):
#     if age>30 and lengthOfCitizenship>9:
#         return True
#     return False


# def eligibleForHouse(age,lengthOfCitizenship):
#     if age>25 and lengthOfCitizenship>7:
#         return True
#     return False

# # main function.
# def main():
#     print("CONGRESS ELIGIBLITY")
#     age=int(input("Enter age of candidate: "))
#     lengthOfCitizenship=int(input("Enter years of U.S. citizenship: "))
#     result1=eligibleForSenate(age,lengthOfCitizenship)
#     result2=eligibleForHouse(age,lengthOfCitizenship)
#     if result1 and result2:
#         print("The candidate is eligible for election to the House of Representatives and for election to the Senate.")
#     elif (result2 and not result1):
#         print("The candidate is eligible for election to the House of Representatives but is NOT eligible for election to the Senate.")
#     elif (not result2):
#         print("The candidate is NOT eligible for election to either the House of Representatives or the Senate.")

# main() # calling main function.


# list1 = [1, [2, 3], 4]
# result = 0
# for ele in list1:
#     if type(ele) == list:
#         for item in ele:
#             result += item
#     else:
#         result+=ele
# print("result =",result)


# def csll0_lstrip(string):
#     for ele in string:
#         if ele==" ":
#             string=string.replace(ele,"")
#         else:
#             return string

# print(csll0_lstrip("  Hello"))

# def csll0_replace(string,char1,char2):
#     string=string.replace(char1,char2)
#     return string

# print(csll0_replace("hello","h","H"))

# a=-1
# b=3
# c=1
# D=(b**2)-(4*a*c)
# root1=((-b)+(D**.5))/(2*a)
# root2=((-b)-(D**.5))/(2*a)
# print("First root1 =",str(root1))
# print("First root2 =",str(root2))

# x=4
# y=5
# print("Remainder =",x%y)
# print("Quotient =",x//y)


# queue = []

# # enqueue() method.
# def enqueue(data):
#     queue.append(data)
#     return queue

# # dequeue() method
# def dequeue():
#     if len(queue) > 0:
#         return queue.pop(0)
#     else:
#         return -1


# enqueue(5)
# print("queue =", queue)

# enqueue(3)
# print("queue =", queue)

# dequeue()
# print("queue =", queue)

# enqueue(2)
# print("queue =", queue)

# enqueue(8)
# print("queue =", queue)

# dequeue()
# print("queue =", queue)

# dequeue()
# print("queue =", queue)

# enqueue(9)
# print("queue =", queue)

# enqueue(1)
# print("queue =", queue)

# dequeue()
# print("queue =", queue)

# enqueue(7)
# print("queue =", queue)

# enqueue(6)
# print("queue =", queue)

# dequeue()
# print("queue =", queue)

# dequeue()
# print("queue =", queue)

# enqueue(4)
# print("queue =", queue)

# dequeue()
# print("queue =", queue)

# dequeue()
# print("queue =", queue)


class ListBox:
    def __init__(self):
        self.listBox=[]
    def add()

# DESCRIPTION-- In this method we generally compare a element with all of the other element of the array
# and if anyone is smaller than it then we swap it from the smaller element.


list1 = [1, 2, 3, 5, 4, 6, 7, 8, 20, 40, 22, 54, 67]
lb = 0  # lb- loweb bound
ub = len(list1)-1  # ub- upper bound
for i in range(lb, ub):
    # here i have taken range(lb,ub) because last element will be automatically sorted.
    for j in range(i, ub+1):
        # here i have taken range(i,ub+1) because if I take only ub then it won't compare with last element.
        if list1[i] > list1[j]:
            x = list1[i]
            y = list1[j]
            list1[i] = y
            list1[j] = x
print(list1)

# -------- BubbleShort using while loop.-------------------
print("Printing using while loop")

list1 = [5, 4, 3, 2, 1, 0]
lb = 0
ub = len(list1)-1
i = 0
while i < ub:
    j = i
    while j <= ub:
        if list1[i] > list1[j]:
            x = list1[i]
            y = list1[j]
            list1[i] = y
            list1[j] = x
        j += 1
    i += 1
print(list1)

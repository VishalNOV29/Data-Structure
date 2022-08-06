myArray=list(map(int,input("Enter elements separated by space.").strip().split()))
ind=int(input("Enter the position."))
ind=ind-1
for i in range(ind,len(myArray)-1):
    myArray[i]=myArray[i+1]
print(myArray)
myArray=myArray[0:len(myArray)-1]
print(myArray)

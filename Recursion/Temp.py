# Asaking user to enter list of tempereature. 
temp_list=list(map(float,input("Enter temperatures between 0 to 100 separated by space \n").strip().split()))
sum_density=0 # Sum of density at 11 different temperatures.
for Tk in temp_list:
    temp=1200.92-1.0056*Tk+0.001084*(Tk**2) # calculatin density at temperatue Tk.
    sum_density+=temp
avg_density=sum_density/len(temp_list) # Calculating average
print("Average density =",avg_density)


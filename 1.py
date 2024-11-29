steps=input("enter your steps:")

steps_string=steps.split() #20 30 40 -> ['20' , '30' , '40']

steps_string=list(map(int,steps_string))


highest_STEP=max(steps_string)
lowest_STEP=min(steps_string)
avg_STEPS=sum(steps_string)/len(steps_string)
steps_sorted_desc = sorted(steps_string, reverse=True)



print(f"Highest step count: {highest_STEP}")
print(f"Lowest step count: {lowest_STEP}")
print(f"Average daily step count: {avg_STEPS:.2f}") #35.00
print(f"Steps in descending order: {steps_sorted_desc}")
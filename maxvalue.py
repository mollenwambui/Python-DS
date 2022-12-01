age1=int(input("Enter the first age \n"))
age2=int(input("Enter the second age \n"))
age3=int(input("Enter the third age \n"))
if age1>age2 and age1>age3:
    print(f"The firstborn is {age1} years old")
elif age2>age1 and age2>age3:
    print(f"The firstbborn is {age2} years old")    
else:
    print(f"The firstborn is {age3} years old")

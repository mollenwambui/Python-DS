name=str(input("Enter you name \n"))
if len(name)<=3:
    print("3 characters long")
elif len(name)>=50:
    print("Can be a maximum of 50 characters")
else:
    print("Looking good ")    
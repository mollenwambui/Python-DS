n=int(input("Enter any number \n"))
if n%2!=0 and n in range(2,5):
    print("Weird")
elif n%2==0 and n in range(6,20):
    print("This is amazing")
elif n%2==0 and n>20:
    print("I'm greatest")   
elif n%2!=0:
    print("I'm odd")   

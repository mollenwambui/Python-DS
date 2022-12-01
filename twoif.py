
#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
number_of_classes_held=int(input("Enter the number of classes held \n "))
number_of_classes_attended=int(input("Enter the number of classes attended \n"))
percentage_attended=(number_of_classes_attended/number_of_classes_held)*100
sickness=input(str("Do you have any medical condition \n" ))
if percentage_attended<75 and  sickness=="Y":
    print("You are allowed to sit for the exam")
elif percentage_attended<75 :
    print("You are not allowed to sit for the exam")

elif sickness=="N" :
    print("You can't sit for the exam")   

else:
    print("Sorry! You can't sit for the exam")

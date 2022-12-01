#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.

#if employee is a male and age is in between 20 to 40 then he may work in anywhere

#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

#And any other input of age should print "ERROR".
age=int(input("How old are you? \n"))
sex=str(input("Gender? M/F  \n"))
marital_status=str(input("M or S \n"))
if sex=="F" :
    print("You will only work in urban area")
elif sex=="M"  and age>=20 and age<=40:
    print("You can work anywhere!") 
elif sex=="M" and age>=40 and age<=60:
    print("You can only work in urban areas")    
elif sex=="F" and marital_status=="M":
    print("You can take martenity leave")
else:
    print("ERROR")   
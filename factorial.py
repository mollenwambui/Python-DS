#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 
def factorial(number):
    fact=1
    for num in range(1,number+1):
        fact*=num
        print(fact)
factorial(10)        
    #return fact


def myFactorial(number):
    fact=1
    for x in range(1,number+1):
        fact*=x
        print(fact)

myFactorial(12)  


def factorial(num):
    count=1
    for x in range(1,num):
        count*x
        print(count)


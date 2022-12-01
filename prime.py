 #Write a Python function that takes a number as a parameter and check the number is prime or not.
 #Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def prime_number(number):
    if number >1 and number%number==0:
        print("Prime")

    else:
        print("Not  prime")    

prime_number(6)        


def find_sum(number):
    sum=0
    for x in str(number):
        
        sum+=int(x)
        print(sum)

find_sum(23)  


def my_numbers(nums):
    sum=0
    for x in str(nums):
        sum+=int(x)
    print(sum)

my_numbers(1572)        

 
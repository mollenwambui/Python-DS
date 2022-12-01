def greet(name,age):
  year=2022-age
  return f"Hello {name} you were born in {year}"
 
def my_country(name,country="Uganda"):
    return f"Hello {name} from {country}"
  
def hello_multi(*names):
    for name in names:
     print(f"Hello {name}")  

def sum(*numbers):
   nums=0
   for num in numbers:
       nums+=num
   return nums
def greet_multiple(**kwargs):
    keys=kwargs.keys()
    if "name" in keys:
        print("Hello {kwargs['name']}")
    elif "country" in keys:
          print("Hello from {kwargs['country']")

    else:
      print("Hello anonymous")


def sum_and_greets(*args,**kwargs):
    print(args)
    print(f"Hello {kwargs}")

def product_and_greeting(*args,**kwargs):
    product=1
    for num in args:
        product*=num
    return product,kwargs
    

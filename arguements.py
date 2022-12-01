
def product_and_greeting(*args,**kwargs):
    product=1
    for num in args:
        product*=num
    print(product)
    print(f"Hello{kwargs}")
    
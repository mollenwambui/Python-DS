# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
def upper_and_under(name):
    x=0
    y=0
    for x in name:
        if name==name.upper():
            print(len(x))
            
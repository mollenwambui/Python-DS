#Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
# def list_comprehension(list):
#     newlist=[]
#     for x in list:
#         if x not in newlist:
#          newlist.append(x)
#     return newlist     

# print(list_comprehension([2,3,4,5,4,6,4,3,3,3]))

# comprehension_list=[1,2,3,12,34,56,67,890,1,2,3]
# empty_list=[]
# for y in comprehension_list:
#     if y not in empty_list:
#         empty_list.append(y)



def unique_elements(list):
    new_list=[]
    for num in list :
        if num not in new_list:
            new_list.append(num)
        print(new_list)    

unique_elements([1,2,3,3,3,3,4,5])


#how to flatten a list
list_a=[1,2,[3,4,5[4,7,8]]]
for sublist in list_a:
    for num in sublist:
        print(num)


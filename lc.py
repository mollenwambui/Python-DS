list_1 = [23,24,25,26]
list_2 = [27,28,29,30]

# for x ,y in list_1 ,list_2:
#     list_3.append(x,y)

# list3=[]
# for i,j in zip(list_1,list_2):
#     list3.append(i,j)
list_3 = [*list_1,*list_2]
print(list_3)


my_list=[1,2,3,4,6,5,4]
for x in my_list:
    while x==4:
        x='Hello'
    print(x)    




myList=[1,2,9,5,6, 5]
# squaredList=[]
# for item in myList:
#     squaredList.append(item*item)
# print(squaredList)

# Above code can be simplified using list comprehensions.There is a example in below

squaredList=[i*i for i in myList]
print(squaredList)

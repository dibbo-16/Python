l=[3,54,334,34]
# index=0
# for item in l:
#     print(f"The item number at index {index} is {item} ")
#     index+=1

# Above code can be simplified using enumerate function. There is a example in below

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item} ")
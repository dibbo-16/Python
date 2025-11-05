class Demo:
    a=4
c=Demo()
print(c.a) # Print the class attribute because instance attribute is not present
c.a=1 # instance attribute is set
print(c.a) # Print the instance attribute because instance attribute is present
print(Demo.a) # print the class attribute

# So class attribute not change

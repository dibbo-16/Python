a=int(input("Enter your age:"))
# if is independent
# if statement number 1
if(a%2==0):
    print("a is even")
# if statement number 2
if(a>=18):
    print("You are above the age of consent.")
    print("Good for you.")

elif(a<0):
    print("You are entering a invalid negative age")

elif(a==0):
    print("You are entering 0, which is not a valid age ") 

else:
    print("You are below the age of consent.")

print("End of program")    
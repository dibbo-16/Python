try:
    a=int(input("Hey, Enter a number: "))
    print(a) 
 # if try successfully run, it will go to else  
except Exception as e:
    print(e)
else:    
    print("I am inside else")   
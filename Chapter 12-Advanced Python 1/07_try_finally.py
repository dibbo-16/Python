def main():
    try:
       a=int(input("Hey, Enter a number: "))
       print(a) 
    # if try successfully run or not, it will go to finally  
    except Exception as e:
        print(e)
    finally:    
        print("I am inside of finally")   
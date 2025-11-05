with open("log.txt","r") as f:
    content= f.read()

if("python" in content):
    print("Yes, Python word is here")
else:
  print("No, Python word is not here")   

with open("old.txt","r") as f:
    content=f.read()
with open("renamed_by_python.txt","w") as f:
    f.write(content)   

# here old.txt file delete hoy nai . But we can do it by shutil mudule import    
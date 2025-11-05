#done by chatgpt
import os

# specify the directory you want to list
directory = "/Python"

# list all files and folders in the directory
contents = os.listdir(directory)

print(f"Contents of directory '{directory}':")
for item in contents:
    print(item)
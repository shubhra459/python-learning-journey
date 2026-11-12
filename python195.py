import os
file_path = input("enter your file name:")
find_file_path = os.path.exists(file_path)
if  not find_file_path :
    print("file doesnt exist")
elif os.path.isfile(file_path):
 print("it is a file")    
 
 basename = os.path.basename(file_path)
 split = os.path.splitext(basename)
 dirname = os.path.dirname(file_path)
 size = os.path.getsize(file_path)
 print(basename)
 print(split[0])
 print(split[1])
 print(dirname)
 print(size)
elif os.path.isdir(file_path):
 print("it is a folder")

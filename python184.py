import os
folder = "data"
file_name = input("entr your file:")
file_path = os.path.join(folder,file_name)
is_file = os.path.isfile(file_path)
if  is_file :
    print("file found")
else :
    print("file not found")    
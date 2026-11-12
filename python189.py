import os
old_file_name = input("entr your old file name:")
new_file_name = input("enter your old file name")
old_file_path = os.path.join("data",old_file_name)
new_file_path = os.path.join("data",new_file_name)
old_file1 =os.path.exists(old_file_path)
if old_file1 :
    os.rename(old_file_path,new_file_path)
    print("file rernamed successfully")
else:
    print("file not found")    
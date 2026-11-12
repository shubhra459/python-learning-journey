import os
folder_file = input("enter your file name:")
is_it_exists = os.path.exists(folder_file)
if is_it_exists :
    os.remove(folder_file)
    print("file deleted")
else:
    print("not found")    
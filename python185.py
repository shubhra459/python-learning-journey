import os
folder = "data"
folder_file = input("enter your file name:")
new_file = os.path.join(folder,folder_file)
is_it_exists = os.path.exists(new_file)
if is_it_exists :
    print("found")
else:
    print("not found")    
import os
folder_name = input("entr your folder name:")
directory = os.path.isdir(folder_name)
new_folder = os.path.exists(folder_name)
if new_folder and directory :
    os.rmdir(folder_name)
    print("folder deleted")
else:
 print("folder dont exist")



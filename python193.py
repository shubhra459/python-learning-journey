import os
counter = 0
folder_path = input("enter your folder name:")
find_folder = os.walk(folder_path)
for root ,dirs,files in find_folder:
   for file in files :  
    if file.endswith(".csv") :
     counter =counter +1
     print(file)

print(counter)
  
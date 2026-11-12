import os
counter = 0
total_size = 0
folder_path = input("enter your folder:")
find_folder = os.walk(folder_path)
folder_exist = os.path.exists(folder_path)
if os.path.isdir(folder_path):
    print("it is a folder")
for root,dirs,files in find_folder : 
 for file in files:    
  if file.endswith(".txt"):
    join = os.path.join(root,file)
    print(file)
    print(join)
    counter = counter +1
    
       
    getsize = os.path.getsize(join)
    total_size =getsize + total_size

print(counter)
print(total_size)    
import os
counter = 0
totalsize = 0
folder_path = input("enter your folder name:")
folder_exist = os.path.exists(folder_path)
if not folder_exist:
  print("folder doesnt exist")
elif os.path.isdir(folder_path):
     print("folder exist")  
     find_folder = os.listdir(folder_path)  
     for file in find_folder:
      if file.endswith(".txt"):
       join = os.path.join(folder_path,file)
     print(join)
     print(file)
     counter = counter + 1
     getsize = os.path.getsize(join)
     totalsize = totalsize + getsize
else:
 print("it is a file ,not a folder")

print(counter)
print(totalsize)

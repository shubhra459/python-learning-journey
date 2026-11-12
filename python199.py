import os
counter = 0
total_size = 0
folder_path = input("enter your folder path:")
folder_exist = os.path.exists(folder_path)
if  not folder_exist:
   print("folder doesnt exist")
elif  os.path.isfile(folder_path):
  print("this is a file")

else:
 find_folder = os.listdir(folder_path)
 for file in find_folder:
   if file.endswith(".txt"):
     join = os.path.join(folder_path,file)
     counter = counter + 1
     get_size = os.path.getsize(join  )
     total_size = total_size + get_size
 print(counter)
 print(total_size)     
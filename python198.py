import os
counter = 0
largest = 0
folder = input("enter your folder name:")
folder_exist = os.path.exists(folder)
if not folder_exist:
   print("folder doesnt exists")

elif os.path.isdir(folder) :
   print("folder exist")
   
   find_folder = os.listdir(folder)
   for file in find_folder:
    if file.endswith(".txt"):
      join = os.path.join(folder,file)
      counter =counter + 1
      
      getsize = os.path.getsize(join)
      if getsize > largest:
        largest = getsize
        largest_file = file
   if counter == 0:
       print("no text files")  
   else   :
       print(largest)
       print(largest_file)      
else:
      print("it's a file, not a folder")    

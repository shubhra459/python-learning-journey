import os
import shutil
source_file_path  = input("enter your file path:")
destination_path = input("enter your folder path:")
file_exist = os.path.exists(source_file_path)
if not  file_exist:
 print("file isnt exist")
elif os.path.isfile(source_file_path):
 print("valid file")
else:
 print("exist but isnt a file")
folder_exist = os.path.exists(destination_path)
if not folder_exist:
 print("folder isnt  exist")
elif os.path.isdir(destination_path):
 print("valid folder")
else:
 print("exist but not a folder")  
if os.path.isfile(source_file_path) and os.path.isdir(destination_path):
  move = shutil.move(source_file_path,destination_path)
  print(move)
  print("transfer successful")
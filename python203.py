import os
from pathlib import Path
user_path = input("enter your path:")
path = Path(user_path)
path_exist = path.exists()
if not path_exist :
    print("the path doesn't exist")
elif path.is_dir():
 print("it is folder")    
 find_folder = path.iterdir()
 for file in find_folder:
   if file.suffix == ".csv" :
     print(file)
     

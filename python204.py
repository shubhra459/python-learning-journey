from pathlib import Path
user_path = input("enter tour path:")
path = Path(user_path)
path_exist = path.exists()
if not path_exist :
 print("path doesn't exist")

elif  not path.is_dir():
 print("it is not a folder") 
else:
 print("it is a folder")
 glob = path.glob("sales*.csv")

 for file in glob:
   print(file)
  
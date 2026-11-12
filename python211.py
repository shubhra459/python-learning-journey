from pathlib import Path
user_path = input("enter your path:")
counter = 0
folder = "processed"
path = Path(user_path)
path_exist =path.exists()
if not path_exist :
    print("this path doesn't exist")
elif not path.is_dir():
    print("not folder")
else:
   (path/folder).mkdir(parents = True,exist_ok= True)
   glob = path.glob("**/*.csv")
   for file in glob:
    counter = counter + 1
    print("file")    
print(counter)
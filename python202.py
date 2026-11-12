from pathlib import Path
user_path = input("enter your path:")
path = Path(user_path)
path_exist = path.exists()
if not path_exist :
    print("the path doesn't exist")
elif path.is_file():
    print("it is a file")
else:
    print("it's a folder")        

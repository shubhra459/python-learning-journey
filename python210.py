from pathlib import Path
user_path = input("enter your path")
path = Path(user_path)
path_exist = path.exists()
if not path_exist :
    print("path does not exist")
elif not path.is_file():
    print("it's not a file")
else:
    path.unlink()
    print("file deleted successfully")        
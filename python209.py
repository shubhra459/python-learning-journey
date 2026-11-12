from pathlib import Path
user_path = input("enter your path name:")
path = Path(user_path)
path_exist = path.exists()
if not path_exist :
    print("path not exist")
elif not path.is_file() :
    print("not file")
else:
    print("it is a file")
    path.write_text("Data Analytics Report\n Analysis completed successfully")       
    don = path.read_text()
    print(don)
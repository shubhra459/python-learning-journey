from pathlib import Path
user_path = input("enter your path name:")
path = Path(user_path)
path.mkdir(parents = True,exist_ok =True)
(path/"raw_data").mkdir(parents = True,exist_ok =True)
(path/"cleaned_data").mkdir(parents = True,exist_ok =True)
(path/"reports").mkdir(parents = True,exist_ok =True)
print("success")
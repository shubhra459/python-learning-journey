from pathlib import Path
user_path = input("entr yuour file name: ")
path = Path(user_path)
path.mkdir(parents= True,exist_ok = True)
folders = ["raw_data", "cleaned_data", "reports",]
for folder in folders :
    (path/folder).mkdir(parents =True ,exist_ok =True)
    
print("Project structure created successfully")
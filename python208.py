from pathlib import Path
user_Path = input("enter your path name:")
path = Path(user_Path)
path.mkdir(parents= True,exist_ok= True)
folders = ['raw_data','reports']
for folder in folders :
    (path/folder).mkdir(parents= True,exist_ok= True)
files = ['summary.txt','analysis.txt']
for file in files:
    (path/"reports"/file).touch()
print("created successfully")

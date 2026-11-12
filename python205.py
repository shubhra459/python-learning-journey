from pathlib import Path
counter = 0
user_path = input("enter your path:")
path = Path(user_path)
folder_exist = path.exists()
if not folder_exist :
    print("path doesnt exist")
elif not  path.is_dir():
   print("it's a path but not a folder")
else:
    print("it's a folder") 
    glob =path.glob('**/*.csv')
    for file in glob :
        counter = counter + 1
        print(file)
print(counter)        
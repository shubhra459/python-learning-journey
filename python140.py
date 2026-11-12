with open("students.txt","r") as file:
    contents = file.readlines()
for content in contents :
     print(content.strip())    

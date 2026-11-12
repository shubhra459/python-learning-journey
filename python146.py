try :
 with open("sales.txt","r") as file:
  content = file.read()
 print(content)
except FileNotFoundError:
 print("sales file not found")  
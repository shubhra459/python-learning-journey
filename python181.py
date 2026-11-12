import os 
files = os.listdir()
counter = 0
for file in files :
   if file.endswith(".py") :
      counter = counter + 1
      
print(counter)



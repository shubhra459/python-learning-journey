import os
filename = input("enter your file name:")
filename1 = os.path.exists(filename)
if filename1 :
 size = os.path.getsize(filename)
 print(filename)
else:
    print("file not found")

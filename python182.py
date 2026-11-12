import os
directory = os.listdir()
count = 0
for file in directory:
    if os.path.isfile(file):
        count = count +1
        print
for folder in directory:
    if os.listdir(folder):
        count = count + 1
        print(count)
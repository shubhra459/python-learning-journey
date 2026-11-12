import os 
file_create = os.makedirs("analytics/data/cleaned",exist_ok = True)
new_file = os.path.isdir("analytics/data/cleaned")

print(new_file)
import os
full_file_path = input("enter your info:")
basename = os.path.basename(full_file_path)
dirname = os.path.dirname(full_file_path)
print(basename)
print(dirname)
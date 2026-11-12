"""
shutil stands for  shell utilities it is a python,
built-in module mainly used copying ,moving and deleting files.
"""
import shutil
source_file_path = input("enter your file:")
destination_file_path = input("enter your file:")
copy = shutil.copy(source_file_path, destination_file_path)
print(copy)
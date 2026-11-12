with open ("students.txt","r") as file:
    content = file.read(5)
    print(content) 
    print(file.seek(0))
    
    print(file.read(5))
'''
A file has content, and Python maintains a current position (cursor) inside 
that file. read() reads from that position, tell() reports the position,
and seek() changes the position .    
'''
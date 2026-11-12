"""
json stands for javascript object notation 
JSON is a data format used to represent/exchange that information.
"""
import json 
data = '{"name" : "Rahul", "age" : 20, "skills" : [ "Python", "SQL", "Excel"]}'
students = json.loads(data)
print(students["name"])
print(students["age"])
print(students["skills"])


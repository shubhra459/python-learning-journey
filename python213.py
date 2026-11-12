import json
student = '{"name" : "Rahul", "age" : 20 ,"skillsyu": ["Python", "SQL", "Excel"]}'
student1 = json.loads(student)
data = json.dumps(student1)
print(data)
print(type(data))
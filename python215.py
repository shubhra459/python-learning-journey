import json
student = {
     "name": "Rahul",
    "age": 20,
    "skills": ["Python", "SQL", "Excel"]
}
with open ("student_output.json","w") as file:
     json.dump(student,file)
with open ("student_output.json","r") as file:
    print(json.load(file))   

student = {
    "name":"rahul",
    "age":21,
    "course":"python"
}
print(student["name"])

student.update({
    "age":22,
    "city":"banglore",
})
for key,values in student.items():
    print(key,values)
if "course" in student:
    print("course is exist")     
else:
    print("course is nor exist")    
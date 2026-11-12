data = [
    {"id": 1, "name": "Rahul","age": 20},
    {"id": 2, "name": "Amit", "age": 25},
    {"id": 3, "name": "Priya","age": 22}
]
counter = 0
for user in data:
    
    if user["age"] > 21:
     print(f'{user["id"]}-{user["name"]} ')
     counter = counter + 1
print(counter)     
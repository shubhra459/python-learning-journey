data = [
    {"name": "Rahul", "city": "Bengaluru", "age": 20},
    {"name": "Amit", "city": "Mumbai", "age": 25},
    {"name": "Priya", "city": "Bengaluru", "age": 22},
    {"name": "Rohan", "city": "Delhi", "age": 19}
]
for user in data:
    if  user["age"] > 20:
     if user["city"] == "Bengaluru" :
        print(f"{user["name"]}-{user["age"]}")
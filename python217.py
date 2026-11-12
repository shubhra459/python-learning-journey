import json
data = {
    "company": {
        "name": "ABC Corp",
        "employees": [
            {"name": "Rahul", "department": "Analytics", "salary": 50000},
            {"name": "Amit", "department": "Marketing", "salary": 45000},
            {"name": "Priya", "department": "Analytics", "salary": 60000}
        ]
    }
}
for employees in data["company"]["employees"]:
    if employees["department"] == "Analytics":
        print(f"{employees['name']},{employees['salary']}")
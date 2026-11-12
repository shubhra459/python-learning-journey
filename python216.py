data = {
    "company": {
        "name": "ABC Corp",
        "employees": [
            {"name": "Rahul", "department": "Analytics", "salary": 50000},
            {"name": "Amit", "department": "Marketing", "salary": 45000}
        ]
    }
}

for employees in data["company"]["employees"]:
    
 print(f"{employees["name"]},{employees["department"]}")

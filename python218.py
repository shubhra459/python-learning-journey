"""
Think of an API as a middleman between your Python program and another system's data.
"""
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)
data = response.json()
print(data)

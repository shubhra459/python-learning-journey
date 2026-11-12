def analyze (data):
    if data == []:
        return 0
    if isinstance(data[0],list):
        return analyze(data[0]) + analyze(data[1:])
    if isinstance(data[0],int):
        return data[0] + analyze(data[1:])
    if isinstance(data[0],str):
        return 0 + analyze(data[1:])
data = [
    10,
    "hello",
    [5, "skip", 6],
    ["python", [1, 2, "ignore"]],
    20
]
print(analyze(data))
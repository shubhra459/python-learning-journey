# map() lets you apply the same function to every item in a collection.
# in python map () returns a map object ,not a normal list,if u wanr to see result u have to use list.
numbers = [5,10,15,20]
result = map(lambda x : x*3,numbers)
print(list(result))
def nested_sum(data):
    if data == []:
        return 0
    if (isinstance(data[0],list)) :
       return nested_sum(data[0]) + nested_sum(data[1:]   )
    else:
        return data[0] + nested_sum(data[1:])
         
data =  [1, [2, 3], [4, [5, 6]], 7]
print(nested_sum(data))

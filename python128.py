number = [1,2,3]
letters = ["x","y"]
result = [(number,letter) for number in number  for letter in letters]
print(result)
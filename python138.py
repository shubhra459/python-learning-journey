try:
 x = int(input("enetr your age:"))
 if x < 18:
    raise ValueError ("you are a kid ")
 else:
    print("enjoy kid")
except ValueError as e:
  print(e)
finally:
  print("program finished")      
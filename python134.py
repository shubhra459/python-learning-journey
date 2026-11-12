try:
    x = int(input("enter a number:"))

except ValueError:
    print("invald number")
else:
    print(f"valid number:{x}")        
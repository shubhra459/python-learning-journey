def list_sum (numbers):
    if numbers == []:
        return 0
    total =  numbers[0] + list_sum(numbers[1:])
    return total
numbers =list(map(int, input("Enter numbers: ").split(",")))
print (list_sum(numbers))
      

    

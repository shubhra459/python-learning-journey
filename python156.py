import random
guess = int(input("enter number between 1 to 10:"))
random_number = random.randint(1,10)
print(random_number)
if guess == random_number :
    print("you guessed it")
else:
    print("wrong guess")    
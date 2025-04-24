# Number guessing game in Python 
import random


a = int(input("Enter the start of the range"))
b = int(input("Enter the last of the range"))

random_number = random.randint(a, b)
print(random_number)
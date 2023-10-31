import random

from math import sqrt

my_name = "Angel"
my_age = "37"
my_height = "1.83"
my_list =[2, "text", "sammael", 3, 8.9]
my_dict = {
    "A": 0,
    "B": 1,
    "C": 3
}

print (my_dict["B"])
print (my_name[0].isupper())
print (my_name[0].islower())

def add_numbers(number1, number2):
    return number1 + number2
number1 = 6
number2 = 9
results = add_numbers(number1, number2)

print(results)

sqrt_results = sqrt(16)
print(sqrt_results)

start = 1
end = 10

for i in range(start, end+1):
    if i % 2 == 0:
        print (i, "is even")
    else:
        print (i, "is odd")
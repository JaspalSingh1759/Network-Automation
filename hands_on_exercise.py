"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`

pi = math.pi
print(f"Type is {type(pi)} and value is {pi}"  )

# TODO: Write a conditional to print out if `i` is less than or greater than 50

i = random.randint(0, 100)
if i==50:
    print("i is equal to 50")
elif i>50:
    print("i is greater than 50")
elif i <50:
    print("i is less than 50")


# TODO: Write a conditional that prints the color of the picked fruit

picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit=="orange":
    print(f"color is orange because fruit is {picked_fruit}")
elif picked_fruit=="strawberry":
    print(f"color is red because fruit is {picked_fruit}")
elif picked_fruit=="banana":
    print(f"color is banana because fruit is {picked_fruit}")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def mult(a,b):
    return a*b

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",mult(12,96))

print("48 x 17 =",mult(48,17))

print("196523 x 87323 =",mult(196523,87323))

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 06:45:12 2023

@author: bahaa
"""
#%% Ex 1:
'''
Write a program that asks the user to enter the radii of circles for which they want to calculate the areas and circumferences.

a. Without using functions: Calculate the area and circumference of each circle and print:

"The area and circumference of the circle with radius r1 are a1 and c1, respectively."
"The area and circumference of the circle with radius r2 are a2 and c2, respectively."
"The area and circumference of the circle with radius r3 are a3 and c3, respectively."
b. Using functions: Define one function to calculate the area and circumference of a circle 
based on its radius, and call these functions for each circle entered by the user. Print the same output as in part a.

Note: Please replace the variables a1, a2, a3, c1, c2, c3, r1, r2, r3 with the actual calculated values for the respective circles.
'''

# part A
# Ask the user to enter the radii of the circles
r1 = float(input("Enter a radius: "))
r2 = float(input("Enter another radius: "))
r3 = float(input("Enter one more radius: "))
a1 = 3.14 * r1 * r1
a2 = 3.14 * r2 * r2
a3 = 3.14 * r3 * r3
c1 = 2 * 3.14 * r1
c2 = 2 * 3.14 * r2
c3 = 2 * 3.14 * r3
print(f"The area and circumference of the circle with radius {r1} are {a1} and {c1}, respectively.")
print(f"The area and circumference of the circle with radius {r2} are {a2} and {c2}, respectively.")
print(f"The area and circumference of the circle with radius {r3} are {a3} and {c3}, respectively.")
print()

#%% part B
def circle_area_circum_calc(radius):
    area = 3.14 * radius * radius
    circum = 2 * 3.14 * radius
    print(f"The area and circumference of the circle with radius {radius} are {area} and {circum}, respectively.")
circle_area_circum_calc(r1)
circle_area_circum_calc(r2)
circle_area_circum_calc(r3)
print()

#%% Ex 2:
'''
a- define X (Type range) between 0 and 10
b- define a fun that return Y = X**2 + 1
c- define a fun that returns the derivative of Y(X)
'''
import random
x = random.randrange(0, 11)
print(x)
def square_plus_one(num):
    return num**2 + 1
def derivative(x):
    return 0

print(square_plus_one(x), derivative(x))
print()

#%% Ex 3:
'''
Suppose you have a list of integers, and you want to find the sum and average 
of all the even numbers in the list. Write a program that uses a function to 
accomplish this task.

test it on two different lists
'''
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
def even_summation_average(temp):
    total = 0
    count = 0
    for num in temp:
        if num % 2 == 0:
            total += num
            count += 1
    return total, total / count
print(even_summation_average(list1))
print(even_summation_average(list2))
print()

#%% Ex 4:
'''
Write a program that computes the roots of a second-degree polynomial equation 
of the form ax^2 + bx + c = 0, where a, b, and c are coefficients entered by the user.
 Use a function to implement the quadratic formula to solve the equation, 
 and return the two possible roots.
 '''
import math
def quadratic_formula(a, b, c):
    root1 = -1 * (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    root2 = -1 * (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return root1, root2
print(quadratic_formula(1, 7, 12))
print()


#%% Ex 5:
'''
Suppose you have a function f(x) = x^3 - 3x + 1, and you want to find its root 
using the iterative method known as Newton's method. Write a program that uses 
a function to implement Newton's method to find the root of this function, 
given an initial guess x0 and a tolerance tol. The function should return the 
estimated root and the number of iterations required to reach it.


Here is a brief description of the Newton's method algorithm in a few steps:

1- Start with an initial guess, x_0, for the root of the function f(x).
2- Compute the function value and its derivative at the current guess, f(x_n) 
and f'(x_n), respectively.
3- Use the formula x_{n+1} = x_n - f(x_n) / f'(x_n) to compute the next guess for the root.
4- Repeat steps 2-3 until the difference between two successive guesses 
is smaller than a desired tolerance or a maximum number of iterations is reached.
5- Output the last computed guess as the estimated root of the function f(x).

'''



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







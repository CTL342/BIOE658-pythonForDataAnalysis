# -*- coding: utf-8 -*-
"""
Created on Thu October  9  2025
@author: bahaa
"""

#################### Example 1 ##########################
#%% 
'''
Suppose we want to model a bank account with support for
 deposit and withdraw operations. One way to do that is by 
 using global state as shown in the following example.
 '''

class bank_account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

Steve_Bank_Account = bank_account(0)
Farid_Bank_Account = bank_account(10)
Sarah_Bank_Account = bank_account(10)

Steve_Bank_Account.deposit(50)
Steve_Bank_Account.withdraw(20)
print(Steve_Bank_Account.balance)

Farid_Bank_Account.deposit(50)
Farid_Bank_Account.withdraw(20)
print(Farid_Bank_Account.balance)

Sarah_Bank_Account.deposit(50)
Sarah_Bank_Account.withdraw(20)
print(Sarah_Bank_Account.balance)
     

#------------------------------------------------------------------------------   
#%% Exercice 2
#%% Question 1
'''Write a Rectangle class, 
allowing you to build a rectangle with length
 and width attributes.
'''
# Question 2
'''Create a Perimeter() method to calculate the perimeter
 of the rectangle and a Area() method to calculate the area 
 of ​​the rectangle.
'''
# Question 3
'''
Create a method display() that display the length, width, 
perimeter and area of an object created using an instantiation
 on 
''' 
#% Question 4:
'''
 Create a Parallelepipede child class inheriting from the 
 Rectangle class and with a height attribute and another 
 Volume() method to calculate the volume of the Parallelepiped.
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return self.length * 2 + self.width * 2

    def Area(self):
        return self.length * self.width
    
    def display(self):
        print("Rectangle Length", self.length)
        print("Rectangle Width", self.width)
        print("Rectangle Perimeter", self.Perimeter())
        print("Rectangle Area", self.Area())
        
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
        return self.Area() * self.height

#%%
'''
Exercise 3: Create a Class for a Dice
Create a Dice class that simulates rolling a dice. The class should have two methods:

__init__: Initialize the dice object with a number of sides (like 6).
roll: Simulate rolling the dice and return the result (a random integer between 1 and the number of sides).
Use the random module to generate a random integer for the roll method.

Here's an example of how the Dice class should work:


# Create a six-sided dice object
dice = Dice(6)

# Roll the dice 10 times and print the results
for i in range(10):
    print(dice.roll())

The output should be something like:
4
1
6
2
5
1
3
2
6
4
'''

import random

class Dice():
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randrange(1, self.sides + 1)

dice = Dice(6)
for i in range(10):
    print(dice.roll())


#%% Exercise 4: Create a Class for a Vehicle:
'''    
Create a Vehicle class that represents a vehicle. The class should have two methods:
1. __init__: Initialize the vehicle object with a make and model.
2. start: Simulate starting the vehicle.

Then, create two classes `Car` and `Bicycle` that inherit from the Vehicle class.

The `Car` class should have an additional method:
1. drive: Simulate driving the car.

The Bicycle class should have an additional method:
1. pedal: Simulate pedaling the bicycle.

Here's an example of how the Vehicle, Car, and Bicycle classes should work:


# Create a vehicle object with make 'Toyota' and model 'Corolla'
vehicle = Vehicle('Toyota', 'Corolla')

# Start the vehicle
vehicle.start()

# Create a car object with make 'Ford' and model 'Mustang'
car = Car('Ford', 'Mustang')

# Start the car and drive it
car.start()
car.drive()

# Create a bicycle object with make 'Schwinn' and model 'Mountain Bike'
bike = Bicycle('Schwinn', 'Mountain Bike')

# Start the bicycle and pedal it
bike.start()
bike.pedal()


The output should be something like:

Starting the Toyota Corolla.
Starting the Ford Mustang.
Driving the Ford Mustang.
Starting the Schwinn Mountain Bike.
Pedaling the Schwinn Mountain Bike.
'''

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self):
        print("Starting the", self.make, self.model)
    
class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def drive(self):
        print("Driving the", self.make, self.model)

class Bicycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def pedal(self):
        print("Pedaling the", self.make, self.model)

### Given Code

# Create a vehicle object with make 'Toyota' and model 'Corolla'
vehicle = Vehicle('Toyota', 'Corolla')

# Start the vehicle
vehicle.start()

# Create a car object with make 'Ford' and model 'Mustang'
car = Car('Ford', 'Mustang')

# Start the car and drive it
car.start()
car.drive()

# Create a bicycle object with make 'Schwinn' and model 'Mountain Bike'
bike = Bicycle('Schwinn', 'Mountain Bike')

# Start the bicycle and pedal it
bike.start()
bike.pedal()

###
import numpy as np 
import matplotlib.pyplot as plt 


#%% ex 1
import numpy as np  # Import the NumPy module
# Create a 1D NumPy array containing the first five positive integers
# Print the array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

#%% ex 2
import numpy as np  # Import the NumPy module
# Create a 1D NumPy array with 12 sequential integers starting from 1
# Print the shape of this array
# Reshape this array into a 2D array with 3 rows and 4 columns
# Print the reshaped array and its new shape
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr2.shape)
print(arr2)
arr3 = arr2.reshape(3, 4)
print(arr3.shape)
print(arr3)

#%% ex 3
import numpy as np  # Import the NumPy module

# Create a 1D NumPy array of 10 random integers between 1 and 100
# Print the entire array
# Print the first 5 elements of the array
# Print the last element of the array
arr4 = np.random.randint(1, 101, size=10)
print(arr4)
print(arr4.shape)
print(arr4[:5])
print(arr4[-1])

#%% ex 4
import numpy as np  # Import the NumPy module

# Create two 1D NumPy arrays, each with 5 elements of your choice
# Print both arrays
# Calculate and print the sum, element-wise product, and difference (first array - second array) of the arrays
arr5 = np.array([1, 2, 3, 4, 5])
arr6 = np.array([6, 7, 8, 9, 10])
print(arr5)
print(arr6)
print(arr5 + arr6)
print(arr5 * arr6)
print(arr5 - arr6)

#%% ex 5
import numpy as np  # Import the NumPy module

# Create a 1D NumPy array with 10 elements, ranging from 1 to 10
# Use boolean masking to create and print a new array that only contains elements greater than 5
arr7 = np.arange(1, 11)
print(arr7)
arr8 = arr7[arr7 > 5]
print(arr8)

#---------------------------------------
#%% ex 6
# solve 
#---------------------------------------
'''
3*x + y - z = 2
x + y - z   = 0
2x + 2y + z = 9
'''
arr9 = np.array([[3, 1, -1],
                [1, 1, -1],
                [2, 2, 1]])
arr10 = np.array([2, 0, 9])
solution = np.linalg.solve(arr9, arr10)
print(solution)

#---------------------------------------
#%% ex 7
#---------------------------------------
'''
The goal of this exercise is to sort the rows of a 2D array by the values in a specified column.

Instructions:

1. Import the NumPy library.
2. Create a 2D NumPy array with random integers.
3. Sort the created array using "column wise sorting".
4. Sort the rows of the 2D array based on the values in a specified column.
hint: use np.argsort
'''
import numpy as np
arr11 = np.random.randint(1, 11, size=(2, 10))
print(arr11)
arr12 = arr11[:, 1].argsort()
print(arr12)

#---------------------------------------
#%% ex 8
#---------------------------------------
import numpy as np

person_dtype = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])

# Create an empty structured array with the custom dtype defined above (add three)
# Fill the structured array with data
# Access data in the structured array
# sort by age:
# sort by height:    
# sort by age and then height if ages are equal:

people = np.zeros(3, dtype=person_dtype)
people[0] = ('Alice', 25, 165.5)
people[1] = ('Bob', 30, 170.0)
people[2] = ('Charlie', 25, 175.3)
print("Accessing individual elements:")
print(f"First person: {people[0]}")
print(f"Name of second person: {people[1]['name']}")
print(f"Ages: {people['age']}")
print(f"Heights: {people['height']}")
print()
sorted_by_age = np.sort(people, order='age')
print("Sorted by age:")
print(sorted_by_age)
print()
sorted_by_height = np.sort(people, order='height')
print("Sorted by height:")
print(sorted_by_height)
print()
sorted_by_age_then_height = np.sort(people, order=['age', 'height'])
print("Sorted by age, then height:")
print(sorted_by_age_then_height)
print()

#---------------------------------------
#%% ex 9
#---------------------------------------
'''
The goal of this exercise is to fit a straight line to a set of data points using the least squares method.

Instructions:

1. Import the NumPy library.
2. Generate a set of data points (x, y) with some random noise added to the y values.
3. Use np.linalg.lstsq to find the best-fitting line parameters (slope and intercept).
4. Print the slope and intercept of the best-fitting line.
'''

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.linspace(0, 10, 20)
y = 2.5 * x + 1.0 + np.random.normal(0, 1.5, size=x.shape) 

A = np.vstack([x, np.ones(len(x))]).T
solution, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)
slope, intercept = solution

x_fit = np.linspace(0, 10, 100)
y_fit = slope * x_fit + intercept

plt.plot(x, y, 'o')
plt.plot(x_fit, y_fit, 'r-', label=f'Fit: y = {slope:.2f}x + {intercept:.2f}', linewidth=2)
plt.show()
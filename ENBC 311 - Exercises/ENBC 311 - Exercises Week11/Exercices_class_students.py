"""
@author: Bahaa.Ghammraoui

"""

#%% prob 1
#%% 1 Write a Pandas program to create and display a DataFrame from a specified
'''
dictionary data which has the index labels.

 

Sample DataFrame:

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',

                      'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
'''
'''
2- Write a Pandas program to display a summary of the basic information created DataFrame.


3- Write a Pandas program to get the first 3 rows

4- Write a Pandas program to select the 'name' and 'score' columns and print them

5- Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.

6- Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2

7- Write a Pandas program to count the number of rows and column

8- Write a Pandas program to select the rows where the score is missing, i.e. is NaN

9- Write a Pandas program to select the rows the score is between 15 and 20 (inclusive)
10- Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.

11- Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order
'''



#-------------------------------------------------------------------------------

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',

                      'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index = labels)
print("General Info:")
print(df)
print(df.info(), "\n")

print("First Three Rows")
print(df.head(3), "\n")

print("Name and Score Columns")
print(df.loc[:, ['name', 'score']], "\n")

print("Rows 1, 3, 5, and 6")
print(df.loc[['a', 'c', 'e', 'f'], ['name', 'score']], "\n")

print("Attempts greater than 2")
print(df.loc[df['attempts'] > 2], "\n")

print("Dimension of Data")
print(df.shape, "\n")

print("Missing Info Rows")
print(df[df['score'].isnull()], "\n")

print("Scores between 15 and 20")
print(df[(df['score'] > 15) & (df['score'] < 20)], "\n")

print("Attempts less than 2 and scores greater than 15")
print(df[(df['attempts'] < 2) & (df['score'] > 15)], "\n")

print("Data with Names in Descending Order")
df_name = df.sort_values(by = ['name', 'score'], ascending = [False, True])
print(df_name, "\n\n")

#%% prob2
'''
1- Write a Pandas program to create and display a DataFrame df from "test_last_name.csv"
2- Write a program to create a list with elements correspond to last names (not hand written)
lst = ['Won', 'Yasich', 'Idle']
3- Write a Pandas program to add a new column to df called 'LastName'. The new column has values of 'lst' created in q2.
4- Write a Pandas program to sort the DataFrame by 'LastName' in descending order
5- Write a Pandas program to delete the 'LastName' column
'''
#-------------------------------------------------------------------------------



#%% prob3
'''
A company has a dataset of customer orders, which includes the following columns:

customer_id: A unique identifier for each customer.
order_date: The date on which the order was placed.
order_total: The total amount of the order.
product_id: The unique identifier for each product purchased.
quantity: The number of units of each product purchased.
Write a pandas program to do the following:

1- Read the dataset into a pandas DataFrame 'orders.csv'.
2- Calculate the total sales for each customer.
3- Identify the top 10 customers by total sales.
4- Calculate the average order value for each customer.
5- Identify the top 10 products by total sales.
'''

# Part 1
path_name = '/Users/christopherlee/Desktop/UMD/Courses/ENBC 311/ENBC 311 - Exercises/ENBC 311 - Exercises Week11/'
file_name = 'orders.csv'
df_orders = pd.read_csv(path_name + file_name)

# Part 2
print("Total Sales\n", df_orders['order_total'].sum(), "\n")

# Part 3
df_sales = df_orders.sort_values(by=['order_total'], ascending=[False])
print("Top 10 total customers by sales\n", df_sales.head(10), "\n")

# Part 4
df_orders['avg_order_value'] = df_orders['order_total'] / df_orders['quantity']
print("Average order value for each customer\n", df_orders, "\n")

# Part 5
top_prod = df_orders.groupby('product_id')['order_total'].sum()
top_prod = top_prod.sort_values(ascending=False)
print("Top 10 total products by sales\n", top_prod) 
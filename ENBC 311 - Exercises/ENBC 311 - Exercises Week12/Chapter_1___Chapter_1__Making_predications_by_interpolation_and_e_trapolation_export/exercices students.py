#%% Exercice 1
'''
q1- Create an array t, the independent variable. t 
should run from 0 to 20 in steps of 1.

q2- Create a "table" of the function to be interpolated. 
We will use the exponential function y = exp(t/10)*sin(t). 
Calculate the value of y for all the points in the t array.

q3- Now use the interp1d method in scipy to make a cubic 
interpolation of the table of values y to a new array with
 points running from 0 to 20 in steps of 0.01.
 
q4- Plot the original table as points and the interpolated 
array that you calculate with the spline function.
'''
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

t = np.arange(0, 21)
y = np.exp(t/10)*np.sin(t)
f = interpolate.interp1d(t, y)


xnew = np.arange(0, 9, 0.1)
ynew = f(xnew)

plt.plot(t, y, 'o', xnew, ynew, '-*')
plt.show()


#%% Exercice 2
'''
Write a Pandas program to interpolate the missing values using the Linear 
Interpolation method in a given DataFrame. 
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
'purch_amt':[150.5,np.nan,65.26,110.5,948.5,np.nan,5760,1983.43,np.nan,250.45, 75.29,3045.6],
'sale_amt':[10.5,20.65,np.nan,11.5,98.5,np.nan,57,19.43,np.nan,25.45, 75.29,35.6],
'ord_date': ['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]})
print("Original Orders DataFrame:")
print(df) 
'''
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.DataFrame({
'ord_no':[70001,np.nan,70002,70004,np.nan,70005,np.nan,70010,70003,70012,np.nan,70013],
'purch_amt':[150.5,np.nan,65.26,110.5,948.5,np.nan,5760,1983.43,np.nan,250.45, 75.29,3045.6],
'sale_amt':[10.5,20.65,np.nan,11.5,98.5,np.nan,57,19.43,np.nan,25.45, 75.29,35.6],
'ord_date': ['2012-10-05','2012-09-10',np.nan,'2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3002,3001,3001,3003,3002,3001,3001,3004,3003,3002,3001,3001],
'salesman_id':[5002,5003,5001,np.nan,5002,5001,5001,np.nan,5003,5002,5003,np.nan]})
print("Original Orders DataFrame:")
print(df) 


# df = df.interpolate(method='polynomial', order = 3)
# print(df)

df['ord_no'] = df['ord_no'].interpolate(method='polynomial', order = 3)
df['purch_amt'] = df['purch_amt'].interpolate(method='linear')
df['sale_amt'] = df['sale_amt'].interpolate(method='polynomial', order = 3)
print(df) 


#%% Exercise3: perfrom 2D Interpolation of Missing Data Points (NaN)
#ttps://scipython.com/book/chapter-8-scipy/examples/two-dimensional-interpolation-with-scipyinterpolategriddata/

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Example 2D array with NaN values
data = np.array([
    [1, 2, 3],
    [4, np.nan, 6],
    [7, 8, 9]
])

x = np.arange(0, 3)
y = np.arange(0, 3)
X, Y = np.meshgrid(x, y)

X = X.flatten()
Y = Y.flatten()
data_flat = data.flatten()

mask_valid = ~np.isnan(data_flat)
x_valid = X[mask_valid]
y_valid = Y[mask_valid]
data_valid = data_flat[mask_valid]

x_nan = X[~mask_valid]
y_nan = Y[~mask_valid]
data_interpolated = interpolate.griddata((x_valid, y_valid), data_valid, (x_nan, y_nan), method='cubic')
data_flat[~mask_valid] = data_interpolated
data_corrected = data_flat.reshape(data.shape)
print(data_corrected)

#%%
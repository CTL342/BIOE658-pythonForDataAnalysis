import numpy as np
from sklearn import datasets


#############-------------------------- Start ------------------------------######
#%% step 1: load the data and scout them first
housing = datasets.fetch_california_housing()
x = housing.data
y = housing.target 

print("DATASET COLUMN NAMES:\n", housing.feature_names)
print("-----------------------")
print("nuber of rows:", len(x))
print("nuber of columns:", len(housing.feature_names))


print(type(x))
print(x[0])
print(type(y))
print(y[0])
print(x.shape)

#%% step 2: Train and Test Split
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, 
    y, 
    test_size=0.2,
    random_state=432
)

print("number of train samples:", len(x_train))
print("number of test samples:", len(x_test))


#%% step 3: train the model using the training datasets
from sklearn.linear_model import LinearRegression

# choose algorithm
model = LinearRegression()
# train model on the train set
model.fit(x_train, y_train)

#%% step 4: Test the model on unseen data (test datasets)
from sklearn.metrics import r2_score

# get the model to "guess" the dollar value of the houses in the test sample
y_pred = model.predict(x_test)
# compare what the model "guessed" with the actual value from y_test
r2 = r2_score(y_test, y_pred)

print("R2 Score:", r2)

#%% step 5 save the model:
import joblib
# save model
joblib.dump(model, "my_model.joblib")


# to to reload and reuse the model without retraining:
'''
saved_model = joblib.load("my_model.joblib")
# evaluate saved model
y_pred = saved_model.predict(x_test)
r2 = r2_score(y_test, y_pred)
print("saved model score:", r2)
'''
#############-------------------------- Done ------------------------------######
#%%
#############-------------------------- Optimize Algorithms ------------------------------######

from sklearn.ensemble import (
    GradientBoostingRegressor, 
    RandomForestRegressor
)

# initialize models
LR = LinearRegression()
GBR = GradientBoostingRegressor()
RFR = RandomForestRegressor(n_jobs=-1)
#%%
LR.fit(x_train, y_train)
y_pred = LR.predict(x_test)
r2 = r2_score(y_test, y_pred)
print("MODEL:", 'LR')
print("R2 SCORE:", r2)
print("-------------")
#%%
GBR.fit(x_train, y_train)
y_pred = GBR.predict(x_test)
r2 = r2_score(y_test, y_pred)
print("MODEL:", 'GBR')
print("R2 SCORE:", r2)
print("-------------")

#%%
RFR.fit(x_train, y_train)
y_pred = RFR.predict(x_test)
r2 = r2_score(y_test, y_pred)
print("MODEL:", 'RFR')
print("R2 SCORE:", r2)
print("-------------")
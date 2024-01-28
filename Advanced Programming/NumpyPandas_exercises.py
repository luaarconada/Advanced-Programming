# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:29:42 2023

@author: Usuario
"""

import numpy as np

############################# Exercise 1 #############################
#Create a 3x5 matrix of normal random numbers 
my_matrix = np.random.randn(3,5)
print(my_matrix)

#Introduce missing values
x=[0,2]
y=[3,1]
my_matrix[x,y]=np.nan
#We make elements (0,3) and (2,1) of the matrix as missing values
print(my_matrix)

#Replace the missing values by a 0
my_matrix[np.isnan(my_matrix)]=0
print(my_matrix)


############################# Exercise 2 #############################
#Create a 3x5 matrix of normal random numbers 
my_matrix = np.random.randn(3,5)
print(my_matrix)

#Create the vectors of the maximun and minimun of the columns
maxima= my_matrix.max(axis=0)
print(maxima)
minima= my_matrix.min(axis=0)
print(minima)

#Normalize the elements
normalized_matrix = (my_matrix - minima)/(maxima - minima)
print(normalized_matrix)

#Check that the normalized values are between 0 and 1
normalized_matrix>=0
normalized_matrix<=1

#Standarize the elements
standarized_matrix = (my_matrix - my_matrix.mean(axis=0))/(my_matrix.std(axis=0))
print(standarized_matrix)

#Check that the mean of the columns are 0 and the standard deviation almost 1
standarized_matrix.mean(axis=0)
standarized_matrix.std(axis=0)


############################# Exercise 3 #############################
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import tree

#Obtain the data
# Getting the data
from sklearn.datasets import fetch_california_housing
# Fetch the dataset
california_housing = fetch_california_housing()
# The dataset is now loaded as a Bunch object
# You can access the data (features) and target (labels) like this:
X = california_housing.data
y = california_housing.target
# Feature names can be accessed as well
feature_names = california_housing.feature_names
# For a description of the dataset
print(california_housing.DESCR)


#Split in train and evaluate data
regr = tree.DecisionTreeRegressor(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state= 0)
regr.fit(X_train, y_train)
y_test_pred = regr.predict(X_test)
print(metrics.mean_squared_error(y_test, y_test_pred)) 

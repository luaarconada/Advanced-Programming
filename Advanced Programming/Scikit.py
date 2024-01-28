# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

############################# Exercise ? #############################
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split, GridSearchCV, KFold, RandomizedSearchCV
from sklearn import metrics
from scipy.stats import randint as sp_randint
iris = load_iris()
X = iris.data
y = iris.target
# Defining the train/test partitions
# random_state is for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state=0)
# Defining the method
clf = tree.DecisionTreeClassifier(random_state=0)


# Defining the Search space
param_grid = {'max_depth':sp_randint (2,16),'min_samples_split':sp_randint (2,34)}
# Defining a 5 fold crossvalidation grid search
cv=KFold(n_splits=5, shuffle=True, random_state=0)
clf_rnd =RandomizedSearchCV(clf ,param_grid,scoring='accuracy',cv=cv ,n_jobs=1, verbose=1,random_state=0)
# Training the model with the grid search
# Fit does hyper parameter tuning, followed by training the model with the best hyper parameters found
clf_rnd.fit(X_train, y_train)
# Making predictions on the testing partition
y_test_pred = clf_rnd.predict(X_test)
# And finally computing the test accuracy (model evaluation or outer evaluation
print(metrics.accuracy_score(y_test_pred, y_test))





from sklearn.neighbors import KNeighborsRegressor 
from sklearn.metrics import mean_absolute_error

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
regr = KNeighborsRegressor()
#Defining the Search space
param_grid={'n_neighbors':range(2,16,2)}
#Defining a 3 fold crossvalidation grid search
cv = KFold(n_splits=3, shuffle=True, random_state=42)
regr_grid=GridSearchCV(regr,
param_grid,
scoring='neg_mean_absolute_error',
cv=cv,
n_jobs=1, verbose=1)
regr_grid.fit(X_train, y_train)
y_predictions_test = regr_grid.predict(X_test)
print(f"Model evaluation / outer evaluation: {mean_absolute_error(y_test, y_predictions_test)}")
print(f'Best hyperparameters: {regr_grid.best_params_} and inner evaluation: {regr_grid.best_score_}')

final_model=regr.grid.fit(X,y)x

'''
Created on 26 Jun 2013

@author: Ash Booth
'''

import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation as cv

data_file = "???"

data = np.genfromtxt(data_file+".csv",delimiter=',')
features = data[:,:-1]
targets  = data[:,-1] 

(train_features, test_features, 
 train_targets, test_targets) = cv.train_test_split(features, targets, 
                                                    test_size=0.3, 
                                                    random_state=1)
def findBestParams():
    rfr = RandomForestRegressor(n_jobs=-1)
    pipe = Pipeline(steps=[('rfr', rfr)])
    n_estimators = [5, 10, 15]
    max_depth = [None, 3, 5, 7]
    estimator = GridSearchCV(pipe, dict(rfr__max_depth=max_depth, 
                                        rfr__n_estimators=n_estimators))
    # Fit model
    estimator.fit(train_features,train_targets)
    
    # Run on test set
    cv_score = estimator.score(train_features, train_targets)
    test_score = estimator.score(test_features, test_targets)
    
    
       




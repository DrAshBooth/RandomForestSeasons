'''
Created on 25 Jun 2013

@author: Ash Booth

'''
from sklearn.ensemble import RandomForestRegressor
from expert import Expert

class Prediction(object):
    def __init__(self, features, targets, window_size, nef, max_experts):
        self.date = None
        self.trading_days_seen=1
        self.start_trading_after=50
        self.experts = []
        self.window_size = window_size
        self.nef = nef # new expert frequency
        self.max_experts = max_experts
        self.threshold = 0.2
        self.previeous_pred = 0.0
        self.prediction = 0.0
        self.features = features
        self.targets = targets
        
    def createExpert(self, row_index, verbose):
        training_features = self.features[row_index-self.window_size:row_index,:]
        training_targets = self.targets[row_index-self.window_size:row_index]
        
        # Generate classifer
        rfr = RandomForestRegressor(n_estimators=10, n_jobs=-1)
        if verbose: print "generating random forest regressor"
        rfr.fit(training_features, training_targets)
        # Add to list
        self.experts.append(Expert(rfr, self.trading_days_seen, 
                                   self.nef, len(self.experts)==0))
        
    def makePrediction(self, row_index, verbose):
        
        test_feature = self.features[row_index,:]
        test_target = self.targets[row_index]
        
        self.previeous_pred = self.prediction
        # is it time to make a new expert
        if self.trading_days_seen%self.nef==1:
            self.createExpert(row_index, verbose)
        
        
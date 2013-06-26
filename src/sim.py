'''
Created on 25 Jun 2013

@author: Ash Booth
'''
from prediction import Prediction

import numpy as np
from sklearn import cross_validation as cv

class Simulation:
    
    def __init__(self, balance, data_file, window_size = 50, 
                 nef=5, max_experts=48):
        self.nef = nef
        self.window_size = window_size
        self.max_experts = max_experts
        self.balance = balance
        self.profit = 0
        self.stock_held = 0
        
        # Data
        self.data_file
        self.features = None
        self.targets = None
        
        # Stats
        self.returns = []
        self.correct_preds
        self.correct_buys
        self.correct_sells
        
    def __loadData(self):
        data = np.genfromtxt(self.data_file+".csv",delimiter=',')
        self.features = data[:,:-1]
        self.targets  = data[:,-1] 
      
    def writeStats(self):
        # write the above
        # calc f-scores etc etc and write the
        pass
    
    def run(self, verbose):
        # Training
        predictor = Prediction(self.features, self.targets, 
                               self.window_size, self.nef, self.max_experts)
        for row_index in range(self.window_size,len(self.features)):
            pred = predictor.makePrediction(row_index, verbose)
            # make prediction (including risk management)

            # update profit
            # update stats
        pass
    

        
        
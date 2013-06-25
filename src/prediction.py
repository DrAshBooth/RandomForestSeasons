'''
Created on 25 Jun 2013

@author: Ash Booth

'''

import numpy as np

class Prediction(object):
    def __init__(self, nef=5, max_experts=48):
        self.date = None
        self.trading_days_seen=1
        self.start_trading_after=50
        self.experts = []
        self.new_exp_freq = nef
        self.max_experts = max_experts
        self.threshold = 0.2
        self.previeous_pred = 0.0
        self.prediction = 0.0
        self.__loadData()
    
    def __loadData(self):
        full_data = np.genfromtxt("stock_metrics.csv",delimiter=',')
        
    def makePrediction(self, date):
        # is it time to make a new expert
        self.date = date
        
        
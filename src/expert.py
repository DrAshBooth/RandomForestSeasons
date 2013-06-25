'''
Created on 25 Jun 2013

@author: Ash Booth
'''

def __init__(self, predictor, time, next_in, first):
    '''
    Constructor
    '''
    self.predictor = predictor
    self.born_at = time
    self.next_ariving_at = time+next_in
    self.first = first
    self.cummulative_return = 0.0
    self.initial_weight = None
    self.weight = None
    self.prediction=None

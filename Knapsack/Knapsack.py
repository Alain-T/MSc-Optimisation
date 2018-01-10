# -*- coding: utf-8 -*-

class Knapsack(object):
  """Knapsack solver using dynamic programming"""

  def __init__(self):
    self.memo = None
    self.max_objects = 0
    self.max_weight = 0


  def initialize(self, max_objects, max_weight):
    self.memo = dict()
    self.max_objects = max_objects
    self.max_weight = max_weight


  def pair(self, k, W):
    return (k, W)
    
  
  def knapsack(self, weight, value, k, W, clear = True):
    if clear:
      self.initialize(k, W)

    # check for the obvious case (no object to be added into the bag)
    if k == 0:
      # no object means no value
      return (0, () )
    else:
      # create a unique identifier the current case (number of objects, remaining weight)
      key = self.pair(k, W)
      
      # check if the optimal value for that case is already known
      if key not in self.memo:
        # solution for that case is unknown:
        # the algorithm will check if the last object of the set can be added
        # into the bag, relying upon the solution for k - 1 objects
        
        # check if the weight of the last object exceeds the remaining weight
        if weight[k - 1] > W:
          # the current object cannot fit into the bag; drop it
          self.memo[key] = self.knapsack(weight, value, k - 1, W, False)
        else:
          # the last object could fit into the bag, pick the maximum value of:

          # - dropping the last object (and keeping the remaining weight for the others)
          ks_1 = self.knapsack( weight, value, k - 1, W, False )

          # - adding the object into the bag (and consumming some of the remaning weight)
          ks_2 = self.knapsack( weight, value, k - 1, W - weight[k - 1], False )
          v2 = ks_2[0] + value[k - 1]
          
          if ks_1[0] < v2:
            self.memo[key] = (v2, ks_2[1] + (k - 1,) )
          else:
            self.memo[key] = ks_1
            
          # self.memo[key] = max(
          #    self.knapsack( weight, value, k - 1, W, False ),
          #    self.knapsack( weight, value, k - 1, W - weight[k - 1], False )
          #      + value[k - 1])
    
    return self.memo[key];
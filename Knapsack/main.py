# -*- coding: utf-8 -*-

from Knapsack import Knapsack


def knapsack(weight, value, max_weight):
  knap_sack = Knapsack()
  ks = knap_sack.knapsack(weight, value, len(weight), max_weight )
  print(ks)
  
  v = 0
  w = 0
  for i in ks[1]:
    v += value[i]
    w += weight[i]
    print('{}: w={} v={}; s(w)={} s(v)={}'.format(i, weight[i], value[i], w, v))
    

def main():
  weight = [ 15, 12, 10, 9, 8, 7, 5, 4, 3, 1]
  value  = [ 210, 220, 180, 120, 160, 170, 90, 40, 60, 10 ]
  knapsack(weight, value, 26)
  
  # weight = [ 4, 4, 9, 9, 9, 6, 6, 6, 6, 6]
  # value  = [ 8, 8, 3, 3, 3, 2, 2, 2, 2, 2 ]
  
  # knap_sack = Knapsack()
  # print(knap_sack.knapsack(weight, value, 10, 26 ))
  # print(knap_sack.knapsack(weight, value, 10, 11 ))
  
  
if __name__ == '__main__':
  main()
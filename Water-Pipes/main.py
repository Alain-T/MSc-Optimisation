# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:54:59 2017

@author: atholon
"""
import os

from Epanet import read_epanet_file
from WaterNetwork import WaterNetwork
  
          
def get_bounding_valves(connected_junctions, valves):
  bounding_valves = list()
  for valve_id, junctions in valves.items():
    nb_junction_found = 0
    for junction in junctions:
      if junction in connected_junctions:
        nb_junction_found += 1
    
    if True:
      # sanity check; check that nb_junction_found is 0, 1 or 2
      if nb_junction_found not in [0, 1, 2]:
        print("ERROR number of valve junction mismatch: {}".format(nb_junction_found))
     
      
    # a bounding valve only has one junction in the subgraph
    if nb_junction_found == 1:
      bounding_valves.append(valve_id)

  return  bounding_valves


def main():
  input_filename = 'network.inp'
  input_filename = 'pd2.inp'
  
  input_filename_base = os.path.splitext(input_filename)[0]
    
  ressources = read_epanet_file(input_filename)
  
  all_pipes = ressources["pipes"]
  all_valves = ressources["valves"]
  all_tanks = ressources["tanks"]
  all_reservoirs = ressources["reservoirs"]

  if False:
    # debug information
    pipe_filename = "{}-pipes.txt".format(input_filename_base)
    with open(pipe_filename, 'w') as output_file:
      for pipe_id, nodes in all_pipes.items():
        print('{} : {}'.format(pipe_id, nodes), file=output_file)
  
  water_network = WaterNetwork()
  
  pipe_id_mapping = dict()
  for pipe_id, nodes in all_pipes.items():
    unique_pipe_id = water_network.get_pipe_id(nodes[0], nodes[1])
    if unique_pipe_id is None:
      water_network.add_pipe(nodes[0], nodes[1], pipe_id, nodes[2])
      pipe_id_mapping[pipe_id] = pipe_id
    else:
      pipe_id_mapping[pipe_id] = unique_pipe_id

  # group the junctions of all water sources (tanks and reservoirs)
  all_water_source_junctions = set(all_tanks)
  all_water_source_junctions |= set(all_reservoirs)

  if len(all_pipes) == len(pipe_id_mapping):
    # water_network.dump()
    
    # split the graph in a set of connected subgraph
    all_connected_junctions = water_network.get_all_connected_junctions()        
    print("number of connected subgraph found : {}".format(len(all_connected_junctions)))

    bounding_valves_mapping = dict()
    water_sources_mapping = dict()
    for connected_junctions in all_connected_junctions:
      # find the bounding valves of the subgraph
      bounding_valves = get_bounding_valves(connected_junctions, all_valves)

      # find the water sources inside the connected graph
      water_sources = set.intersection(all_water_source_junctions, connected_junctions)
      
      for junction in connected_junctions:
        bounding_valves_mapping[junction] = bounding_valves
        water_sources_mapping[junction] = water_sources
        
    output_filename = "{}-output.txt".format(input_filename_base)
        
    with open(output_filename, 'w') as output_file:
      for pipe_id, nodes in all_pipes.items():
        print('{} -> water_sources={} bounding_valves={}'.format(
            pipe_id,
            water_sources_mapping[nodes[0]],
            bounding_valves_mapping[nodes[0]]), file=output_file)
        
  else:
    print("ERROR number of pipes mismatch: {} - {}".format(len(all_pipes), len(pipe_id_mapping)))
   
    
if __name__ == '__main__':
  main()
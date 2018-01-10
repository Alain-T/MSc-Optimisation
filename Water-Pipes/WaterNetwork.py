# -*- coding: utf-8 -*-

class WaterNetwork(object):
  """Graph using adjacency list"""

  def __init__(self):
    self.junctions = dict()


  def add_junction(self, junction):
    """Add a junction to the graph"""
    if junction not in self.junctions:
      pipes = dict()
      self.junctions[junction] = pipes


  def add_pipe(self, origin, destination, pipe_id, status):
    """Add a pipe_idd edge to the graph"""

    self.add_junction(origin)
    self.add_junction(destination)

    if True:
      # sanity check
      if (destination in self.junctions[origin]):
        print('ERROR: add_pipe: duplicate')
        print('{}-{}:{} / {}'.format(origin, destination, self.junctions[origin][destination], pipe_id))
  
      if (origin in self.junctions[destination]):
        print('ERROR: add_pipe: duplicate')
        print('{}-{}:{} / {}'.format(destination, origin, self.junctions[destination][origin], pipe_id))
      
    # make the pipe bidirectional    
    if status == 'Open' or status =='CV':
      self.junctions[origin][destination] = pipe_id
      
    if status == 'Open':
      self.junctions[destination][origin] = pipe_id


  def get_pipe_id(self, origin, destination):
    pipe_id = None
    if origin in self.junctions:
      if destination in self.junctions[origin]:
        pipe_id = self.junctions[origin][destination]
    
    return pipe_id
	

  def dump(self):
    print("pipes:")
    for origin, adjacents in self.junctions.items():
      print("{}->{}".format(origin, adjacents))

    
  def get_connected_junctions(self, start):
    """ get all connected junctions from a graph using breadth first algorithm"""
    
    stack = list()
    visited = list()
    
    visited.append(start)
    stack.append(start)

    while len(stack) != 0:
      # get first junction
      junction = stack.pop(0)
 
      for next_junction in self.junctions[junction]:
        if next_junction not in visited:
          visited.append(next_junction)
          stack.append(next_junction)
          
    return visited

  
  def get_all_connected_junctions(self):
    all_connected_junctions = list()
    explored_junctions = list() 
    for junction in self.junctions:
      if junction not in explored_junctions:
        connected_junctions = self.get_connected_junctions(junction)
        explored_junctions.extend(connected_junctions)
        all_connected_junctions.append(connected_junctions)

    if True:
      # sanity check
      n = 0
      for connected_junction in all_connected_junctions:
        n += len(connected_junction)
      if n != len(self.junctions):
        print('ERROR: get_all_connected_junctions: inconsistent result')
    
    return all_connected_junctions;
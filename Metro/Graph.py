# -*- coding: utf-8 -*-

class Graph(object):
  """Graph using adjacency list"""

  def __init__(self):
    self.vertices = dict()


  def add_vertex(self, vertex):
    """Add a vertex to the graph"""
    if vertex not in self.vertices:
      edges = dict()
      self.vertices[vertex] = edges


  def add_edge(self, origin, destination, duration):
    """Add an edge to the graph"""

    self.add_vertex(origin)
    self.add_vertex(destination)

    self.vertices[origin][destination] = duration


  def get_vertices(self):
    """get the list of all vertices of the graph"""
    return self.vertices.keys()


  def get_duration(self, origin, destination):
    """get the duration of an edge"""
    return self.vertices[origin][destination]


  def get_closest_unvisited_vertex(self, visited, path_length):
    """ return the closer unvisited vertex  """
    distance = float("inf")
    closer_unvisited_vertex = None

    for vertex in self.vertices:
      if not visited[vertex] and path_length[vertex] < distance:
        distance = path_length[vertex]
        closer_unvisited_vertex = vertex

    return closer_unvisited_vertex
          

  def get_shortest_path_dijkstra(self, start):
    """ return shortex path array using dijkstra algorithm  """

    visited = dict()
    path_length = dict()
    predecessor = dict()
    for vertex in self.vertices:
      visited[vertex] = False
      path_length[vertex] = float("inf")
      predecessor[vertex] = None
      
    path_length[start] = 0

    vertex = self.get_closest_unvisited_vertex(visited, path_length)
    while vertex is not None:
      visited[vertex] = True
      for next_vertex in self.vertices[vertex]:
        if path_length[vertex] + self.vertices[vertex][next_vertex] < path_length[next_vertex]:
          path_length[next_vertex] = path_length[vertex] + self.vertices[vertex][next_vertex]
          predecessor[next_vertex] = vertex
      vertex = self.get_closest_unvisited_vertex(visited, path_length)

    return visited, path_length, predecessor
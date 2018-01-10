import math

class Graph(object):
  """Graph using adjacency list"""

  def __init__(self):
    self.vertices = dict()


  def add_vertex(self, vertex):
    """Add a vertex to the graph"""
    if vertex not in self.vertices:
      edges = dict()
      self.vertices[vertex] = edges


  def add_edge(self, origin, destination, weight):
    """Add an edge to the graph"""

    self.add_vertex(origin)
    self.add_vertex(destination)

    self.vertices[origin][destination] = weight


  def get_vertices(self):
    """get the list of all vertices of the graph"""
    return self.vertices.keys()


  def get_reachable_vertices(self, origin):
    """returns the list of reachable vertex from a given one"""

    # initialize the list of vertices that can be reached from the origin
    reachable_vertices = list()

    if origin in self.vertices:
      # when starting, the list of vertices to be explored are those adjacent from the origin
      vertices_to_be_explored = list(self.vertices[origin].keys())

      # while some vertices remains to be explored
      while len(vertices_to_be_explored) > 0:

        # get the next vertex to explore
        current_vertex = vertices_to_be_explored.pop()

        # check if it has not been reached yet
        if current_vertex not in reachable_vertices:

          # newly reached vertex, add it to the list
          reachable_vertices.append(current_vertex)

          # check the adjacent vertices of the current vertex
          for next_vertex in self.vertices[current_vertex]:

            # check if the adjacent vertex has not been reached yet
            if next_vertex not in reachable_vertices:

              # check if the adjacent vertex is not already pending to be explored
              if next_vertex not in vertices_to_be_explored:

                # brand new vertex; needs to be explored
                vertices_to_be_explored.append(next_vertex)

    return reachable_vertices;


  def is_strongly_connected(self):
    """check if the graph is strongly connected or not"""
    is_strongly_connected = True

    # for each vertex, check if it is connected to all others
    vertices_to_be_checked = list(self.vertices.keys())
    while len(vertices_to_be_checked) > 0 and is_strongly_connected:

      # get the current vertex
      current_vertex = vertices_to_be_checked.pop()

      # get all the reachable vertex from the current one
      reachable_vertices = self.get_reachable_vertices(current_vertex)

      # check if the current vertex can reach itself
      if current_vertex in reachable_vertices:
        # if the current vertex can reach itself, all vertices of the graph must be reachable
        if len(reachable_vertices) != len(self.vertices.keys()):
          is_strongly_connected = False
      else:
        # if the current vertex cannot reach  itself, all other vertices of the graph must be reachable
        if len(reachable_vertices) != (len(self.vertices.keys()) - 1):
          is_strongly_connected = False    

    return is_strongly_connected;
    

  def has_a_cycle(self):
    """check if the graph has at least one cycle"""
    has_a_cycle = False

    # for each vertex, check if it is part of cycle
    vertices_to_be_checked = list(self.vertices.keys())
    while len(vertices_to_be_checked) > 0 and not has_a_cycle:

      # get the current vertex
      current_vertex = vertices_to_be_checked.pop()

      # get all the reachable vertices from the current one
      reachable_vertices = self.get_reachable_vertices(current_vertex)

      # check if the current vertex can reach itself
      if current_vertex in reachable_vertices:
        has_a_cycle = True    

    return has_a_cycle;


  def get_vertex_degrees(self, origin):
    """get the in and out degrees of a given vertex"""
    out_degree = 0
    in_degree  = 0

    # the out degree is the number of adjacent vertices to the given vertex
    if origin in self.vertices:
      out_degree = len(self.vertices[origin].keys())

    # count the number of vertex "pointing" to the given vertex
    for vertex in self.vertices:
      if origin in self.vertices[vertex].keys():
        in_degree += 1

    return (in_degree, out_degree)


  def dump(self):
    """dump the graph vertices and edges"""
    for key in self.vertices:
      print("{}:{}".format(key, self.vertices[key]))


  def breadth_first_traverval(self, first):
    """ visit all vertices of a graph using breadth first algorithm"""
    stack = list()
    visited = list()

    visited.append(first)
    stack.append(first)

    while len(stack) != 0:
      # get first element
      vertex = stack.pop(0)

      # process vertex
      print("{}".format(vertex))

      for next_vertex in self.vertices[vertex]:
        if next_vertex not in visited:
          visited.append(next_vertex)
          stack.append(next_vertex)


  def depth_first_traverval(self, first):
    """ visit all vertices of a graph using depth first algorithm"""
    stack = list()
    visited = list()

    visited.append(first)
    stack.append(first)

    while len(stack) != 0:
      # get last element
      vertex = stack.pop()

      # process vertex
      print("{}".format(vertex))

      for next_vertex in self.vertices[vertex]:
        if next_vertex not in visited:
          visited.append(next_vertex)
          stack.append(next_vertex)


  def depth_first_traverval_recurs_low(self, visited, vertex):
    """ sub function to implement recursive version of graph depth first traversal """
    # process vertex
    print("{}".format(vertex))

    for next_vertex in self.vertices[vertex]:
      if next_vertex not in visited:
        visited.append(next_vertex)
        self.depth_first_traverval_recurs_low(visited, next_vertex)


  def depth_first_traverval_recursive(self, first):
    """ visit all vertices of a graph using depth first algorithm - recursive version"""
    visited = list()
    visited.append(first)

    self.depth_first_traverval_recurs_low(visited, first)


  def get_in_degrees(self):
    """ return the in degrees of all vertices """
    in_degrees = dict()

    # initialize the in-degree of all vertices
    for vertex in self.vertices:
      in_degrees[vertex]= 0

    # iterate over each edge
    for origin in self.vertices:
      for destination in self.vertices[origin]:
        # increment the in degree of the destination vertex of the current edge
        in_degrees[destination] += 1

    return in_degrees


  def get_topological_sort(self):
    """ return a topological sort for the graph if it exists or None otherwise """

    in_degrees = self.get_in_degrees()

    # for debugging purposes
    if False:
      keys=list(in_degrees.keys())
      keys.sort()
      for key in keys:
        print("{}:{}".format(key, in_degrees[key]))


    queue = list()

    # queue indexes: write on tail, read from head
    index_head = 0
    index_tail = -1

    # push all source vertices into the queue
    for vertex in list(in_degrees.keys()):
      if in_degrees[vertex] == 0:
        index_tail += 1
        # add an element at the end of the queue; Python's way
        queue.append(vertex)

    # while the queue is not empty
    while index_head < index_tail + 1:

      # pop the front vertex from the queue
      current_vertex = queue[index_head]
      index_head += 1

      # decrement the in-­degree of each neighbor of the current vertex
      for next_vertex in self.vertices[current_vertex]:
        in_degrees[next_vertex] -= 1

        # if the neighbor now has an in degree of 0, add it to the queue
        if in_degrees[next_vertex] == 0:
          index_tail += 1
          queue.append(next_vertex)
      
    if len(queue) == len(self.vertices):
      return queue
    else:
      return None


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

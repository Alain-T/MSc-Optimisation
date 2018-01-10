from Graph import Graph

#
# Day 1 exercices
#
def get_graph_10():
  graph = Graph()

  for origin in range(0, 3):
    for destination in range(0, 3):
      if (origin != destination):
        graph.add_edge(origin, destination, origin * 1000 + destination)

  return graph;


def get_graph_11():
  graph = Graph()

  graph.add_edge(0, 1, 0)
  graph.add_edge(1, 2, 0)
  graph.add_edge(1, 3, 0)
  graph.add_edge(2, 4, 0)
  graph.add_edge(2, 1, 0)
  graph.add_edge(3, 6, 0)
  graph.add_vertex(10)

  return graph;


def get_graph_12():
  graph = Graph()

  graph.add_edge(0, 1, 0)
  graph.add_edge(1, 2, 0)
  graph.add_edge(2, 3, 0)
  graph.add_edge(3, 4, 0)
  graph.add_edge(4, 5, 0)
  graph.add_edge(5, 0, 0)

  return graph;


def test_graph(graph):
  graph.dump()

  for origin in graph.get_vertices():
    print("{}:get_vertex_degrees={}".format(origin, graph.get_vertex_degrees(origin)))

  for origin in graph.get_vertices():
    print("{}:get_reachable_vertices={}".format(origin, graph.get_reachable_vertices(origin)))

  print("is_strongly_connected={}".format(graph.is_strongly_connected()))
  print("has_a_cycle={}".format(graph.has_a_cycle()))


def graph_connection_tests():
  """first homework on graph connection, in and out degrees, cycle detection"""
  test_graph(get_graph_10())
  print("")

  test_graph(get_graph_11())
  print("")

  test_graph(get_graph_12())
  print("")


#
# Day 3 exercices
#
def get_graph_20():
  graph = Graph()

  graph.add_edge(0, 10, 0)
  graph.add_edge(0, 20, 0)

  graph.add_edge(10, 100, 0)
  graph.add_edge(10, 110, 0)

  graph.add_edge(100, 1000, 0)
  graph.add_edge(110, 1100, 0)

  graph.add_edge(1000, 10000, 0)
  graph.add_edge(1100, 11000, 0)

  graph.add_edge(20, 200, 0)
  graph.add_edge(20, 210, 0)

  graph.add_edge(200, 2000, 0)
  graph.add_edge(210, 2100, 0)

  graph.add_edge(2000, 20000, 0)
  graph.add_edge(2100, 21000, 0)

  return graph;


def get_graph_21():
  graph = Graph()

  graph.add_edge('H', 'D', 0)
  graph.add_edge('H', 'I', 0)

  graph.add_edge('C', 'D', 0)

  graph.add_edge('I', 'J', 0)

  graph.add_edge('J', 'F', 0)

  graph.add_edge('D', 'A', 0)
  graph.add_edge('D', 'E', 0)
  graph.add_edge('D', 'F', 0)

  graph.add_edge('A', 'B', 0)

  graph.add_edge('B', 'E', 0)

  graph.add_edge('F', 'E', 0)
  graph.add_edge('F', 'G', 0)

  graph.add_edge('G', 'E', 0)
  graph.add_edge('G', 'L', 0)

  graph.add_edge('F', 'K', 0)

  graph.add_edge('K', 'L', 0)

  return graph;


def graph_traversal_test(graph, first):
  graph.depth_first_traverval(first)
  print("")
  graph.depth_first_traverval_recursive(first)
  print("")
  graph.breadth_first_traverval(first)
  print("")


def graph_traversal_tests():
  graph_traversal_test(get_graph_10(), 0)
  print("")

  graph_traversal_test(get_graph_12(), 0)
  print("")

  graph_traversal_test(get_graph_20(), 0)
  print("")



def topological_sort_tests():
  topological_sort=get_graph_21().get_topological_sort()
  print(topological_sort)

#
# Day 4 exercice
#
def get_graph_30():
  graph = Graph()

  graph.add_edge('A', 'B', 5)
  graph.add_edge('A', 'C', 2)

  graph.add_edge('B', 'D', 6)
  graph.add_edge('B', 'E', 7)

  graph.add_edge('C', 'B', 1)
  graph.add_edge('C', 'D', 4)

  graph.add_edge('D', 'E', 2)

  return graph;

def shortest_path_dijkstra_test(graph, start):
  visited, path_length, predecessor = graph.get_shortest_path_dijkstra(start)
  for vertex in visited:
    print("{}:visited={} predecessor={} shortest_distance={}".
          format(vertex, visited[vertex], predecessor[vertex], path_length[vertex]))


def shortest_path_dijkstra_tests():
  shortest_path_dijkstra_test(get_graph_30(), 'A')


def main():
   # graph_connection_tests()
   # graph_traversal_tests()
   # topological_sort_tests()
   shortest_path_dijkstra_tests()

if __name__ == '__main__':
  main()
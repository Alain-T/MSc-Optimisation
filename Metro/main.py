# -*- coding: utf-8 -*-

import os

from MetroMapFile import read_metro_map_file
from Graph import Graph


def get_vertice_id(question, all_vertices):
  vertice_id = None
  while vertice_id == None:
    text = input(question)
    if (text == '*'):
      vertice_id = '*'
    else:
      if text in all_vertices: 
        vertice_id = text
      else:
        print('Invalid entry, not a vertice id: {}'.format(text))

  return vertice_id


def find_path(vertices, graph, source, destination):
  visited, path_length, predecessor = graph.get_shortest_path_dijkstra(source)
  if (visited[destination]):
    path=list()
    current = destination
    while (current != source):
      path.append(current)
      current = predecessor[current]
    path.append(current)
    path.reverse()

    previous = None
    for vertice in path:
      if previous is None:
        duration = ''
      else:
        duration = graph.get_duration(previous, vertice)
      
      print('{:6} - {:6} - {:4} - {}'.format(path_length[vertice], duration,
            vertice, vertices[vertice]))
      previous = vertice
  else:
    print('not path found from {}({}) to {}({})'.format(
        vertices[source], source, vertices[destination], destination))
    
    
def main():
  input_filename = 'metro_complet.txt'
  
  ressources = read_metro_map_file(input_filename)
  # print(ressources)

  all_vertices = ressources['vertices']
  all_edges = ressources['edges']

  quickest_graph = Graph()
  shortest_graph = Graph()
  
  for source, destination, duration in all_edges:
    quickest_graph.add_edge(source, destination, duration)
    shortest_graph.add_edge(source, destination, 1)

  source = None
  destination = None
  while source != '*' and destination != '*':
    source = get_vertice_id('enter source vertice or * to quit : ', all_vertices)
    if (source != '*'):
      destination = get_vertice_id('enter destination vertice or * to quit : ', all_vertices)
      if (destination != '*'):
        print('quickest path from {}({}) to {}({})'.format(
            all_vertices[source], source, all_vertices[destination], destination))      
        find_path(all_vertices, quickest_graph, source, destination)
        print()
        print('shortest path from {}({}) to {}({})'.format(
            all_vertices[source], source, all_vertices[destination], destination))        
        find_path(all_vertices, shortest_graph, source, destination)
        
if __name__ == '__main__':
  main()
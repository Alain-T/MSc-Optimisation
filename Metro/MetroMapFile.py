# -*- coding: utf-8 -*-


def get_tokens(line):
  """tokenize a line"""
  return line.split()


def read_metro_map_file(filename):
  """read ressources from a metro map input file"""

  sections = ('[Vertices]', '[Edges]')

  vertices = dict();
  edges = list();
  line_number = 0
  section = None
  with open(filename, "r") as input_file:
    for line in input_file:
      line_number += 1
      tokens = get_tokens(line)
      if len(tokens) > 0:
        if tokens[0][:1] == '[':
          # section keyword, check that it ends with a ']'
          if tokens[0][-1:] == ']':
            section = tokens[0]
            if section in sections:
              pass
            else:
              print("ERROR invalid section name at line {} : {}".format(line_number, line))
        else:
          # in section line
          if section is None:
            print("WARNING lines before any section at line {} : {}".format(line_number, line))
          elif section == '[Vertices]':
            # remove leading zeros
            key = tokens[0].lstrip("0")
            if key == '':
              key = '0'
            if key in vertices:
              print("ERROR duplicated key at line {} : {}".format(line_number, line))
            else:
              vertices[key] = ' '.join(tokens[1:])
          elif section == '[Edges]':
            duration = float(tokens[2])
            edges.append((tokens[0], tokens[1], duration))
          else:
            # kind of section not handled
            pass

  # sanity check
  for source, destination, duration in edges:
    if source not in vertices:
      print("ERROR source is not a vertice {} -> {} : {}".format(source, destination, duration))
    if destination not in vertices:
      print("ERROR destination is not a vertice {} -> {} : {}".format(source, destination, duration))
    if duration <= 0:
      print("ERROR invalid duration {} -> {} : {}".format(source, destination, duration))
  
  resources = dict()
  resources["vertices"] = vertices
  resources["edges"] = edges
  
  return resources

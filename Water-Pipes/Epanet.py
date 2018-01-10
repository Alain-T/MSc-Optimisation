# -*- coding: utf-8 -*-


def get_tokens(line):
  """tokenize an Epanet line (i.e. split words; stopping when ; encountered)"""
  tokens=list()
  words=line.split()
  for word in words:
    if word[:1] == ';':
      break
    else:
      tokens.append(word)
  
  return tokens  


def read_epanet_file(filename):
  """read ressources from a epanet input file"""
  pipes = None;
  tanks = None;
  valves = None;
  junctions = None;
  reservoirs = None;
  
  # EPANET file format is documented here :
  # https://github.com/OpenWaterAnalytics/EPANET/wiki/Input-File-Format
  #
  # EPANET parser
  # https://github.com/OpenWaterAnalytics/EPANET/blob/master/src/input3.c
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
            if tokens[0] == '[JUNCTIONS]':
              if junctions is None:
                junctions = dict()
              else:
                print("WARNING duplicated section at line {} : {}".format(line_number, line))                
            elif tokens[0] == '[PIPES]':
              if pipes is None:
                pipes = dict()
              else:
                print("WARNING duplicated section at line {} : {}".format(line_number, line))                
            elif tokens[0] == '[TANKS]':
              if tanks is None:
                tanks = dict()
              else:
                print("WARNING duplicated section at line {} : {}".format(line_number, line))                
            elif tokens[0] == '[RESERVOIRS]':
              if reservoirs is None:
                reservoirs = dict()
              else:
                print("WARNING duplicated section at line {} : {}".format(line_number, line))                
            elif tokens[0] == '[VALVES]':
              if valves is None:
                valves = dict()
              else:
                print("WARNING duplicated section at line {} : {}".format(line_number, line))                
          else:
            print("ERROR invalid section name at line {} : {}".format(line_number, line))
        else:
          # in section line
          if section is None:
            print("WARNING lines before any section at line {} : {}".format(line_number, line))
          elif section == '[JUNCTIONS]':
            pass
          elif section == '[PIPES]':
            if tokens[0] not in pipes:
              # from EPANET file format and parser implementation
              
              # extract pipe status or use default value otherwise
              status = None
              if len(tokens) == 6:
                # no optional status, status is Open per default
                status = 'Open'
              elif len(tokens) == 7:
                # optional status
                status = tokens[-1]
              elif len(tokens) == 8:
                # optional minor loss and optional status
                status = tokens[-1]
              
              # sanity check on pipe status
              if status == 'Open':
                pass
              elif status == 'Closed':
                pass
              elif status == 'CV':
                pass
              else:
                status = None
                
              if status is None:
                print("ERROR invalid pipe format line {} : {}".format(line_number, line))                  
              else:
                # ignore status for now, to be checked with Professor
                status = 'Open'
                pipes[tokens[0]] = (tokens[1], tokens[2], status)
            else:
              # sanity check
              print("duplicated pipes {}".format(tokens[0]))
          elif section == '[VALVES]':
            if tokens[0] not in valves:
              valves[tokens[0]] = (tokens[1], tokens[2])
            else:
              # sanity check
              print("duplicated valves {}".format(tokens[0]))
          elif section == '[TANKS]':
            if tokens[0] not in tanks:
              tanks[tokens[0]] = None
            else:
              # sanity check
              print("duplicated tanks {}".format(tokens[0]))
          elif section == '[RESERVOIRS]':
            if tokens[0] not in reservoirs:
              reservoirs[tokens[0]] = None
            else:
              # sanity check
              print("duplicated reservoirs {}".format(tokens[0]))
          else:
            # kind of section not handled
            pass

  resources = dict()
  resources["pipes"] = pipes
  resources["valves"] = valves
  resources["reservoirs"] = reservoirs
  resources["tanks"] = tanks
  resources["junctions"] = junctions
  
  return resources

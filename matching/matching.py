import networkx as nx
import json
import os
from networkx.algorithms import bipartite
      
B = nx.Graph()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
with open(os.path.join(__location__, 'students.json')) as json_file:
    data = json.load(json_file)
    for p in data:
        print('Name: ' + p)
        print(data[p])







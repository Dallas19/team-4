import networkx as nx
import json
import os
from networkx.algorithms import bipartite
      
B = nx.Graph()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
students = {};
jobs = {};

# fill the student maps and the jobs map
with open(os.path.join(__location__, 'students.json')) as json_file:
    data = json.load(json_file)
    for p in data:
        students[p] = data[p];

with open(os.path.join(__location__, 'jobs.json')) as json_file:
    data = json.load(json_file)
    for p in data:
        jobs[p] = data[p];

B = nx.Graph()

for key, values in jobs.items():
    print(key)
    print(values[0])
    
    for i in range(len(values)):
        for x in range(len(students[values[i]])):
            if students[values[i]][x] == key:
                B.add_weighted_edges_from((key, values[i], abs(x-i)))
                break
        

    

    









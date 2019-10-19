import networkx as nx
from networkx.algorithms import bipartite
from math import inf
from itertools import chain


def match(jobs, students):
  make_graph(jobs, students)
  print(make_graph)

def make_graph(jobs, students):
  B = nx.Graph()
  B.add_nodes_from(jobs.keys(), bipartite=0)
  B.add_nodes_from(students.keys(), bipartite=1)
  B.add_weighted_edges_from( compute_weights(jobs, students) )


def compute_weights(jobs, students):
  weights = []
  func = lambda job, student: get_distance(job, student[1], student[0], students)
  for job in jobs:
    job_weights = list(map(lambda s: func(job, s), enumerate(jobs[job])))
    weights.append(job_weights)

  return list(chain.from_iterable(weights))


def get_distance(job_id, student_id, rank, students):
  try:
    job_rank = students[student_id].index(job_id)
  except ValueError:
    job_rank = inf

  return (job_id, student_id, abs(rank - job_rank - 1))
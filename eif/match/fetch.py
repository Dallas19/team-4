import sqlite3
from itertools import groupby

def connect(path='../db.sqlite3'):
  return sqlite3.connect(path)


def get_jobs(conn):
  c = conn.cursor()

  join_table = c.execute('''
    Select match_student.first_name, match_student.last_name, match_job.name, match_companystudent.rank
    From match_companystudent
    Inner Join match_student On match_companystudent.student_id = match_student.id
    Inner Join match_job On match_companystudent.job_id = match_job.id
  ''')

  return parse_jobs(join_table.fetchall())


def parse_jobs(jobs):
  final = {}
  groups = [(k, v) for k, v in groupby(jobs, key=lambda x: x[2])]
  for job, info in groups:
    ordered = sorted(info, key=lambda x: x[3])
    parsed = list(map(lambda x: x[0] + ' ' + x[1]), ordered)
    final[job] = parsed

  return final



get_jobs(connect())

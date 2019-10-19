import sqlite3

def connect(path='../db.sqlite3'):
  return sqlite3.connect(path)


def get_info(conn):
  c = conn.cursor()

  join_table = c.execute('''
    Select match_student.first_name, match_student.last_name, match_job.name, match_companystudent.rank
    From match_companystudent
    Inner Join match_student On match_companystudent.student_id = match_student.id
    Inner Join match_job On match_companystudent.job_id = match_job.id
    GROUP BY match_job.name
    ORDER BY match_companystudent.rank
  ''')




  print(join_table.fetchall().split())


get_info(connect())

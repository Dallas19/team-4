import sqlite3
def connect(path='../eif/db.sqlite3'):
  return sqlite3.connect(path)


def get_info(conn):
  c = conn.cursor()

  c.execute('''
    Select Student.first_name, Student.last_name, Job.name, CompnayStudent.rank
    From CompanyStudent 
    Left Join Student On CompanyStudent.student = Student.pk
    Left Join Job On CompanyStudent.job = Job.pk 
  ''')
  print(c.fetchone())

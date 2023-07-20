import pyodbc

conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-211231-321\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')

cur = conn.cursor()

cur.execute('SELECT * FROM Training.dbo.S')

for row in cur:
  for value in row:
    print(value, end='')

conn.close()
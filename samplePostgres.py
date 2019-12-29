import psycopg2
from configure import configure

db = configure()
conn = psycopg2.connect(database="cricket", user="swagat", password="Suits@3629", host='localhost',port=5432)
a = 3+5
conn.close()

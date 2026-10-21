import psycopg2

def get_connection():
    try:
        return psycopg2.connect(database="information_db", user="postgres", password="123", host="localhost", port="5432")
    except: 
        return False

conn=get_connection()

if conn:
    print("connection is established")
else:
    print("Connection has NOT been established")    

curr =conn.cursor()
curr.execute("")
curr.execute("SELECT * FROM student;")
data= curr.fetchall()
for row in data:
    print(row)
conn.close()
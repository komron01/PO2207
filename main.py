import psycopg2 
conn = psycopg2.connect(
        user="postgres",
        password="123",
        host="78.141.227.124",
        database="GITHUB"
    )

cur = conn.cursor()
cur.execute("SELECT ROUND(AVG(age),1) FROM STUDENTS  WHERE stud_name LIKE 'A%'")
avg= cur.fetchone()
print('Average:',avg)
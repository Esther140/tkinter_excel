import mysql.connector
mydb = mysql.connector.connect(host="localhost",username="root",password="xter1171",database="jande")
mycursor =mydb.cursor()
mycursor.execute("select * from employee")
result = mycursor.fetchall()
for i in result:
    print(i)

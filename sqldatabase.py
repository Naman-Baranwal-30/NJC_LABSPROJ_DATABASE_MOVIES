#!C:\Users\Naman\AppData\Local\Programs\Python\Python39\python.exe
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="NJCLABS_MOVIES"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE NJCLABS_MOVIES")//for firsttime creating database
#mycursor.execute("CREATE Table MOVIES(Name varchar(200),actor varchar(100),actress varchar(100),director varchar(100),Year int(4))")//for firsttime creating table
as1="naman"
sql="insert into movies(Name,actor,actress,director,Year) values(%s,%s,%s,%s,%s)";
value=("Aspirants","Naveen","Shreya","Abhilash",2021);
#
mycursor.execute(sql,value);
sql1="insert into movies(Name,actor,actress,director,Year) values(%s,%s,%s,%s,%s)";
value1=("Panchayat","Jitendra","Pooja","Deepak",2020);
#
mycursor.execute(sql1,value1);
sql2="insert into movies(Name,actor,actress,director,Year) values(%s,%s,%s,%s,%s)";
value2=("Cubicles","Abhishek","Dhairya","Atharva",2020);
#
mycursor.execute(sql2,value2);
mydb.commit()
mycursor.execute("Select *from movies");
rows = mycursor.fetchall()

for row in rows:
   print(row)

mycursor.execute("SELECT * FROM movies WHERE actor ='Naveen'")

res = mycursor.fetchall()

for data in res:
  print(data)
mycursor.close();
mydb.close();
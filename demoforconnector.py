import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="arti",
  password="2828"
)

print(mydb)

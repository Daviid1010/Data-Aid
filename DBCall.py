import mysql.connector

con = mysql.connector.connect(host='den1.mysql4.gear.host',database='dataaid',user='dataaid',password='Gv365NTY-!W6');
print(con)

mycursor = con.cursor();

mycursor.execute("SELECT * FROM LineItems")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

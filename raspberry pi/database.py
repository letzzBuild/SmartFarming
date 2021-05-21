import mysql.connector as mysql

conn=mysql.connect(
    host="localhost",
    user="myuser",
    password="Password",
    database="SmartAgriculture"    
)

cursor=conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS SmartAgriculture")
cursor.execute("CREATE TABLE IF NOT EXISTS crops(id INTEGER PRIMARY KEY AUTO_INCREMENT,cropName VARCHAR(20) NOT NULL,water INT NOT NULL,light INT NOT NULL,temp DECIMAL NOT NULL)")

#insert values into table 
print("...... CROPS DATABASE VALUES .....")
noOfCrops=int(input("Enter how many crops you want to insert in database"))
for i in range(noOfCrops):
    plantName=input("enter the plant name ")
    waterVale=input("Enter the amount of water required for the plant") 
    tempValue=float(input("Enter the temperature required for the plant"))
    lightValue=int(input("Enter the light intensity required for the plant"))
    cursor.execute("INSERT INTO crops(cropName,water,light,temp) VALUES(%s,%s,%s,%s)",(plantName,waterVale,lightValue,tempValue))
    conn.commit()
    print("new crop added successfully....") 

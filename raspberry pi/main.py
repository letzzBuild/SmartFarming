import serial 
import RPi.GPIO as GPIO
import mysql.connector as mysql
from time import sleep



plantName = input("Enter the plant name in want to grow ")

try: 
   conn=mysql.connect(
    host="localhost",
    user="myuser",
    password="Password",
    database="SmartAgriculture"    
    )
except Exception as error:   
    print(error)
    exit(0)
    
    
curs = conn.cursor()

curs.execute("select * from crops where cropName=%s",(plantName,))

result = curs.fetchone()

if result is None:
    print("we are sorry to inform you that the plant is not added in our database, please add it first")
    exit(0)

requiredMoistureValue =  int(result[2])
requiredTemperatureValue = float(result[4])
requiredLdrValue = int(result[3])

currentMoistureValue = 0
currentTemperatureValue = 0.0
currentLdrValue = 0

moistureFlag = 0
temperatureFlag = 0
ldrFlag = 0


PORT = '/dev/ttyACM0'
BAURDRATE = 9600

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)



ser = serial.Serial(
port=PORT,
baudrate=BAURDRATE,
)

while True:
  try:   
    values=ser.readline().decode('utf-8')      [1024,43,555]
    listOfAllValues = values.split(';')
    currentMoistureValue = int(listOfAllValues[0])
    currentTemperatureValue = float(listOfAllValues[1])
    currentLdrValue = int(listOfAllValues[2])
    
    print(f"Sensor Moisture value : {currentMoistureValue} Required Moisture Value {requiredMoistureValue}")
    print(f"Sensor Temperature value : {currentTemperatureValue} Required Temperature Value {requiredTemperatureValue}")
    print(f"Sensor LDR value : {currentLdrValue} Required LDR Value {requiredLdrValue}")
    
    if (currentMoistureValue < requiredMoistureValue):
       print("motar on ")
       if moistureFlag == 0:
         GPIO.output(15,True)
         moistureFlag = 1
    else:
        print("motar off ")
        if moistureFlag == 1:
            moistureFlag = 0
            GPIO.output(15,False)
        
        
    if (currentTemperatureValue > requiredTemperatureValue ):
       print("fan on ")
       if temperatureFlag == 0:
         GPIO.output(11,True)
         temperatureFlag = 1
    else:
        print("fan off")
        if temperatureFlag == 1:
            temperatureFlag = 0
            GPIO.output(11,False)
            
        
        
    if (currentLdrValue < requiredLdrValue ):
       print("light off")
       if ldrFlag == 0:
         GPIO.output(13,True)
         ldrFlag = 1
    else:
        print("light off")
        if ldrFlag == 1:
          ldrFlag = 0
          GPIO.output(13,False)
        
    sleep(0.5)    
  except Exception as error:
      print(error)
      
GPIO.cleanup()      

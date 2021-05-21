#define moisture_sensor A1
#define ldr_sensor  A2
#define temperature_sensor A0


void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(moisture_sensor,INPUT);
pinMode(ldr_sensor,INPUT);
pinMode(temperature_sensor,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  
int moisture_value=analogRead(moisture_sensor);  
                      
int analogValue=analogRead(temperature_sensor);
float temp_val = (analogValue * 4.88);  //formula to convert analogvalue to celsius temp
float temperature_value = (temp_val/10);   //formula to convert analogvalue to celsius temp

int ldr_value=analogRead(ldr_sensor);
                          
Serial.print(moisture_value);
Serial.print(";");
Serial.print(temperature_value);
Serial.print(";");
Serial.print(ldr_value);
Serial.print(";");
Serial.println();

delay(1000);



}

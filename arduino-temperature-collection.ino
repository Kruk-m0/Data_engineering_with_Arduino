#define LM35 A0
#define Dallas A5
#include <OneWire.h>
#include <DallasTemperature.h>
OneWire oneWire(A5); 
DallasTemperature sensors(&oneWire);

void setup() 
{ 
Serial.begin(9600); sensors.begin(); 
} 

void loop() 
{
sensors.requestTemperatures(); 
float temp = ((analogRead(LM35) * 5.0) / 1024.0) * 100; 

Serial.print(sensors.getTempCByIndex(0)); 
Serial.print(", ");
Serial.println(temp);
delay(10000); 
}

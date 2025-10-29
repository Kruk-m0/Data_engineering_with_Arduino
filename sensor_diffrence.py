import serial
import datetime as dt
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

with open("thermometer-diffs.csv",'a') as csv:
    while True:
        response=ser.readline()
        a=dt.datetime.now()
        if response and len(response.decode('utf-8').strip())==12:
            csv.write(f"{a}, {response.decode('utf-8').strip()}\n")

ser.close()

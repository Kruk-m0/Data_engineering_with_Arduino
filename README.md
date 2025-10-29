All of this works in the following way:

1. I have an Arduino set up with LM35 connected to the A0 pin, and DS18B20 connected to A5 pin. The arduino code sends raw data through serial port 9600.
2. The temp_aggregate.py file formats the serial output and appends it to the csv file.
3. The temp_diffs.py file is a playgroud where i clean the data and display it with matplotlib.

Overall, all this was made to see if i can connect my knowledge from data enginnering and electronics.

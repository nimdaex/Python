import time
import serial
import binascii
import pyupm_i2clcd as upmLCD

serial_port = serial.Serial( port="/dev/ttyS0", baudrate=9600 )
LCD_096 = upmLCD.SSD1306(0, 0x3C);
#LCD_096.clear()
#LCD_096.display()

LCD_096.write ("Hello")
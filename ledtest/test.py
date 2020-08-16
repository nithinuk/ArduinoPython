import serial
import time

arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=9600)
time.sleep(2)
print("Connected to Arduino...")

print ("Enter '1' to turn 'on' the LED and '0' to turn LED 'off'")

while 1:

    var = input()
    print ("You Entered :"), var

    if var == '1':
        arduino.write(str.encode('1'))
        print("LED turned on")
        time.sleep(1)

    if var == '0':
        arduino.write(str.encode('0'))
        print("LED turned off")

    if var == 'q':
        break

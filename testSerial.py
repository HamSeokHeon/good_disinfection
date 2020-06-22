import serial

ser = serial.Serial('/dev/ttyACM1',9600)
while True:
    ReadText = ser.readline()[0]
    if ReadText == 102:
        print("aaaaaaaaaaaaaaaa")
    
    

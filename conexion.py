
import serial

ser = serial.Serial('COM3', 9600, timeout=2)


a = True
while a == True:
    var = input("Escribe a y b y h: ")
    if (var == "a"):
     
     ser.write(b'a')

    elif (var == "b"):
        ser.write(b'b')
    elif (var == 'h'):
       ser.write(b'h')
       
    r = input("Deseas terminar?")
    if (r == "si"):
       ser.close()
       break
    elif (r != "si"):
       a == True

print("El programa ha finalizado")
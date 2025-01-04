import torch
import cv2
import numpy as np
import pathlib
import serial
pathlib.PosixPath = pathlib.WindowsPath

#arduino = serial.Serial('COM4', 9600)

model = torch.hub.load('ultralytics/yolov5', 'custom', 
                       path = 'C:/Users/Erick Charly Yahir/Desktop/Proyecto_Charly_ IA/model/video/plasticos.pt')
                
modelo = torch.hub.load('ultralytics/yolov5', 'custom', 
                       path = 'C:/Users/Erick Charly Yahir/Desktop/Proyecto_Charly_ IA/model/video/papel.pt')

cap = cv2.VideoCapture(1)
fps = 20 
cap.set(cv2.CAP_PROP_FPS, fps)

#empezamos
while True:
    # Realizar lectura de la videocaptura

    ret, frame = cap.read()
    if not ret:
        break
    
    #realizamos las detecciones
    detect = model(frame)
    detect2 = modelo(frame)
   

    #mostramos fps
    cv2.imshow('detector de objetos', np.squeeze(detect.render()))
    cv2.imshow('detector de objetos', np.squeeze(detect2.render())) 
    
    #leemos el teclado
    
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

import torch
import cv2
import numpy as np
import pathlib

# Ajustes necesarios
pathlib.PosixPath = pathlib.WindowsPath

# Cargar modelos
model = torch.hub.load('ultralytics/yolov5', 'custom', 
                       path='F:/Daniel/model/video/plasticos.pt')
modelo = torch.hub.load('ultralytics/yolov5', 'custom', 
                        path='F:/Daniel/model/video/papel.pt')

# Configuración de la captura de video
cap = cv2.VideoCapture(1)
fps = 12
cap.set(cv2.CAP_PROP_FPS, fps)

# Empezamos
frame_count = 0
frame_skip = 1  # Procesar cada frame

while True:
    # Leer captura de video
    ret, frame = cap.read()
    if not ret:
        break

    # Procesar cada N-ésimo frame
    if frame_count % frame_skip == 0:
        # Realizar detecciones
        detect = model(frame)
        detect2 = modelo(frame)

        # Combinar resultados
        combined_frame = np.squeeze(detect.render())
        combined_frame = np.squeeze(detect2.render())

        # Mostrar el resultado combinado
        cv2.imshow('Detector de Objetos', combined_frame)

    frame_count += 1

    # Leer el teclado
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

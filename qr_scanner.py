from cv2 import cv2
from pyzbar.pyzbar import decode
import time

cap = cv2.VideoCapture(0)
received_data = []
time_start = time.time()

while True:
    _, frame = cap.read()
    time_now = time.time()
    
    if time_now > time_start+60:
        if received_data == []:
            break
        time_start = time_now
    
    decoded_data = decode(frame)
    try:
        data = decoded_data[0][0]
        if data not in received_data:
            received_data.append(data)
            print(data)
    except:
        pass

    cv2.imshow("Qr Scanner", frame)
    

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

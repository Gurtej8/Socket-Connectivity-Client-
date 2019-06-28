import cv2
import numpy as np
import socket
import pickle
import struct 
cap=cv2.VideoCapture(0)
w = cap.get(3)
h = cap.get(4)
ret = cap.set(3,w)
ret = cap.set(4,h)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('172.26.139.93',8089))
while True:
    ret,frame=cap.read()
    data = pickle.dumps(frame) 
    clientsocket.sendall(struct.pack("L", len(data))+data)

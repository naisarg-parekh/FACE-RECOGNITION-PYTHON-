import cv2
import numpy as np
import face_recognition

imgNVP = face_recognition.load_image_file("images/n.jpg")
imgNVP = cv2.cvtColor(imgNVP,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("images/n1.jpg")
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgNVP)[0]
encodeNVP = face_recognition.face_encodings(imgNVP)[0]
cv2.rectangle(imgNVP,(faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]),(0,255,0),2)
#print(faceLoc)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3], faceLocTest[0]),(faceLocTest[1], faceLocTest[2]),(0,255,0),2)

results = face_recognition.compare_faces([encodeNVP],encodeTest)
faceDis = face_recognition.face_distance([encodeNVP],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],4)}',(40,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv2.imshow('NAISARG PAREKH', imgNVP)
cv2.imshow('NAISARG Test', imgTest)
cv2.waitKey(0)
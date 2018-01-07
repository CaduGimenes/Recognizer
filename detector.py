import cv2
import sqlite3
import numpy as np


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("recognizer\\trainnerData.yml")
id=0
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
fontScale = 1.5
fontColor = (255,255,255)

def getProfile(id):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM Pessoas WHERE ID="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile


while (True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h)in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if(profile!=None):
            # Para adicionar mais campos basta copiar a linha a baixo e alterar o profile[1] para o numero da coluna desejada
            # To add more fields just copy the line down and change the profile[1] to the number of the desired column
            cv2.putText(img,str(profile[1]),(x,y+h+30),font,fontScale,fontColor,2);
    cv2.imshow("Detecao de Faces",img);      
    if(cv2.waitKey(1)==ord('q')): 
        break;                                   
cam.release()                              
cv2.destroyAllWindows()   

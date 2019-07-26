import cv2
import sqlite3
import numpy as np
from datetime import datetime

faceDetect=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml");
cam=cv2.VideoCapture(0);
conn=sqlite3.connect("Faces.db")

def insertOrUpdate(Tempo,Name):
    cmd="SELECT * FROM tb_faces WHERE cd_img="+str(Tempo)
    cursor=conn.execute(cmd)
    isRecordExist=0
    Name.lower()
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE tb_faces SET nm_client=' "+str(Name)+" ' WHERE nm_client="+str(Name)
    else:
        cmd="INSERT INTO tb_faces(cd_img,nm_client) Values("+str(Tempo)+",' "+str(Name)+" ' )"
    conn.execute(cmd)
    conn.commit()
    conn.close()

    
now = datetime.now()
tempo = now.year+now.month+now.day+now.hour+now.minute+now.second

nome=input('Informe seu nome: ')
insertOrUpdate(tempo,nome)
sampleNum=0;

while (True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h)in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataSet/User."+str(tempo)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100);
    cv2.waitKey(1);
    if(sampleNum>20):
        break
cam.release()                              
cv2.destroyAllWindows()




import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml");

path='dataSet'
def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faceSamples=[]
    Ids=[]
    
    for imagePath in imagePaths:
        if(os.path.split(imagePath)[-1].split(".")[-1]!='jpg'):
            continue
        
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces=detector.detectMultiScale(imageNp)

        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    
    return faceSamples,Ids


faces,Ids = getImagesAndLabels('dataSet')
recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainnerData.yml')

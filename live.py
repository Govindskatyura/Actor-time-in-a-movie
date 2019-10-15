import numpy as np
import cv2
import csv
import json
#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation




face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("sairabanu.mp4")
rec = cv2.face_LBPHFaceRecognizer.create();
rec.read("trainingdata.yml")
people=list()
id=0
jsFile=open("userId.json","r")
file=json.load(jsFile)
jsFile.close()
fpsCount={}

for framePerPerson in file.keys():
    fpsCount[framePerPerson] = 0 
font = cv2.FONT_HERSHEY_SIMPLEX

def liveVideo():
    t=1
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        for (x,y,w,h) in faces:
            #lower is better
            userid,conf=rec.predict(gray[y:y+h,x:x+w])
            fpsCount[str(userid)]=(fpsCount[str(userid)]+1)/25
            userid=file[str(userid)] 
            if(conf<60):
                t=t+1
                #cv2.imwrite("new/"+userid+str(t)+".jpg",img)
            if(conf>60):
                t=t+1
                #cv2.imwrite("unknown/"+userid+str(t)+".jpg",img)
            #print(id)
            #id=con("SELECT username FROM studentinfp WHERE id=%s" %id)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            if userid is None or conf>90:
                userid="Unknown"
            print(userid+" : " +str(conf))  
            cv2.putText(img,str(userid),(x,y+h),font,2.0,(0,0, 255))
            #if(id not in set(people)):
                #attandace(id)
            #people.append(id)
        cv2.imshow('img',img)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    print(fpsCount)
    ##display graph
    barGraph()



def barGraph():
    bar_width=0.3
    valueofdata=[]
    labels=[]
    for z in file.keys():
        labels.append(file[z])
        valueofdata.append(fpsCount[z])
    plt.bar(file.keys(), valueofdata,bar_width,color='b')
    index = np.arange(len(file.keys()))
    #label=file.keys()
    plt.xlabel('actor')
    plt.ylabel('Time in seconds')
    plt.xticks(index, labels, fontsize=8, rotation=30)
    plt.title('move time')

    plt.title('Time Graph with matplotlib')
    plt.show()

liveVideo()
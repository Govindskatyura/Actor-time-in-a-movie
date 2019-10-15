import os
import cv2
import cv2
import numpy as np
from PIL import Image
import json

recognizer =  cv2.face.LBPHFaceRecognizer_create();
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#dictionary for name and thiere id
idAndName={}
idofUser=1

for (_,subfolders,_) in os.walk('.'):
	faces = []
	IDs = []
	for folder in subfolders:
		if(folder !='User' and folder !='new'and folder !='unknown'):
			fileNames = [fileName for fileName in os.listdir(folder) if fileName.endswith(".jpg" or ".jpeg")]
			idAndName[idofUser]=folder
			sampleN=0
			for file in fileNames:
				#add path with file name
				z='./'+folder+'/'+file
				#print(z)

				img=cv2.imread(z)
				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

				faces = face_cascade.detectMultiScale(gray, 1.3, 5)
				for (x,y,w,h) in faces:
					sampleN=sampleN+1;
					saveFace="User/"+folder+"."+str(idofUser)+ "." +str(sampleN)+ ".jpg"
					print(saveFace)
					#save croped image
					cv2.imwrite(saveFace, gray[y:y+h, x:x+w])
					cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
					#cv2.imshow("tmp",img)
					cv2.waitKey(100)
			idofUser +=1
		cv2.waitKey(1)
		cv2.destroyAllWindows()
		# for other 
		idAndName["Unknown"]="Other or Not predict"
	jsFile=open("userId.json","w+")
	json.dump(idAndName,jsFile)
	jsFile.close()
	#close os.walk() 
	break
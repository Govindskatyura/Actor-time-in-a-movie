# Actor-time-in-a-movie
 facial recognition tool of each and every character of the movie and calculate the total screen time of the characters.
##
# Installation 
!pip install -r requirements.txt

##
in this project i used OpenCv for vision and Matplotlib for ploting
model trained with images and labeled with the folder name.
to train a new model you have to create a folder with name of person and inside of the folder images of that person

## How to run this project 
 First you have to download a video (hera pheri 1976) or images of any cast of this movie.(this project is trained for only hera pheri cast)
 and replace the video name inside of live.py file
 run live.py and 
 #Quit key is 'q'
 after quit you will get a barChart of all actors and there total time in the movie till you quit.
 
 ##Train for other movie
 for that you have to remove all folders (not 'new','unkown',and 'User')
 create new folder with names and images inside of theme
 run faceCrop.py
 run train.py
 and your model will saved in trainingdata.yml file
 then run live.py for test.
 

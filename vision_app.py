import pytesseract
import cv2
from gtts import gTTS
import os,stat
import sys
import time

# Playing the Vision App's introduction Audio
os.system("mpg321 -q /home/pi/TestingResults/intro.wav")

while True:
    try:
       
        input("Press Enter to continue...")
        
        #Setting variables to store pictures and audio files
        testingfolder = '/home/pi/Testing/'
        testingresultsfolder = '/home/pi/TestingResults/'
        #Making filename value
        filename = time.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        # uses Fswebcam to take picture
        os.system('fswebcam -r 1024x720 -S 3 --jpeg 100 --save ' + testingfolder + filename) 
        #Reading the image in OpenCV
        img = cv2.imread(testingfolder + filename)
        
        custom_config = r'-l eng --psm 6'
        #Detects text from image
        texts = pytesseract.image_to_string(img, config=custom_config)
        print(texts)
        cv2.destroyAllWindows()
        
        # gTTS converts text to audio
        audio = gTTS(text = texts, lang = 'en', slow = True)
        # Saves the audio in a folder
        audio.save(testingresultsfolder + filename+".mp3")
        os.system("chmod 777 " + testingresultsfolder + filename+".mp3")
        # Says out loud the audio file
        os.system("mpg321 -q " + testingresultsfolder + filename +".mp3")
        # Says out loud the instructions to repeat again
        os.system("mpg321 -q /home/pi/TestingResults/again.wav")
    except AssertionError:
        print(" There was no text found. Try to take a picture again or contact Pranav.ar.2010@gmail.com ")
        os.system("mpg321 -q /home/pi/TestingResults/mistake.wav")
    except TypeError:
        print(" Camera not found. Check if your camera is pluged in and functioning properly.")
        os.system("mpg321 -q /home/pi/TestingResults/camera.wav")
        break
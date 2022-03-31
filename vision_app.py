
import cv2
import os,stat
import sys
import time
import pytesseract
import cv2
from gtts import gTTS
from textblob import TextBlob
from spellchecker import SpellChecker
import getch
import pty
import termios
import sys
 

# Playing the Vision App's introduction Audio
os.system("mpg321 -q /home/pi/TestingResults/introduction2.wav")

spell = SpellChecker()

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
        

        #cv2.imshow('normal', img)
        #cv2.waitKey(0)
        custom_config = r'-l eng --psm 6'
        texts = pytesseract.image_to_string(img, config=custom_config)
        print(texts)

        words = texts.split()
        original_total = 1 
        correctedwords = []

        for i in range(len(words)):         
            correctedword = str(TextBlob(words[i]).correct())
            correctedwords.append(correctedword)
            original_total = len(correctedwords)      

        original_sentence = " ".join(correctedwords)
        
        #Converts original image into a gray scale image
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #Converts gray scale image into a black and white image
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 70, 255, cv2.THRESH_BINARY)
        
        #cv2.imshow('black_and_white', blackAndWhiteImage)
        #cv2.waitKey(0)

        # Detects texts from image
        custom_config = r'-l eng --psm 6'
        texts = pytesseract.image_to_string(blackAndWhiteImage, config=custom_config)
        print(texts)
        
        #splits sentence into words
        words = texts.split()
        
        #initializes variables
        bw_total = 1 
        correctedwords = []

        for i in range(len(words)):
            # loop through words to get corrected words
            correctedword = str(TextBlob(words[i]).correct())
            correctedwords.append(correctedword)
        
        #get number of words
        bw_total = len(correctedwords)
        #join the words into sentence
        bw_sentence = " ".join(correctedwords)   

        #check if black and white words are more than original total 
        if bw_total > original_total:
            print (bw_total)
            print ("black and white")
            print (bw_sentence)
            # gTTS converts text to audio
            audio = gTTS(text = bw_sentence, lang = 'en', slow = False)
            # Saves the audio in a folder
            audio.save(testingresultsfolder + filename+".mp3")
        else:
            print (original_total)
            print ("original")
            print (original_sentence)
            # gTTS converts text to audio
            audio = gTTS(text = original_sentence, lang = 'en', slow = False)
            # Saves the audio in a folder
            audio.save(testingresultsfolder + filename+".mp3")
            
        os.system("chmod 777 " + testingresultsfolder + filename+".mp3")
        # Says out loud the audio file
        os.system("mpg321 -q " + testingresultsfolder + filename +".mp3")  

        #print("------------------------")
        #print(" If you want to hear the second audio version, press the space bar")
        os.system("mpg321 -q /home/pi/TestingResults/other_image.wav")       
        
        #get input from usser to hear the second option
        ch = sys.stdin.read(1)
        #if user input is space then read the second version
        if ch == ' ':
            if bw_total > original_total:
                print (original_total)
                print ("original")
                print (original_sentence)
                audio = gTTS(text = original_sentence, lang = 'en', slow = False)
                 # Saves the audio in a folder
                audio.save(testingresultsfolder + filename+".mp3")
            else:
                print (bw_total)
                print ("black and white")
                print (bw_sentence)
                audio = gTTS(text = bw_sentence, lang = 'en', slow = False)
             # Saves the audio in a folder
                audio.save(testingresultsfolder + filename+".mp3")
            os.system("chmod 777 " + testingresultsfolder + filename+".mp3")
            # Says out loud the audio file
            os.system("mpg321 -q " + testingresultsfolder + filename +".mp3")
            
        sys.stdin.flush()        
             
        cv2.destroyAllWindows()
   
        # Says out loud the instructions to repeat again
        os.system("mpg321 -q /home/pi/TestingResults/again.wav")
    except AssertionError:
        print(" There was no text found. Try to take a picture again or contact Pranav.ar.2010@gmail.com ")
        os.system("mpg321 -q /home/pi/TestingResults/mistake.wav")
    except TypeError:
        print(" Camera not found. Check if your camera is pluged in and functioning properly.")
        os.system("mpg321 -q /home/pi/TestingResults/camera.wav")
        break

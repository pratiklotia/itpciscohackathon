#Python script that records user input and converts it to text.
#Makes use of "speech_recognition" and "pyaudio" modules.
#This script should be installed on a computer.
#The computer sends the text input to the Intel Edison via scp.

import pyttsx3
import speech_recognition as sr
import os
from gtts import gTTS
r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
		print ('Say Something!')
		try:
			audio = r.listen(source)
			print ('Done!')
			text = r.recognize_google(audio)
			print ("You Said: " + text)
			try:
				f=open("command.txt","w")
				f.write(text)
				f.close()
				tts=gTTS(text="Hello! You have sent the message"+str(text), lang="en")
				tts.save("good.mp3")
				os.system("mpg123 good.mp3")     
			except:
				print("Can't create file")
			os.system("scp command.txt root@127.0.0.1:/root/rec_command.txt") 
		except:
			print("Didn't say anything")
	print("Yo\n\n")


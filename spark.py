from ciscosparkapi import CiscoSparkAPI
import configparser
import time
import pyttsx3
import speech_recognition as sr
import os
from gtts import gTTS
config = configparser.ConfigParser()
config.read("spark.cfg")
apiKey = config.get('apiKey', 'key')
#print(apiKey)
api = CiscoSparkAPI(access_token=apiKey)
roomName="Trishul"
r = sr.Recognizer()

def getRoomID(api, roomName):
    rawRooms=api.rooms.list()
    rooms=[room for room in rawRooms if room.title == roomName]
    if len(rooms)==0:
        api.rooms.create(roomName)
    for room in rooms:
        roomID=(room.id)
        return roomID

roomID=getRoomID(api, roomName)
#print(roomID)
#Send message on start
reply = "Cisco ITP Hackathon"
api.messages.create(roomID, text=reply)
last_id = 0
while True:
    messages = api.messages.list(roomID, max=1)
    for message in messages:
        if message.id != last_id:
            print("Found New message")
            if message.text == "Spark":
                with sr.Microphone() as source:
                    print ('Say Something!')
                    audio = r.listen(source)
                    print ('Done!')
                text = r.recognize_google(audio)
                reply = text
                api.messages.create(roomID, text=reply)
        last_id = message.id
        time.sleep(10)
        break

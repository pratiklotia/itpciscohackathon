import pyttsx3
engine = pyttsx3.init()
#engine.say('Hello World')
#engine.runAndWait()

#engine = pyttsx.init()
'''
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''

while True:
	engine.say('Sally sells seashells by the seashore.')
	engine.say('The quick brown fox jumped over the lazy dog.')
	engine.runAndWait()
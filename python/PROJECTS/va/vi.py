
'''
Virtual Assistance --> make conversion,location
#TTs -->gTTs(Google TEXT TO SPEECH)

import gtts
from gtts import gTTS
import playsound # now we will give a text and convert to audio

#now we will give a text and convert to audio
text = "namasthe boss"
g = gTTS(text)
#save as audio file (.mp3)
g.save("audio.mp3")
playsound.playsound('audio.mp3')
'''
#let us make our VirtualAssistance to understand what we speak
import gtts
from gtts import gTTS
import playsound 
import speech_recognition as sr
from time import ctime #it returns current time
import os
import uuid
import webbrowser
#first we will make our Vartual Assistance to understand what we speak

def listen():
    #SpeechRecognition
    #we will make our system to chek the Microphone as source
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Now we can start talking")
        audio = r.listen(source,phrase_time_limit = 5)
    #what ever we speak lets store in data
    data =""
    #now we will give our Exception handling here to avoid any errors
    try:
        data = r.recognize_google(audio,language="en-US")
        print("You said data:",data)
    except sr.UnknownValueError:
        print("Make sure to speak louder,so it can be heard")
    except sr.RequestError as e:
        print("Request failed,please check your internet connection")
    return data
#listen() #needs have pyaudio --> pip install pyaudio
    #text = gTTS(data)
    #text.save('new.mp3')
    #playsound.playsound('new.mp3')
#listen()

#we will create separate functions for responding back and virtual assistance actions

def respond(String):
    #Responding function to get audio saved and text is spoken back
    print(String)
    tts = gTTS(text=String)
    #now we want only text to be modified in the audio file
    tts.save("Speech.mp3")
    #we will use above audio file and modify the content in it
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
#next we will make our virtualassistance to work with given conditions
    

def va(data):
    #Now we will map our conditions
    if "hello" in data:
        listening = True
        respond("hey hi good to see you")
    elif "how are you"in data:
        listening =True
        respond("I am good hope you are well")
    elif "what are your plans" in data:
        listening = True
        respond("em ledhi ra bhaii chdhuvukoo")
    elif "time" in data:
        listenng = True
        respond(ctime())
    elif "open Google" in data:
        listening = True
        url = "https://www.google.com"
        webbrowser.open(url)
        print("Success")
        respond("Done opened")
    elif "locate" in data:
        listening = True
        url = "https://www.google.com/search"
        webbrowser.open(url+data.replace("locate",""))
        print("Located")
        respond("Done maps Opened")
    elif "play" in data:
        listening = True
        url = "https://www.youtube.com/"
        webbrowser.open(url+data.replace("play",""))
        print("play")
        respond("Done")
    elif "stop talking" in data:
        listening = False
        respond("ok cool")
    try:
        return listening
    except UnboundLocalError:
        print("Mismatched speak correctly")
respond("hey ramana")
listening = True
while listening:
    data = listen()
    listening = va(data)


 


















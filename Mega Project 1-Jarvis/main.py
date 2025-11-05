# ctrn+shift+p and search Python: select intrpreter and select virtual environment and version global
# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
# pip install pocketsphinx
# pip install requests
# pip install openai
# pip install gTTS
# pip install pygame

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer=sr.Recognizer() # Recognizer is a class which helps to get from speech recognizer functionality
engine = pyttsx3.init() # it will initialize
newsApi="<Your api Key Here>" #get from newsapi account



def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
      tts = gTTS('hello')
      tts.save('temp.mp3') 

      # Initialize Pygame mixer
      pygame.mixer.init()

      # Load the MP3 file
      pygame.mixer.music.load('temp.mp3')

      # Play the MP3 file
      pygame.mixer.music.play()

      # Keep the program running until the music stops playing
      while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
      
      pygame.mixer.music.unload()
      os.remove("temp.mp3") 

if __name__ == "__main__":
   
   speak("Initializing Jarvis......")

   while True:
            # taking code from speech recognition documentation example github microphone recognition file

            # Listen for the wake word jarvis
            # obtain audio from the microphone
            r = sr.Recognizer()
            # with sr.Microphone() as source:
            #     print("Listening.....")
            #     audio = r.listen(source)

            def aiProcess(command):
                  client = OpenAI(api_key="<Your Key Here>",
                  )

                  completion = client.chat.completions.create(
                  model="gpt-3.5-turbo",
                  messages=[
                        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
                        {"role": "user", "content": command}
                  ]
                  )

                  return completion.choices[0].message.content


            def processCommand(c):
                  if "open google" in c.lower():
                        webbrowser.open("https://www.google.com")
                  elif "open facebook" in c.lower():
                        webbrowser.open("https://www.facebook.com")
                  elif "open youtube" in c.lower():
                        webbrowser.open("https://www.youtube.com")
                                    
                  elif c.lower().startswith("play"):
                        song= c.lower().split(" ")[1]
                        link= musicLibrary.music[song]
                        webbrowser.open(link)

                  elif "news" in c.lower():
                        r=requests.get("https://newsapi.org/v2/top-headlines?country=bd&apiKey={newsApi}")
                        if r.status_code==200:
                                    # parse the json response
                                    data= r.json()
                                    # extract the articles
                                    articles= data.get("articles", [])

                                    # print the headlines
                                    for article in articles:
                                          speak(article["title"])

                  else:
                        # Let OpenAI handle the request 
                        output = aiProcess(c)
                        speak(output) 


                                          


                         
                      
            
            print("Recognizing...")
            # recognize speech using Sphinx or google.google give more clear ans
            try:
                with sr.Microphone() as source:
                        print("Listening.....")
                        audio = r.listen(source,timeout=2,phrase_time_limit=1)  
                # print("Sphinx thinks you said " + r.recognize_sphinx(audio))
                # command= r.recognize_sphinx(audio)
                word= r.recognize_google(audio)
                if(word.lower()=="jarvis"):
                      speak("Ya")


                      # Listen for command

                      with sr.Microphone() as source:
                                    print("Jarvis Acitivated.....")
                                    audio = r.listen(source)
                                    command= r.recognize_google(audio)
                                    processCommand(command)

            # except sr.UnknownValueError:
            #     print("Sphinx could not understand audio")
            # except sr.RequestError as e:
            #     print("Sphinx error; {0}".format(e))
            except Exception as e:
                  
                  print("Error; {0}".format(e))
                 
            

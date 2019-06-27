#!/usr/bin/env python
# coding: utf-8

#                             I HAVE PREPARED A SPEECH RECOGNITION /AI BASED CHATBOT
#                     By which we can give command and as per the command it will give us the output.
#                     

# In[1]:


import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser


# In[2]:


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


# In[3]:


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# In[4]:


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("hi i am your assistant. Please tell me how may I help you")       


# In[5]:


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=10)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query


# In[6]:


if __name__ == "__main__":
    wishMe()
    while True:
        
    #if 1:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            webbrowser.open("music.youtube.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
            
        elif 'what can you do for me' in query:
            speak('i will give you the answer of your questions')
                
        elif'your name' in query:
            speak("i am robo")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
                
        elif 'thank you' in query:
            speak('you welcome')
            print('you welcome and good bye')
            break
            
                
                
        elif 'bye' in query:
            break
        


# In[ ]:





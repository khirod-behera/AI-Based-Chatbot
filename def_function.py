            #Here i have imported two python libraries by which we can detect the audio and recognise the audio
 




# 1st one is the pyttsx3 it will convert text into speech.
#2nd one is the speech_recognition it will recognise the voice.

import pyttsx3 
import speech_recognition as sr

engine = pyttsx3.init('sapi5') #sapi5 is the speech api by which we can convert into voice

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id) # Here i have given voices id is  1 because of male voice if i will give 0 then i can convert into female



def speak(audio):       #Here i have define a function to speak audio
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    #This is the defination which will take voice command.
    #It takes microphone input from the user and returns string output
    
    #it will listen the voice and then recognize it 
    #and if this will could not recognize then it will print say that again please.

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
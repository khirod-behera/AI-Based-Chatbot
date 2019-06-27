


#Here i have taken wikipedia and webbrowser these are also the python libraries.
#from this i have created conditions and given some logics as per the customer requirement..


import wikipedia 
import webbrowser


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
            
        elif'hi' in query:
            speak("hello what is your name")
            
                
        elif 'thank you' in query:
            speak('you welcome')
            print('you welcome and good bye')
            break
            
                
                
        elif 'bye' in query:
            break

import datetime

#By importing Date and time it will wish us as per the time.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")   #if this is before 12 then condition is here to say good morning
        


    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   #if this is between 12 to 6 pm then it will say us Good afternoon as per the time.

    else:
        speak("Good Evening!")   #else it will say Good evening.
        
        
    speak("hi i am your assistant. Please tell me how may I help you")
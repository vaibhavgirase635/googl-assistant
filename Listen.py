import speech_recognition as sr
from Speak import talk, greet_user



def take_command():
    r = sr.Recognizer()  # Create a new listener instance
    with sr.Microphone() as source:
        
        print("Listening.....")
        greet_user()
        r.pause_threshold = 1
        audio = r.listen(source,0,2)
    try:        
        print("Recognizing..")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said : {query}")
    except:
        return ""
    
    query = str(query)
    return query.lower()

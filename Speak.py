import pyttsx3
from datetime import datetime
def talk(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in talk function: {e}")
    finally:
        engine.stop()

def greet_user():
   hour = datetime.now().hour
   if (hour >= 6) and (hour < 12):
      talk("Good Morning sir, how can I help you?")
   elif (hour >= 12) and (hour < 16):
      talk("Good Afternoon sir, how can I help you?")
   else:
      talk("Good Evening sir, how can I help you?")   

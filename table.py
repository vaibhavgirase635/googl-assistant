import pyttsx3
import speech_recognition as sr
from datetime import datetime
from transformers import pipeline
import pandas as pd
def talk(text):
    engine = pyttsx3.init()
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

def take_command():
    listener = sr.Recognizer()  # Create a new listener instance
    with sr.Microphone() as source:
        try:
            print("Listening.....")
            greet_user()
            voice = listener.listen(source)
            print('voice')
            audio = listener.recognize_google(voice)
            print(audio)
            return audio
        except sr.RequestError:
            print("No Default Input Device Available")
            return None
        except sr.UnknownValueError:
            print("Say that again")
            talk("Please tell me again")
            return None
        

def Table(question):
# prepare table + question
    data = {"Actors": ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"], "Number of movies": ["87", "53", "69"]}
    table = pd.DataFrame.from_dict(data)
    

    # pipeline model
    # Note: you must to install torch-scatter first.
    tqa = pipeline(task="table-question-answering", model="google/tapas-large-finetuned-wtq")

    # result

    print(tqa(table=table, query=question)['cells'][0])

Table("how many movies does Leonardo Di Caprio have?")

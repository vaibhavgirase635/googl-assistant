import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
            with sr.Microphone() as source:
                print("Listening.....")
                talk('Please tell me how can I help you')
                
                #print(voice)
                listener.pause_threshold = 1
                voice = listener.listen(source)
            try:
                audio = listener.recognize_google(voice)
                #print(command)
                command = audio
            except:
                print('Say that again')
                talk("Please tell me again")
                return None
            #print(command)
            
            return command
                

if __name__ == '__main__':
      while True:
            que = take_command()
            try:
                  
                ans = wikipedia.summary(que, 2)
                print(ans)
                talk(ans)
            except:
                talk("Soory not found")
            try:
                if 'bye' in que:
                  break
            except:
                take_command()
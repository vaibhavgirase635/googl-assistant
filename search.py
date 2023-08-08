import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import openai
from apikey import api_data


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
openai.api_key = api_data
completion = openai.Completion()


def Answer(question):
     prompt = f'Chando: {question}\n Jarvis: '
     response = completion.create(prompt=prompt, engine="text-davinci-002-render-sha", stop=['\Chando'], max_tokens=200)
     answer = response.choices[0].text.strip()
     return answer
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
            except Exception as e:
                print('Say that again')
                talk("Please tell me again")
                return None
            #print(command)
            
            return command
                

if __name__ == '__main__':
      while True:
            query = take_command().lower()
            ans = Answer(query)
            print(ans)
            talk(ans)
            if 'bye' in query:
                  break
import playsound # allows the playing of sound files
import time #download current time for sleep function
import pygame #Library for running graphical interface
import threading
import time
import wikipedia
from transformers import logging, pipeline
from Deepset import model, tokenizer
import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
from datetime import datetime
import webbrowser
import requests

def greet_user():
   hour = datetime.now().hour
   if (hour >= 6) and (hour < 12):
      talk("Good Morning sir, how can I help you?")
   elif (hour >= 12) and (hour < 16):
      talk("Good Afternoon sir, how can I help you?")
   else:
      talk("Good Evening sir, how can I help you?")

def talk(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate')
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in talk function: {e}")
    finally:
        engine.stop()
    
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
    

class imageHandler:
  def __init__ ( self ):
    self.pics = dict()

  def loadFromFile ( self, filename, id=None ):
    if id == None: id = filename
    self.pics[id] = pygame.image.load ( filename ).convert()

  def loadFromSurface( self, surface, id ):
    self.pics[id] = surface.convert_alpha()

  def render( self, surface, id, position = None, clear = False, size = None ):
    if clear == True:
      surface.fill ( (5,2,23) ) #

    if position == None:
      picX = int ( surface.get_width() / 2 - self.pics [ id ].get_width() / 2 )
    else:
      picX = position [0]
      picY = position [1]

    if size == None:
      surface.blit( self.pics[id], ( picX, picY ) ) #

    else:
      surface.blit( pygame.transform.smoothscale(self.pics[id], size ), ( picX, picY ) )
      
#Initialises the display-------------------------------------------------------
pygame.display.init() # Initiates the display pygame
pygame.display.set_caption("J.A.R.V.I.S")
screen = pygame.display.set_mode((1000,600), pygame.RESIZABLE) #uncomment this line for smaller window
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #allows fullscreen #comment this line out for smaller window
handler = imageHandler()

def display():
    handler.loadFromFile(r'C:\jarvis\frame_00_delay-0.03s.jpg','1')
    handler.loadFromFile(r'C:\jarvis\frame_01_delay-0.03s.jpg','2')
    handler.loadFromFile(r'C:\jarvis\frame_02_delay-0.03s.jpg','3')
    handler.loadFromFile(r'C:\jarvis\frame_03_delay-0.03s.jpg','4')
    handler.loadFromFile(r'C:\jarvis\frame_04_delay-0.03s.jpg','5')
    handler.loadFromFile(r'C:\jarvis\frame_05_delay-0.03s.jpg','6')
    handler.loadFromFile(r'C:\jarvis\frame_06_delay-0.03s.jpg','7')
    handler.loadFromFile(r'C:\jarvis\frame_07_delay-0.03s.jpg','8')
    handler.loadFromFile(r'C:\jarvis\frame_08_delay-0.03s.jpg','9')
    handler.loadFromFile(r'C:\jarvis\frame_09_delay-0.03s.jpg','10')
    handler.loadFromFile(r'C:\jarvis\frame_10_delay-0.03s.jpg','11')
    handler.loadFromFile(r'C:\jarvis\frame_11_delay-0.03s.jpg','12')
    handler.loadFromFile(r'C:\jarvis\frame_12_delay-0.03s.jpg','13')
    handler.loadFromFile(r'C:\jarvis\frame_13_delay-0.03s.jpg','14')
    handler.loadFromFile(r'C:\jarvis\frame_14_delay-0.03s.jpg','15')
    handler.loadFromFile(r'C:\jarvis\frame_15_delay-0.03s.jpg','16')
    handler.loadFromFile(r'C:\jarvis\frame_16_delay-0.03s.jpg','17')
    handler.loadFromFile(r'C:\jarvis\frame_17_delay-0.03s.jpg','18')
    handler.loadFromFile(r'C:\jarvis\frame_18_delay-0.03s.jpg','19')
    handler.loadFromFile(r'C:\jarvis\frame_19_delay-0.03s.jpg','20')
    handler.loadFromFile(r'C:\jarvis\frame_20_delay-0.03s.jpg','21')
    handler.loadFromFile(r'C:\jarvis\frame_21_delay-0.03s.jpg','22')
    handler.loadFromFile(r'C:\jarvis\frame_22_delay-0.03s.jpg','23')
    handler.loadFromFile(r'C:\jarvis\frame_23_delay-0.03s.jpg','24')
    handler.loadFromFile(r'C:\jarvis\frame_24_delay-0.03s.jpg','25')
    handler.loadFromFile(r'C:\jarvis\frame_25_delay-0.03s.jpg','26')
    handler.loadFromFile(r'C:\jarvis\frame_26_delay-0.03s.jpg','27')
    handler.loadFromFile(r'C:\jarvis\frame_27_delay-0.03s.jpg','28')
    handler.loadFromFile(r'C:\jarvis\frame_28_delay-0.03s.jpg','29')
    handler.loadFromFile(r'C:\jarvis\frame_29_delay-0.03s.jpg','30')
    handler.loadFromFile(r'C:\jarvis\frame_30_delay-0.03s.jpg','31')
    handler.loadFromFile(r'C:\jarvis\frame_31_delay-0.03s.jpg','32')
    handler.loadFromFile(r'C:\jarvis\frame_32_delay-0.03s.jpg','33')
    handler.loadFromFile(r'C:\jarvis\frame_33_delay-0.03s.jpg','34')
    handler.loadFromFile(r'C:\jarvis\frame_34_delay-0.03s.jpg','35')
    handler.loadFromFile(r'C:\jarvis\frame_35_delay-0.03s.jpg','36')
    handler.loadFromFile(r'C:\jarvis\frame_36_delay-0.03s.jpg','37')
    handler.loadFromFile(r'C:\jarvis\frame_37_delay-0.03s.jpg','38')
    handler.loadFromFile(r'C:\jarvis\frame_38_delay-0.03s.jpg','39')
    handler.loadFromFile(r'C:\jarvis\frame_39_delay-0.03s.jpg','40')
    handler.loadFromFile(r'C:\jarvis\frame_40_delay-0.03s.jpg','41')
    handler.loadFromFile(r'C:\jarvis\frame_41_delay-0.03s.jpg','42')
    handler.loadFromFile(r'C:\jarvis\frame_42_delay-0.03s.jpg','43')
    handler.loadFromFile(r'C:\jarvis\frame_43_delay-0.03s.jpg','44')
    handler.loadFromFile(r'C:\jarvis\frame_44_delay-0.03s.jpg','45')
    handler.loadFromFile(r'C:\jarvis\frame_45_delay-0.03s.jpg','46')
    handler.loadFromFile(r'C:\jarvis\frame_46_delay-0.03s.jpg','47')
    handler.loadFromFile(r'C:\jarvis\frame_47_delay-0.03s.jpg','48')
    handler.loadFromFile(r'C:\jarvis\frame_48_delay-0.03s.jpg','49')
    handler.loadFromFile(r'C:\jarvis\frame_49_delay-0.03s.jpg','50')
    handler.loadFromFile(r'C:\jarvis\frame_50_delay-0.03s.jpg','51')
    handler.loadFromFile(r'C:\jarvis\frame_51_delay-0.03s.jpg','52')
    handler.loadFromFile(r'C:\jarvis\frame_52_delay-0.03s.jpg','53')
    handler.loadFromFile(r'C:\jarvis\frame_53_delay-0.03s.jpg','54')
    handler.loadFromFile(r'C:\jarvis\frame_54_delay-0.03s.jpg','55')
    handler.loadFromFile(r'C:\jarvis\frame_55_delay-0.03s.jpg','56')
    handler.loadFromFile(r'C:\jarvis\frame_56_delay-0.03s.jpg','57')
    handler.loadFromFile(r'C:\jarvis\frame_57_delay-0.03s.jpg','58')
    handler.loadFromFile(r'C:\jarvis\frame_58_delay-0.03s.jpg','59')
    handler.loadFromFile(r'C:\jarvis\frame_59_delay-0.03s.jpg','60')
    handler.loadFromFile(r'C:\jarvis\frame_60_delay-0.03s.jpg','61')
    handler.loadFromFile(r'C:\jarvis\frame_61_delay-0.03s.jpg','62')
    handler.loadFromFile(r'C:\jarvis\frame_62_delay-0.03s.jpg','63')
    handler.loadFromFile(r'C:\jarvis\frame_63_delay-0.03s.jpg','64')



def face():
    A = 240
    B = -5
    x = 550
    y = 550
    running = True
    while running:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
      for i in range(1,65):
        handler.render ( screen, f"{i}", ( A, B ), True, ( x, y ) )
        pygame.display.update(A,B,x,y) 
        # or replace with this line for easier coding 
        #pygame.display.update(A,B,x,y) 
        time.sleep(.2)

def get_random_joke():
   headers = {'Accept': 'application/json'}
   res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
   return res["joke"]
      
def main():
    while True:
      question = take_command()
      print(question)
      if question is None:
          talk("No input question received")
      
      elif "hello" in question.lower():
          talk("Hello sir, how can I help you")

      elif "how are you" in question.lower():
          talk("I am fine sir")
      elif "time now" in question:
          ctime = datetime.now()
          print(ctime)
          talk("The time is" + ctime)
      
      elif "joke" in question:
          talk("Hope you like this one sir")
          joke = get_random_joke()
          talk(joke)
          print(joke)

      elif "who is" or "what is" in question.lower():
          context = wikipedia.summary(question, 3)
          print(context)
          qna_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)
          result = qna_pipeline({'question':question, 'context':context})
          print(result)
          answer = result['answer']
          talk(answer)
          
        
def Main():
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=face)

    display()
    t1.start()
    t2.start()

Main()

# def search_on_google(query):
#    kit.search(query)
# search_on_google('what is python')
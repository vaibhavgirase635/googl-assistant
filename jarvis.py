import random
import torch
import json
from brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
from Listen import take_command
from Speak import talk
from Task import NonInputExecution,InputExecution,ArithmaticOperation
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisGUI import Ui_MainWindow
import speech_recognition as sr
import sys
import pyttsx3
from datetime import datetime


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json","r") as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

Name = "Jarvis"
breakup = ["bye","goodbye","see you later","sleep","exit"]

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Main()
    
    def talk(self,text):
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

    def greet_user(self):
        hour = datetime.now().hour
        if (hour >= 6) and (hour < 12):
            talk("Good Morning sir, how can I help you?")
        elif (hour >= 12) and (hour < 16):
            talk("Good Afternoon sir, how can I help you?")
        else:
            talk("Good Evening sir, how can I help you?")   

    def take_command(self):
        r = sr.Recognizer()  # Create a new listener instance
        with sr.Microphone() as source:
            
            print("Listening.....")
            self.greet_user()
            r.pause_threshold = 1
            audio = r.listen(source,0,4)
        try:        
            print("Recognizing..")
            query = r.recognize_google(audio,language="en-in")
            print(f"You Said : {query}")
        except:
            return ""
        
        query = str(query)
        return query.lower()

    def Main(self):
        self.sentence = self.take_command()
        # print(sentence)
        if self.sentence in breakup:
            talk("Bye sir")
            exit()
        
        elif self.sentence != "":
            self.sentence = tokenize(self.sentence)
            # print(sentence)
            x = bag_of_words(self.sentence, all_words)
            # print(x)
            x = x.reshape(1,x.shape[0])
            # print(x)
            x = torch.from_numpy(x).to(device)
            # print(x)
            output = model(x)

            _ , predicted = torch.max(output,dim=1)

            tag = tags[predicted.item()]
            # print(tag)
            probs = torch.softmax(output,dim=1)
            prob = probs[0][predicted.item()]
            # print(prob.item())
            if prob.item() > 0.55:
                for intent in intents['intents']:
                    if tag == intent["tag"]:
                        reply = random.choice(intent["responses"])
                        # print(reply)
                        if "time" in reply:
                            NonInputExecution(reply)

                        elif "date" in reply:
                            NonInputExecution(reply)

                        elif "day" in reply:
                            NonInputExecution(reply)
                        
                        elif "wikipedia" in reply:
                            InputExecution(reply, self.sentence)

                        elif "addition" in reply:
                            ArithmaticOperation(reply)
                        
                        elif "multiplication" in reply:
                            ArithmaticOperation(reply)
                        
                        elif "division" in reply:
                            ArithmaticOperation(reply)

                        elif "substraction" in reply:
                            ArithmaticOperation(reply)
                        else:
                            talk(reply) 
        else:
            talk("I cant't understand your question please tell me again")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/shree/Downloads/jarvisgif.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        # self.ui.movie = QtGui.QMovie("../../Downloads/system.gif")
        # self.ui.label_2.setMovie(self.ui.movie)
        # self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString('yyyy-MM-dd')
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
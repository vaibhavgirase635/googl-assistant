import random
import torch
import json
from brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
from Listen import take_command
from Speak import talk
from Task import NonInputExecution, InputExecution
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

def Main():
    sentence = take_command()
    print(sentence)
    if sentence == 'bye':
        talk("Bye sir")
        exit()
    
    sentence = tokenize(sentence)
    # print(sentence)
    x = bag_of_words(sentence, all_words)
    # print(x)
    x = x.reshape(1,x.shape[0])
    # print(x)
    x = torch.from_numpy(x).to(device)
    # print(x)
    output = model(x)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]
    print(tag)
    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]
    print(prob.item())
    if prob.item() > 0.55:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                print(reply)
                if "time" in reply:
                    NonInputExecution(reply)

                elif "date" in reply:
                    NonInputExecution(reply)

                elif "day" in reply:
                    NonInputExecution(reply)
                
                elif "wikipedia" in reply:
                    InputExecution(reply, sentence)

                else:
                    talk(reply) 

while True:

    Main()
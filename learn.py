import torch
from data import tokenizer, model
import wikipedia
import speech_recognition as sr
import pyttsx3
from transformers import logging

logging.set_verbosity_warning()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def main(question):
    question = question
    context = wikipedia.summary(question, 1)

    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors='pt')
    input_ids = inputs["input_ids"].tolist()[0]
    with torch.no_grad():
        outputs = model(**inputs)
    start_index = torch.argmax(outputs.start_logits)
    end_index = torch.argmax(outputs.end_logits)
    answer = tokenizer.decode(input_ids[start_index:end_index + 1], skip_special_tokens=True)

    print("Question:", question)
    print("Answer:", answer)
    return answer


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
            with sr.Microphone() as source:
                print("Listening.....")
                talk('Please tell me how can I help you')
                #print(voice)
                voice = listener.listen(source)
            try:
                audio = listener.recognize_google(voice)
                print(audio)
                command = audio
            except Exception as e:
                print('Say that again')
                talk("Please tell me again")
                return None
            #print(command)
            
            return command
                

if __name__ == '__main__':
      while True:
            query = take_command()
            try:
                
                print(query)
                ans = main(query)
                talk(ans)
                
                
            except Exception as e:
                talk("Answer of your question not found")
                
            
import datetime
from Speak import talk
import wikipedia
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    print(time)
    talk(f'The time is {time}')

def Date():
    date = datetime.date.today()
    print(date)
    talk(f"Today's date is {date}")

def Day():
    day = datetime.datetime.now().strftime("A")
    print(day)
    talk(f"Today is {day}")

def NonInputExecution(query):
    query = str(query)
    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","")
        result = wikipedia.summary(name)
        print(result)
        talk(result)
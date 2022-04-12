import speech_recognition as sr
from web_automation import *
from web_auto import *
from web_auto1 import *
from words import *
import datetime
import pyjokes
import pyttsx3 as p

#initial conversation
r1 = sr.Recognizer()
engine = p.init()
voices=engine.getProperty('voices')
engine.setProperty("voice", voices[1].id) 
engine.say("Hello, I am Alexa")
engine.runAndWait()
engine.say("what can i do for you?")
engine.runAndWait()



def run_alexa():
    #giving instruction
    r2=sr.Recognizer()
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source)
        print("listening....")
        audio=r2.listen(source)
        try:
            instruction =r2.recognize_google(audio)
            instruction=instruction.lower()
            print(instruction)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

    #getting info from wiki
    r3=sr.Recognizer()
    if "information" in instruction:
        engine.say("information about what?")
        engine.runAndWait()
        print("listenning...")
        with sr.Microphone() as source1:
            audio2=r3.listen(source1)
            try:
                information = r3.recognize_google(audio2)
                bot=info()
                bot.get_info(information)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    #movie rating
    r4=sr.Recognizer()
    if "review" in instruction:
        engine.say("what is the name of the movie?")
        print("what is the name of the movie?")
        engine.runAndWait()
        print("listenning...")
        with sr.Microphone() as source2:
            audio3=r4.listen(source2)
            try:
                rating=r4.recognize_google(audio3)
                bot=movie()
                bot.movie_review(rating)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    #open video on youtube
    r5=sr.Recognizer()
    if "video" in instruction:
        engine.say("which video you want me to open?")
        print("which video you want me to open?")
        engine.runAndWait()
        print("listenning...")
        with sr.Microphone() as source2:
            audio4=r5.listen(source2)
            try:
                video=r5.recognize_google(audio4)
                bot=music()
                bot.play(video)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    #word meanings
    r6=sr.Recognizer()
    if "meaning" in instruction:
        engine.say("which word sire?")
        print("which word sire?")
        engine.runAndWait()
        with sr.Microphone() as source2:
            audio5=r5.listen(source2)
            try:
                word=r6.recognize_google(audio5)
                bot=mean()
                bot.word_mean(word)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    #time
    if 'time' in instruction:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say('current time is' + time)
        engine.runAndWait()

    #date
    if 'are you single' in instruction:
        engine.say('i am in a relationship with wifi')
        print('i am in a relationship with wifi')
        engine.runAndWait()

    #jokes
    if 'joke' in instruction:
        j=pyjokes.get_joke()
        print(j)
        engine.say(j)
        engine.runAndWait()

    #date
    if 'date' in instruction:
        date = datetime.datetime.now().strftime('%d %B %Y')
        print(date)
        engine.say("today's date is" + date)
        engine.runAndWait()



while True:
    run_alexa()







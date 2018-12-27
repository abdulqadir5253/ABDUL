from gtts import gTTS
import speech_recognition as sr
import os
import datetime
import socket
import sys

flag = 1


def lamiya_listens():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Speak")
        audio = r.listen(source)
        print(r.recognize_google(audio))
    return r.recognize_google(audio)


def wish():
    current = datetime.datetime.now()
    time = current.hour
    if 0 < time < 12:
        text = "Good Morning Abdul"
    elif 12 < time < 16:
        text = "Good Afternoon Abdul"
    else:
        text = "Good Evening Abdul"
    lang = "en"
    myobj = gTTS(text=text, lang=lang)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")


def lamiya_speaks(audio):
    if flag == 1:
        wish()
        return

    if audio == "open chrome":
        os.system("start chrome")
    elif audio == "open pycharm":
        os.startfile("C:\\Program Files\JetBrains\PyCharm Community Edition 2018.1\bin")
    else:
        print("Exiting")



def is_connected(hostname):
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False


if not is_connected("www.google.com"):
    print("No Internet")
    sys.exit()
lamiya_speaks("tst")
flag = 0
audio = "hello"
while audio != "bye":
    audio = lamiya_listens()
    audio = audio.lower()
    lamiya_speaks(audio)



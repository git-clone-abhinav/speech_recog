import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("I'm Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)

except:
    print("Mic not found")
    pass





'''friend = pyttsx3.init()
while True:
    speech = input("Say something :")
    friend.say(speech)
    friend.runAndWait()
'''
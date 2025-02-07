import speech_recognition as sr
from django.http import JsonResponse
from django.shortcuts import render
import pyttsx3
import os
import webbrowser
import subprocess



def index(request):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    pyttsx3.speak("HEllo I am your assistant How I help you ?")
    return render(request, 'index.html')
    



# Create a function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    pyttsx3.speak("SPEAK")
    # Use microphone to listen to the user
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print("You said: ", text)
        pyttsx3.speak(text)
        return text
            
    except sr.UnknownValueError:
        pyttsx3.speak("Sorry, I didn't understand that. please speak again")
        return "Sorry, I didn't understand that."
    except sr.RequestError:
        pyttsx3.speak( "Sorry, I'm having trouble connecting to the service.")

# Create a view to handle the interaction
def voice_assistant(request):
    user_input = recognize_speech()
    # Create a response based on the user input
    if "hello" in user_input.lower():
        assistant_response = "Hello! How can I assist you today?"
    elif "time" in user_input.lower():
        from datetime import datetime
        hour=int(datetime.now().hour)
        if hour>=0 and hour<12:
            pyttsx3.speak("Good morning. sir")
        elif hour>=12 and hour<18:
            pyttsx3.speak("Good Afternoon. sir")
        else:
            pyttsx3.speak("Good Evening...sir")
        assistant_response = "The current time is " + datetime.now().strftime("%H:%M:%S")

        pyttsx3.speak("Current time is..."+datetime.now().strftime("%H:%M:%S"))
       
    elif "goodbye" in user_input.lower():
        assistant_response = "Goodbye! Have a nice day!"
    elif  "opening google" in user_input.lower():
        open_google()
    elif  "opening youtube" in user_input.lower():
        open_youtube()
    elif  "opening chatgpt" in user_input.lower():
        open_chatgpt()

    elif  "opening college website" in user_input.lower():
        open_SIIT()
    elif  "opening instagram" in user_input.lower():
        open_Insta()
    elif "open eclipse" in user_input.lower():
        eclipse_path = "D:\java-2024-06\eclipse\eclipse.exe" 
        if os.path.exists(eclipse_path):
            os.startfile(eclipse_path)  # This opens the file in Windows
            pyttsx3.speak("Opening Eclipse IDE.")
    elif "open notepad" in user_input.lower():
                pyttsx3.speak("Opening Notepad.")
                os.system("notepad")
   
    else:
        assistant_response = "I'm sorry, I didn't catch that."
    

    return JsonResponse({"response": assistant_response})

def open_google():
    webbrowser.open("https://www.google.com")
def open_youtube():
    webbrowser.open("https://www.youtube.com")
    pyttsx3.speak("Opening Youtube.")
def open_chatgpt():
    webbrowser.open("https://chatgpt.com/")
    pyttsx3.speak("Opening chatgpt.")
def open_SIIT():
    webbrowser.open("https://siitpaniv.org/")
    pyttsx3.speak("Opening SIIT collage Home page")
def open_Insta():
    webbrowser.open("https://www.instagram.com/accounts/login/?hl=en")
    pyttsx3.speak("Opening Instagramm")

import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import requests
import math
import webbrowser
import pytemperature


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am Jarvis!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                  
    with sr.Microphone() as source:                                                                      
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print('User said: ' + query +'\n')
       
    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login(yourgmail@.com', '*******')
#     server.sendmail('yourgmail@gmail.com', to, content)
#     server.close()
       

if __name__ == '__main__':

    while True:
   
        query = myCommand();
        query = query.lower()
       
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')



        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'open instagram' in query:
            speak('okay')
            webbrowser.open('www.instagram.com')

        elif 'firstcry' in query:
            speak('okay')
            webbrowser.open('https://www.firstcry.com/')    

        elif 'open facebook' in query:
            speak('okay')
            webbrowser.open('www.facebook.com')

        elif 'open whatsapp' in query:
            speak('okay')
            webbrowser.open('https://web.whatsapp.com/')

        elif 'location' in query:
            res = requests.get('https://ipinfo.io/')
            data = res.json()

            city = data['city']
            region= data['region']

            location=data['loc'].split(',')
            latitude=location[0]
            longitude=location[1]

            print("latitude : ",latitude)
            print("longitude : ",longitude)
            print("city : ",city)
            print("region : ",region)

            speak(f"your location is {city}{region}{latitude}{longitude}")

       
           

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

       
       
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')
            print('Hello sir')

        elif 'thakyou' in query:
            speak('most wlcom sir')
            print('most wlcom sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = myCommand()
                to = "dilpreetkaurchawla.2121@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
           
       elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(f" time is {strTime}")


        elif 'weather' in query:
            speak("searching Weather..")
            query = query.replace("weatdeher", "")
            results = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
            speak("speak city name")
            city = takeCommand().lower()
            url = results + city
            json_data = requests.get(url).json()
            speak("according to Open Weather, weather condtion is")
            y = json_data["main"]
            current_temperature = math.ceil(pytemperature.k2c((y["temp"])))
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]

            weather_des = json_data['weather'][0]["description"]

            print(" Temperature  = " +
                  str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_des))

            speak(
                f" Temperature is {current_temperature} degree celcius. atmospheric pressure (in hPa unit) is {current_pressure}. humidity (in percentage) is {current_humidiy} and {weather_des}")
            speak(f"in {city}")

            if "rain" in weather_des:
                speak('take your umbrella with you')
            else:
                speak("")

         
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(resultsb)
                   
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
       
            except:
                webbrowser.open('www.google.com')
        speak('Next Command please..')

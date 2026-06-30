import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")


if __name__ == "__main__":

    speak("Initializing Sanju")

    while True:

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(
                    source,
                    timeout=2,
                    phrase_time_limit=2
                )

            word = recognizer.recognize_google(audio)

            if word.lower() == "sanju":

                speak("Hello, I am Sanju. How can I help you?")

                with sr.Microphone() as source:
                    print("Sanju is listening...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                processCommand(command)

        except Exception as e:
            print("Error:", e)
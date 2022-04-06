import speech_recognition
import pyttsx3
import os

recognizer = speech_recognition.Recognizer()

def closeFile():
    try:
        os.system('TASKKILL /F /IM Hearthstone.exe')
    except Exception as e:
        print(str(e))

while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

            if 's***' in text or "f***" in text or "damn" in text or "dogshit" in text or "damnit" in text or "pineapple" in text or "b****" in text or "niger" in text or "faget" in text or "Jello" in text:
                closeFile()




    except:
        print("error")

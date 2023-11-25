import speech_recognition as sr
import datetime

# Initialize recognizer
recognizer = sr.Recognizer()

def assistant_response(text):
    print("Assistant:", text)

def process_command(command):
    if "hello" in command:
        assistant_response("Hello there!")
    elif "time" in command:

        
        now = datetime.datetime.now().strftime("%I:%M %p")
        assistant_response(f"The current time is {now}.")
    elif "date" in command:
        today = datetime.date.today().strftime("%A, %B %d, %Y")
        assistant_response(f"Today is {today}.")
    else:
        assistant_response("Sorry, I didn't understand that.")

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("User:", command)
        process_command(command)
    except sr.UnknownValueError:
        assistant_response("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        assistant_response("Sorry, there was an error processing your request.")

if __name__ == "__main__":
    while True:
        listen()

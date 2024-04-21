# Import libs
import google.generativeai as genai
from gtts import gTTS
import speech_recognition
from playsound import playsound
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Initialize robot ear
robot_ear = speech_recognition.Recognizer()

# Config Gemini AI
genai.configure(api_key=os.getenv("AI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Load file history (data.json)
try:
    with open('data.json', 'r') as file:
        try:
            data = json.load(file)
            chat = model.start_chat(history=data["data"])
        except:
            with open("data.json", "w") as save:
                data = {"data": []}
                chat = model.start_chat(history=[])
                json.dump(data, save)
except:
    with open("data.json", "w") as save:
        data = {"data": []}
        chat = model.start_chat(history=[])
        json.dump(data, save)

# Process
while (True):
    # Listen user
    with speech_recognition.Microphone() as mic:
        robot_ear.adjust_for_ambient_noise(mic)
        print("Robot: Tôi đang nghe")
        audio = robot_ear.listen(mic)
    
    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio, language="vi-VN")
        print(f"You: {you}")
    except:
        you = ""
    if (you == ""):
        continue
    
    # Chat input if u want
    # you = input("You: ")
    
    # Send message to Gemini AI
    response = chat.send_message(you)
    print(f"Robot: {response.text}")
    
    # Update the history (data.json)
    # Convert Python object to JSON
    history = [{"role": el.role, "parts": [text.text for text in el.parts]} for el in chat.history]
    data["data"] = history
    with open("data.json", "w") as file:
        json.dump(data, file)
    
    # Play robot sound
    text = gTTS(text=response.text, lang="vi")
    text.save("robot_voice.mp3")
    playsound("robot_voice.mp3")
    os.remove("robot_voice.mp3")
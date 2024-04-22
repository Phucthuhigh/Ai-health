# Import libs
import google.generativeai as genai
from gtts import gTTS
import speech_recognition
from playsound import playsound
import os
from dotenv import load_dotenv
import json
import re
import random
from youtubesearchpython import VideosSearch
import webbrowser

GREEN = '\033[92m'
WHITE = '\33[0m'

# Find all names of the songs in string
def find_songs_in_string(string):
    regex = r"\<(.+)\>"
    songs = re.findall(regex, string)
    return songs

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
    # with speech_recognition.Microphone() as mic:
    #     robot_ear.adjust_for_ambient_noise(mic)
    #     print(f"{GREEN}Robot: Tôi đang nghe")
    #     audio = robot_ear.listen(mic)
    
    # print(f"{GREEN}Robot: ...")

    # try:
    #     you = robot_ear.recognize_google(audio, language="vi-VN")
    #     print(f"{WHITE}You: {you}")
    # except:
    #     you = ""
    # if (you == ""):
    #     continue
    
    # Chat input if u want
    you = input(f"{WHITE}\nYou: ")
    
    # Send message to Gemini AI
    try:
        response = chat.send_message(you)
        print(f"{GREEN}\nRobot: {response.text}")
        
        # Check if the song in output then play song on youtube
        songs = find_songs_in_string(response.text)
        if (len(songs) > 0):
            song = random.choice(songs)
            videosSearch = VideosSearch(song, limit = 1)
            try:
                linkVideo = videosSearch.result()["result"][0]["link"]
                webbrowser.open_new_tab(linkVideo)
            except:
                print(f"{GREEN}\nTiếc quá, tớ kiếm video này trên mạng không ra rồi :(")
    except:
        print(f"{GREEN}\nRobot: Câu nói của bạn không phù hợp tiêu chuẩn đạo đức!!!")
    
    # Update the history (data.json)
    # Convert Python object to JSON
    history = [{"role": el.role, "parts": [text.text for text in el.parts]} for el in chat.history]
    data["data"] = history
    with open("data.json", "w") as file:
        json.dump(data, file)
    
    # Play robot sound
    # text = gTTS(text=response.text, lang="vi")
    # text.save("robot_voice.mp3")
    # playsound("robot_voice.mp3")
    # os.remove("robot_voice.mp3")
import speech_recognition as sr
import pygame
import threading
import requests

# Initialize the pygame mixer for playing audio
pygame.mixer.init()

# Function to play sound using threading to avoid blocking
def play_sound(file_path):
    def _play_sound():
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    thread = threading.Thread(target=_play_sound)
    thread.start()

# Function to recognize speech and act accordingly
def recognize_speech_and_act():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        print("Listening for commands...")

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            base_url = "http://192.168.98.158"
            sound_path = "C:/Users/sak78/Downloads"

            if command == "bujji":
                play_sound(f"{sound_path}/ayyoout.wav")
                response = requests.post(f"{base_url}/smrik")
            elif command == "bujji hands up":
                play_sound(f"{sound_path}/abbaout.wav")

                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/handsup")
            elif command == "bujji hands down":
                play_sound(f"{sound_path}/abbaout.wav")

                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/handsdown")
            elif command == "bujji come here":
                play_sound(f"{sound_path}/vastunnaleout.wav")
                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/fwd")
            elif command == "stop":
                play_sound(f"{sound_path}/complecxout.wav")
                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/stop")
            elif command == "turn left":
                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/fwdLeft")
            elif command == "turn right":
                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/fwdRight")
            elif command == "reverse":
                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/rev")
            elif command == "reverse left":
                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/revLeft")
            elif command == "reverse right":
                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/revRight")
            elif command == "bujji dance":
                play_sound(f"{sound_path}/abbaout.wav")

                response = requests.post(f"{base_url}/smrik")
                response = requests.post(f"{base_url}/dance")
            else:
                print("Command not recognized.")
                continue

            if response.status_code == 200:
                print(f"{command} command executed.")
            else:
                print(f"Failed to send command to robot: {response.status_code}")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if _name_ == "_main_":
    recognize_speech_and_act()

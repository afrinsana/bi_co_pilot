import speech_recognition as sr
import pyttsx3
from core.config import Config

class VoiceInterface:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
    
    def listen(self) -> str:
        """Convert speech to text."""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except Exception as e:
                print("Error:", e)
                return ""
    
    def speak(self, text: str) -> None:
        """Convert text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

# Example usage:
# voice = VoiceInterface()
# user_input = voice.listen()
# voice.speak("Hello! How can I help?")
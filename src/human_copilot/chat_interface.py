from .voice_interface import VoiceInterface
from .productivity_tools import ProductivityTools
from .memory import UserMemory
from .multimodal import MultiModalProcessor

class HumanCoPilot:
    def __init__(self):
        self.voice = VoiceInterface()
        self.tools = ProductivityTools()
        self.memory = UserMemory()
        self.multimodal = MultiModalProcessor()
    
    def run(self):
        print("HCP: Voice or text input? (say 'voice' or type text)")
        choice = input("You: ").lower()
        
        if choice == "voice":
            user_input = self.voice.listen()
            self.voice.speak(f"You said: {user_input}")
        else:
            user_input = input("You: ")
        
        # Add logic to route tasks (e.g., "schedule meeting" -> calendar)
        if "schedule" in user_input:
            events = self.tools.get_upcoming_events()
            print("Upcoming events:", events)
        elif "remember" in user_input:
            key, value = user_input.split("remember")[1].split("is")
            self.memory.store(key.strip(), value.strip())
        else:
            print("HCP: I'll process this further!")

if __name__ == "__main__":
    hcp = HumanCoPilot()
    hcp.run()
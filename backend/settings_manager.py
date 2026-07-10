from PySide6.QtCore import QObject
import json
import os

class SettingsManager(QObject):
    
    SETTINGS_FILE = "settings.json"
    DEFAULT_SETTINGS = {
    "server_executable": "M:\\Starbound_Things\\OpenStarbound-Windows-Server\\win\\starbound_server.exe",
    "server_directory": "M:\\Starbound_Things\\OpenStarbound-Windows-Server\\win",
    "ngrok_executable": "M:\\Starbound_Things\\OpenStarbound-Windows-Server\\win\\tools\\ngrok.exe",
    "ngrok_directory": "M:\\Starbound_Things\\OpenStarbound-Windows-Server\\win\\tools",
    "universe_path": "...",
    "assets_path": "...",
    "use_ngrok": True
}
    
    def __init__(self):
        super().__init__()
        
        if os.path.isfile(self.SETTINGS_FILE):
            self.load_settings()
        else:
            self.create_default_settings()     
            
                
    def create_default_settings(self):
        with open(self.SETTINGS_FILE, "w") as file:
                json.dump(self.DEFAULT_SETTINGS, file, indent=4)
                self.settings = self.DEFAULT_SETTINGS.copy()
               
    
    def load_settings(self):
        with open(self.SETTINGS_FILE, "r") as file:
            self.settings = json.load(file)           
                
                
    def save_settings(self):
        with open(self.SETTINGS_FILE, 'w') as file:
            json.dump(self.settings, file, indent=4)
            

    def update_settings(self, new_settings):
        self.settings = new_settings
        self.save_settings()
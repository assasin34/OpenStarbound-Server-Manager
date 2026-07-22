from PySide6.QtCore import QObject, QTimer, Signal
from backend.settings_manager import SettingsManager
import json
import os

class ConfigManager(QObject):
    
    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        
        self.settings_manager = settings_manager
            
    
    def load_config(self):
        self.config_file = f"{self.settings_manager.settings["storage_path"]}/starbound_server.config"
        
        if os.path.isfile(self.config_file):
            with open(self.config_file, "r") as file:
                self.config = json.load(file)   
            return True
        else:
            return False 
            
    
    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=3)
         
            
    def update_config(self, new_config):
        self.config = new_config
        self.save_config()
        
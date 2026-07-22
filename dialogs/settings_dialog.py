from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog, QLineEdit
from PySide6.QtCore import Signal
from ui.SettingsWindow import Ui_Dialog
from backend.settings_manager import SettingsManager
import os

class SettingsDialog(QDialog, Ui_Dialog):
    settings_changed = Signal(dict)
    
    def __init__(self, settings_manager: SettingsManager):
        super().__init__()
        self.setupUi(self)

        self.settings_manager = settings_manager
        self.settings = settings_manager.settings.copy()
        
        self.lineEditServerExecutable.setText(self.settings["server_executable"])
        self.lineEditServerExecutableFolder.setText(self.settings["server_directory"])
        self.lineEditStorageFolder.setText(self.settings["storage_path"])
        self.lineEditNgrokExecutable.setText(self.settings["ngrok_executable"])
        self.lineEditNgrokExecutableFolder.setText(self.settings["ngrok_directory"])
        self.checkBoxUseNgrok.setChecked(self.settings["use_ngrok"])
        
        self.disable_ngrok_settings(self.checkBoxUseNgrok.isChecked())
        
        self.btnServerExecutableBrowse.clicked.connect(lambda: self.browse_file(self.lineEditServerExecutable))
        self.btnServerExecutableFolderBrowse.clicked.connect(lambda: self.browse_folder(self.lineEditServerExecutableFolder))
        self.btnStorageFolderBrowse.clicked.connect(lambda: self.browse_folder(self.lineEditStorageFolder))
        self.btnNgrokExecutableBrowse.clicked.connect(lambda: self.browse_file(self.lineEditNgrokExecutable))
        self.btnNgrokExecutableFolderBrowse.clicked.connect(lambda: self.browse_folder(self.lineEditNgrokExecutableFolder))
        
        self.checkBoxUseNgrok.toggled.connect(self.disable_ngrok_settings)
        self.buttonBox.accepted.connect(self.accept_changes)
    
    
    def browse_file(self, setting_name: QLineEdit):
        path = QFileDialog.getOpenFileName(caption="Select starbound_server.exe", filter="starbound_server (*.exe)")[0]
        if "starbound_server.exe" in path:
            setting_name.setText(path)
            self.lineEditServerExecutableFolder.setText(path[:-20])
            self.lineEditStorageFolder.setText(f"{path[:-24]}storage/")
        elif "ngrok.exe" in path:
            setting_name.setText(path)
            self.lineEditNgrokExecutableFolder.setText(path[:-9])
        else:
            self.popup("Wrong file", "Please select a correct exe file.")
        
        
    def browse_folder(self, setting_name: QLineEdit):
        path = QFileDialog.getExistingDirectory()
        setting_name.setText(path)
    
        
    def accept_changes(self):
        self.settings["server_executable"] = self.lineEditServerExecutable.text()
        self.settings["server_directory"] = self.lineEditServerExecutableFolder.text()
        self.settings["ngrok_executable"] = self.lineEditNgrokExecutable.text()
        self.settings["ngrok_directory"] = self.lineEditNgrokExecutableFolder.text()
        self.settings["storage_path"] = self.lineEditStorageFolder.text()
        self.settings["use_ngrok"] = self.checkBoxUseNgrok.isChecked()
        
        self.settings_manager.update_settings(self.settings)
        
        
    def disable_ngrok_settings(self, checked):
            ngrok_settings = [
            self.lineEditNgrokExecutable,
            self.lineEditNgrokExecutableFolder,
            self.btnNgrokExecutableBrowse,
            self.btnNgrokExecutableFolderBrowse,
            ]
            
            for widget in ngrok_settings:
                widget.setDisabled(not checked)
                
    
    def popup(self, window_title, text):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(window_title)
        msgBox.setText(text)
        msgBox.exec()
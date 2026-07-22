from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog, QLineEdit
from PySide6.QtCore import Signal
from ui.ConfigWindow import Ui_Dialog
from backend.config_manager import ConfigManager


class ConfigDialog(QDialog, Ui_Dialog):
    
    def __init__(self, config_manager: ConfigManager):
        super().__init__()
        self.setupUi(self)
        
        self.config_manager = config_manager
        self.config = config_manager.config.copy()
        
        self.lineEditServerName.setText(self.config["serverName"])
        self.spinBoxServerPort.setValue(self.config["gameServerPort"])
        self.spinBoxMaxPlayers.setValue(self.config["maxPlayers"])
        self.spinBoxTeamSize.setValue(self.config["maxTeamSize"])
        self.checkBoxAllowAdminCommands.setChecked(self.config["allowAdminCommands"])
        self.checkBoxAllowAdminCommandsFromAnyone.setChecked(self.config["allowAdminCommandsFromAnyone"])
        self.checkBoxAllowAnonymousConnections.setChecked(self.config["allowAnonymousConnections"])
        self.checkBoxAllowAssetsMismatch.setChecked(self.config["allowAssetsMismatch"])
        self.checkBoxAnonymousConnectionsAreAdmin.setChecked(self.config["anonymousConnectionsAreAdmin"])
        
        self.buttonBox.accepted.connect(self.accept_changes)
        
        
    def accept_changes(self):
        self.config["serverName"] = self.lineEditServerName.text()
        self.config["gameServerPort"] = self.spinBoxServerPort.value()
        self.config["maxPlayers"] = self.spinBoxMaxPlayers.value()
        self.config["maxTeamSize"] = self.spinBoxTeamSize.value()
        self.config["allowAdminCommands"] = self.checkBoxAllowAdminCommands.isChecked()
        self.config["allowAdminCommandsFromAnyone"] = self.checkBoxAllowAdminCommandsFromAnyone.isChecked()
        self.config["allowAnonymousConnections"] = self.checkBoxAllowAnonymousConnections.isChecked()
        self.config["allowAssetsMismatch"] = self.checkBoxAllowAssetsMismatch.isChecked()
        self.config["anonymousConnectionsAreAdmin"] = self.checkBoxAnonymousConnectionsAreAdmin.isChecked()
        
        self.config_manager.update_config(self.config)
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(651, 244)
        Dialog.setMinimumSize(QSize(651, 244))
        Dialog.setMaximumSize(QSize(651, 16777215))
        Dialog.setStyleSheet(u"QDialog { background-color: rgb(236, 236, 236) }\\n")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, 210, 651, 32))
        self.buttonBox.setMaximumSize(QSize(651, 32))
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 651, 211))
        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 30, 651, 21))
        self.line_4.setStyleSheet(u"")
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4.setLineWidth(1)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 6, 191, 41))
        self.label.setStyleSheet(u"font: 700 18pt \"Arial\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 40, 281, 161))
        self.lineEditServerName = QLineEdit(self.groupBox_2)
        self.lineEditServerName.setObjectName(u"lineEditServerName")
        self.lineEditServerName.setGeometry(QRect(10, 50, 261, 26))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 81, 16))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 71, 16))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 90, 71, 16))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 90, 71, 16))
        self.spinBoxServerPort = QSpinBox(self.groupBox_2)
        self.spinBoxServerPort.setObjectName(u"spinBoxServerPort")
        self.spinBoxServerPort.setGeometry(QRect(10, 110, 81, 21))
        self.spinBoxServerPort.setStyleSheet(u"QSpinBox {\n"
"	border: 1px solid;\n"
"}\n"
"QSpinBox::down-button {\n"
"    subcontrol-position: bottom right;\n"
"    width: 18px;\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-position: top right;\n"
"    width: 18px;\n"
"}")
        self.spinBoxServerPort.setAccelerated(True)
        self.spinBoxServerPort.setMinimum(1)
        self.spinBoxServerPort.setMaximum(65535)
        self.spinBoxMaxPlayers = QSpinBox(self.groupBox_2)
        self.spinBoxMaxPlayers.setObjectName(u"spinBoxMaxPlayers")
        self.spinBoxMaxPlayers.setGeometry(QRect(100, 110, 81, 21))
        self.spinBoxMaxPlayers.setStyleSheet(u"QSpinBox {\n"
"	border: 1px solid;\n"
"}\n"
"QSpinBox::down-button {\n"
"    subcontrol-position: bottom right;\n"
"    width: 18px;\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-position: top right;\n"
"    width: 18px;\n"
"}")
        self.spinBoxMaxPlayers.setAccelerated(True)
        self.spinBoxMaxPlayers.setMaximum(99999)
        self.spinBoxTeamSize = QSpinBox(self.groupBox_2)
        self.spinBoxTeamSize.setObjectName(u"spinBoxTeamSize")
        self.spinBoxTeamSize.setGeometry(QRect(190, 110, 81, 21))
        self.spinBoxTeamSize.setStyleSheet(u"QSpinBox {\n"
"	border: 1px solid;\n"
"}\n"
"QSpinBox::down-button {\n"
"    subcontrol-position: bottom right;\n"
"    width: 18px;\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-position: top right;\n"
"    width: 18px;\n"
"}")
        self.spinBoxTeamSize.setAccelerated(True)
        self.spinBoxTeamSize.setMaximum(999)
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(300, 40, 341, 161))
        self.verticalLayoutWidget = QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 26, 251, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 26, 31, 121))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBoxAllowAdminCommands = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxAllowAdminCommands.setObjectName(u"checkBoxAllowAdminCommands")

        self.verticalLayout_2.addWidget(self.checkBoxAllowAdminCommands)

        self.checkBoxAllowAdminCommandsFromAnyone = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxAllowAdminCommandsFromAnyone.setObjectName(u"checkBoxAllowAdminCommandsFromAnyone")

        self.verticalLayout_2.addWidget(self.checkBoxAllowAdminCommandsFromAnyone)

        self.checkBoxAllowAnonymousConnections = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxAllowAnonymousConnections.setObjectName(u"checkBoxAllowAnonymousConnections")

        self.verticalLayout_2.addWidget(self.checkBoxAllowAnonymousConnections)

        self.checkBoxAllowAssetsMismatch = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxAllowAssetsMismatch.setObjectName(u"checkBoxAllowAssetsMismatch")

        self.verticalLayout_2.addWidget(self.checkBoxAllowAssetsMismatch)

        self.checkBoxAnonymousConnectionsAreAdmin = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBoxAnonymousConnectionsAreAdmin.setObjectName(u"checkBoxAnonymousConnectionsAreAdmin")

        self.verticalLayout_2.addWidget(self.checkBoxAnonymousConnectionsAreAdmin)

        self.groupBox.raise_()
        self.buttonBox.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Config", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Config", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"General", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Server Name:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Server Port:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Max Players:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Team Size:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Permissions", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Allow Admin Commands", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Allow Admin Commands From Anyone", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Allow Anonymous Connections", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Allow Assets Mismatch", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Anonymous Connections Are Admin", None))
        self.checkBoxAllowAdminCommands.setText("")
        self.checkBoxAllowAdminCommandsFromAnyone.setText("")
        self.checkBoxAllowAnonymousConnections.setText("")
        self.checkBoxAllowAssetsMismatch.setText("")
        self.checkBoxAnonymousConnectionsAreAdmin.setText("")
    # retranslateUi


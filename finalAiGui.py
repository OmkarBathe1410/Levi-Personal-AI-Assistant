from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_finalAiGui(object):
    def setupUi(self, finalAiGui):
        finalAiGui.setObjectName("finalAiGui")
        finalAiGui.resize(1280, 720)
        finalAiGui.setStatusTip("")
        finalAiGui.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.leviLogo = QtWidgets.QLabel(finalAiGui)
        self.leviLogo.setGeometry(QtCore.QRect(320, -20, 611, 151))
        self.leviLogo.setStyleSheet("border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/LEVI_AI_logo-removebg-preview.png);\n"
"background-color: transparent;")
        self.leviLogo.setText("")
        self.leviLogo.setObjectName("leviLogo")
        self.exitButton = QtWidgets.QPushButton(finalAiGui)
        self.exitButton.setGeometry(QtCore.QRect(1080, 630, 191, 91))
        self.exitButton.setStyleSheet("border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Exit_btn.png);\n"
"background-color: transparent;")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        self.codingWindow = QtWidgets.QLabel(finalAiGui)
        self.codingWindow.setGeometry(QtCore.QRect(0, 0, 311, 181))
        self.codingWindow.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"image: url(F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Code_Template.gif);\n"
"border-style:solid;\n"
"border-width:0.5px 0.5px 0.5px 0.5px;\n"
"")
        self.codingWindow.setText("")
        self.codingWindow.setObjectName("codingWindow")
        self.terminalText = QtWidgets.QPlainTextEdit(finalAiGui)
        self.terminalText.setGeometry(QtCore.QRect(0, 499, 1071, 181))
        self.terminalText.setEnabled(True)
        self.terminalText.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width:0.5px 0.5px 0.5px 0.5px;\n"
"font: 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(0, 128, 0);\n"
"padding-left: 2px;\n"
"padding-top: 2px;")
        self.terminalText.setPlainText("")
        self.terminalText.setObjectName("terminalText")
        self.inputText = QtWidgets.QPlainTextEdit(finalAiGui)
        self.inputText.setGeometry(QtCore.QRect(0, 680, 951, 41))
        self.inputText.setEnabled(True)
        self.inputText.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width:2px 2px 2px 2px;\n"
"font: 12pt \"Arial Rounded MT Bold\";\n"
"color: rgb(0, 128, 0);\n"
"padding-left: 5px;\n"
"padding-top: 5px;")
        self.inputText.setPlainText("")
        self.inputText.setObjectName("inputText")
        self.enterButton = QtWidgets.QPushButton(finalAiGui)
        self.enterButton.setGeometry(QtCore.QRect(939, 673, 141, 51))
        self.enterButton.setStyleSheet("border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Enter_btn.png);\nbackground-color: transparent;")
        self.enterButton.setText("")
        self.enterButton.setObjectName("enterButton")
        self.loadingLbl = QtWidgets.QLabel(finalAiGui)
        self.loadingLbl.setGeometry(QtCore.QRect(390, 110, 500, 375))
        self.loadingLbl.setStyleSheet("border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Earth.gif);")
        self.loadingLbl.setText("")
        self.loadingLbl.setObjectName("loadingLbl")
        self.listenLbl = QtWidgets.QLabel(finalAiGui)
        self.listenLbl.setGeometry(QtCore.QRect(390, 110, 500, 375))
        self.listenLbl.setStyleSheet("border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/VoiceReg/Siri.gif);")
        self.listenLbl.setText("")
        self.listenLbl.setObjectName("listenLbl")
        self.speakLbl = QtWidgets.QLabel(finalAiGui)
        self.speakLbl.setGeometry(QtCore.QRect(340, 130, 601, 351))
        self.speakLbl.setStyleSheet("\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Jarvis_Gui (1).gif);")
        self.speakLbl.setText("")
        self.speakLbl.setObjectName("speakLbl")
        self.loadingLbl.raise_()
        self.listenLbl.raise_()
        self.exitButton.raise_()
        self.codingWindow.raise_()
        self.terminalText.raise_()
        self.inputText.raise_()
        self.enterButton.raise_()
        self.speakLbl.raise_()
        self.leviLogo.raise_()

        self.retranslateUi(finalAiGui)
        QtCore.QMetaObject.connectSlotsByName(finalAiGui)

    def retranslateUi(self, finalAiGui):
        _translate = QtCore.QCoreApplication.translate
        finalAiGui.setWindowTitle(_translate("finalAiGui", "finalAiGui"))
        self.terminalText.setPlaceholderText(_translate("finalAiGui", "Terminal Output Here"))
        self.inputText.setPlaceholderText(_translate("finalAiGui", "Enter Your Command"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    finalAiGui = QtWidgets.QWidget()
    ui = Ui_finalAiGui()
    ui.setupUi(finalAiGui)
    finalAiGui.show()
    sys.exit(app.exec_())
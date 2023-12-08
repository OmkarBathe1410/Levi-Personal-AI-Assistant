from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 576)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/LEVI_AI_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        
        self.Levi = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Levi.setFont(font)
        self.Levi.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Levi.setObjectName("Levi")
        
        
        self.leviLogo = QtWidgets.QLabel(self.Levi)
        self.leviLogo.setGeometry(QtCore.QRect(293, -10, 310, 100))
        self.leviLogo.setStyleSheet("background-color: transparent;")
        self.leviLogo.setText("")
        self.leviLogo.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/LEVI_AI_logo-removebg-preview.png"))
        self.leviLogo.setScaledContents(True)
        self.leviLogo.setObjectName("leviLogo")
        
        
        self.speakLbl = QtWidgets.QLabel(self.Levi)
        self.speakLbl.setGeometry(QtCore.QRect(320, 100, 270, 200))
        self.speakLbl.setStyleSheet("background-color: transparent;")
        self.speakLbl.setText("")
        self.speakLbl.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Speaking_Levi.gif"))
        self.speakLbl.setScaledContents(True)
        self.speakLbl.setObjectName("speakLbl")
        
        
        self.listenLbl = QtWidgets.QLabel(self.Levi)
        self.listenLbl.setGeometry(QtCore.QRect(320, 100, 270, 200))
        self.listenLbl.setStyleSheet("background-color: transparent;")
        self.listenLbl.setText("")
        self.listenLbl.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Listening_Levi.gif"))
        self.listenLbl.setScaledContents(True)
        self.listenLbl.setObjectName("listenLbl")
        
        
        self.loadingLbl = QtWidgets.QLabel(self.Levi)
        self.loadingLbl.setGeometry(QtCore.QRect(320, 100, 270, 200))
        self.loadingLbl.setStyleSheet("background-color: transparent;")
        self.loadingLbl.setText("")
        self.loadingLbl.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Loading_Levi.gif"))
        self.loadingLbl.setScaledContents(True)
        self.loadingLbl.setObjectName("loadingLbl")
        
        
        self.sleepLbl = QtWidgets.QLabel(self.Levi)
        self.sleepLbl.setGeometry(QtCore.QRect(320, 100, 270, 200))
        self.sleepLbl.setStyleSheet("background-color: transparent;")
        self.sleepLbl.setText("")
        self.sleepLbl.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Sleeping_Levi.gif"))
        self.sleepLbl.setScaledContents(True)
        self.sleepLbl.setObjectName("sleepLbl")
        
        
        self.terminalText = QtWidgets.QTextEdit(self.Levi)
        self.terminalText.setGeometry(QtCore.QRect(10, 310, 870, 200))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.terminalText.setFont(font)
        self.terminalText.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(0, 128, 0);\n"
"padding: 8px;")
        self.terminalText.setText("")
        self.terminalText.setObjectName("terminalText")
        
        
        self.inputText = QtWidgets.QLineEdit(self.Levi)
        self.inputText.setGeometry(QtCore.QRect(10, 520, 740, 50))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.inputText.setFont(font)
        self.inputText.setStyleSheet("background-color: transparent;\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(0, 128, 0);\n"
"padding: 8px;")
        self.inputText.setMaxLength(50000)
        self.inputText.setFrame(True)
        self.inputText.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.inputText.setClearButtonEnabled(True)
        self.inputText.setObjectName("inputText")
        
        
        self.enterButton = QtWidgets.QPushButton(self.Levi)
        self.enterButton.setGeometry(QtCore.QRect(755, 514, 130, 60))
        self.enterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterButton.setStyleSheet("background-color: transparent;\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Enter_btn.png);")
        self.enterButton.setText("")
        self.enterButton.setObjectName("enterButton")
        
        
        self.exitButton = QtWidgets.QPushButton(self.Levi)
        self.exitButton.setGeometry(QtCore.QRect(754, 250, 130, 60))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("background-color: transparent;\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Exit_btn.png);")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        

        self.leviLogo.raise_()
        self.listenLbl.raise_()
        self.loadingLbl.raise_()
        self.speakLbl.raise_()
        self.sleepLbl.raise_()
        self.terminalText.raise_()
        self.inputText.raise_()
        self.enterButton.raise_()
        self.exitButton.raise_()

        
        MainWindow.setCentralWidget(self.Levi)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Levi - A Peresonal AI Assistant"))
        self.terminalText.setPlaceholderText(_translate("MainWindow", "Terminal output here.."))
        self.inputText.setPlaceholderText(_translate("MainWindow", "Enter input here.."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
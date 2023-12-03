
# Importing required packages or libraries:
from PyQt5 import QtCore, QtGui, QtWidgets

# Python class corresponding to the MAIN [Starting point of the system] window GUI:
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Python code corresponding to MainWindow in GUI:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 576)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/LEVI_AI_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        # Python code corresponding to CentralWidget in MainWindow in GUI:
        self.Levi = QtWidgets.QWidget(MainWindow)
        self.Levi.setObjectName("Levi")
        
        # Python code corresponding to Logo of the system in GUI:
        self.leviLogo = QtWidgets.QLabel(self.Levi)
        self.leviLogo.setGeometry(QtCore.QRect(244, -15, 400, 120))
        self.leviLogo.setStyleSheet("background-color: transparent;")
        self.leviLogo.setText("")
        self.leviLogo.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/LEVI_AI_logo-removebg-preview.png"))
        self.leviLogo.setScaledContents(True)
        self.leviLogo.setObjectName("leviLogo")
        
        # Python code corresponding to Main Widget in GUI [which is at the centre]:
        self.mainGUI = QtWidgets.QLabel(self.Levi)
        self.mainGUI.setGeometry(QtCore.QRect(74, 92, 750, 400))
        self.mainGUI.setStyleSheet("background-color: transparent;")
        self.mainGUI.setText("")
        self.mainGUI.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Hero_Template.gif"))
        self.mainGUI.setScaledContents(True)
        self.mainGUI.setObjectName("mainGUI")
        
        # Python code corresponding to Start button in MainWindow in GUI:
        self.startButton = QtWidgets.QPushButton(self.Levi)
        self.startButton.setGeometry(QtCore.QRect(73, 496, 180, 80))
        self.startButton.setStyleSheet("border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Start_btn.png);\n"
"background-color: transparent;")
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")
        
        # Python code corresponding to Login button in MainWindow in GUI:
        self.loginButton = QtWidgets.QPushButton(self.Levi)
        self.loginButton.setGeometry(QtCore.QRect(365, 496, 180, 80))
        self.loginButton.setStyleSheet("border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Login_btn.png);\n"
"background-color: transparent;")
        self.loginButton.setText("")
        self.loginButton.setObjectName("loginButton")
        
        # Python code corresponding to Exit button in MainWindow in GUI:
        self.exitButton = QtWidgets.QPushButton(self.Levi)
        self.exitButton.setGeometry(QtCore.QRect(647, 496, 180, 80))
        self.exitButton.setStyleSheet("border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Exit_btn.png);\n"
"background-color: transparent;")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        
        # Python code for setting Levi as the CENTRAL WIDGET in our MAIN WINDOW:
        MainWindow.setCentralWidget(self.Levi)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Levi"))

# Main code:
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
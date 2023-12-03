# Importing required packages or libraries:
from PyQt5 import QtCore, QtGui, QtWidgets


# Python class corresponding to the facerecognition window GUI:
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Python code corresponding to MainWindow in GUI:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 576)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/LEVI_AI_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        # Python code corresponding to CentralWidget in MainWindow in GUI:
        self.Levi = QtWidgets.QWidget(MainWindow)
        self.Levi.setObjectName("Levi")
        
        # Python code corresponding to right-hand side background of Iron Man character in GUI:
        self.ironManBack = QtWidgets.QLabel(self.Levi)
        self.ironManBack.setGeometry(QtCore.QRect(-30, 0, 920, 580))
        self.ironManBack.setStyleSheet("background-color: transparent;")
        self.ironManBack.setText("")
        self.ironManBack.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/B.G/Iron_Template_2.jpg"))
        self.ironManBack.setScaledContents(True)
        self.ironManBack.setObjectName("ironManBack")
        
        # Python code corresponding to Logo of the system in GUI:
        self.leviLogo = QtWidgets.QLabel(self.Levi)
        self.leviLogo.setGeometry(QtCore.QRect(27, -2, 460, 120))
        self.leviLogo.setStyleSheet("background-color: transparent;")
        self.leviLogo.setText("")
        self.leviLogo.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/LEVI_AI_logo-removebg-preview.png"))
        self.leviLogo.setObjectName("leviLogo")
        
        # Python code corresponding to window where Facerecognition will happen, in GUI:
        self.videoBack = QtWidgets.QLabel(self.Levi)
        self.videoBack.setGeometry(QtCore.QRect(7, 126, 530, 360))
        self.videoBack.setStyleSheet("border: 1px solid #ffffff;\n"
"background-color: transparent;")
        self.videoBack.setText("")
        self.videoBack.setScaledContents(True)
        self.videoBack.setObjectName("videoBack")
        
        # Python code corresponding to Login button in MainWindow in GUI:
        self.loginButton = QtWidgets.QPushButton(self.Levi)
        self.loginButton.setGeometry(QtCore.QRect(80, 500, 150, 70))
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setStyleSheet("border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Login_btn.png);\n"
"background-color: transparent;")
        self.loginButton.setText("")
        self.loginButton.setObjectName("loginButton")
        
        # Python code corresponding to Exit button in MainWindow in GUI:
        self.exitButton = QtWidgets.QPushButton(self.Levi)
        self.exitButton.setGeometry(QtCore.QRect(300, 500, 150, 70))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Levi - FaceRecognition"))

# Main code:
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
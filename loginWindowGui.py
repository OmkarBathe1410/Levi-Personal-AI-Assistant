# Importing required packages or libraries:
from PyQt5 import QtCore, QtGui, QtWidgets

# Python class corresponding to the Login Main window GUI:
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Python code corresponding to MainWindow in GUI:
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 576)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/LEVI_AI_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background: rgb(0, 0, 0);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        
        # Python code corresponding to CentralWidget in MainWindow in GUI:
        self.Levi = QtWidgets.QWidget(MainWindow)
        self.Levi.setObjectName("Levi")
        
        # Python code corresponding to Logo of the system in GUI:
        self.leviLogo = QtWidgets.QLabel(self.Levi)
        self.leviLogo.setGeometry(QtCore.QRect(280, -10, 330, 100))
        self.leviLogo.setStyleSheet("background: transparent;\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/LEVI_AI_logo-removebg-preview.png)")
        self.leviLogo.setText("")
        self.leviLogo.setObjectName("leviLogo")
        
        # Python code corresponding to a FRAME, inside which everything is displayed in GUI:
        self.frame = QtWidgets.QLabel(self.Levi)
        self.frame.setGeometry(QtCore.QRect(50, 90, 790, 470))
        self.frame.setStyleSheet("background: transparent;\n"
"border: 3px solid #fff;\n"
"border-radius: 15px;")
        self.frame.setText("")
        self.frame.setObjectName("frame")
        
        # Python code corresponding to RETRY button in Login MainWindow in GUI:
        self.retryButton = QtWidgets.QPushButton(self.Levi)
        self.retryButton.setGeometry(QtCore.QRect(103, 480, 160, 70))
        self.retryButton.setAutoFillBackground(False)
        self.retryButton.setStyleSheet("background: transparent;\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Retry_btn.png)")
        self.retryButton.setText("")
        self.retryButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retryButton.setObjectName("retryButton")
        
        # Python code corresponding to BACK button in Login MainWindow in GUI:
        self.backButton = QtWidgets.QPushButton(self.Levi)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setGeometry(QtCore.QRect(370, 480, 160, 70))
        self.backButton.setAutoFillBackground(False)
        self.backButton.setStyleSheet("background: transparent;\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Back_btn.png)")
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        
        # Python code corresponding to EXIT button in Login MainWindow in GUI:
        self.exitButton = QtWidgets.QPushButton(self.Levi)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setGeometry(QtCore.QRect(630, 480, 160, 70))
        self.exitButton.setAutoFillBackground(False)
        self.exitButton.setStyleSheet("background: transparent;\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Exit_btn.png)")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        
        # Python code corresponding to "New User?" label in Login MainWindow in GUI:
        self.newRegisterLbl = QtWidgets.QLabel(self.Levi)
        self.newRegisterLbl.setGeometry(QtCore.QRect(410, 380, 101, 50))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newRegisterLbl.setFont(font)
        self.newRegisterLbl.setStyleSheet("background: transparent;\n"
"color: #fff;")
        self.newRegisterLbl.setObjectName("newRegisterLbl")
        
        # Python code corresponding to "Directing to REGISRATION WINDOW" button in Login MainWindow in GUI:
        self.newRegisterButton = QtWidgets.QPushButton(self.Levi)
        self.newRegisterButton.setGeometry(QtCore.QRect(352, 400, 200, 70))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newRegisterButton.setFont(font)
        self.newRegisterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newRegisterButton.setAutoFillBackground(False)
        self.newRegisterButton.setStyleSheet("background: transparent;\n"
"color: rgb(55, 252, 255);")
        self.newRegisterButton.setObjectName("newRegisterButton")
        
        # Python code corresponding to "LOGIN" heading in Login MainWindow in GUI:
        self.loginLbl = QtWidgets.QLabel(self.Levi)
        self.loginLbl.setGeometry(QtCore.QRect(410, 100, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.loginLbl.setFont(font)
        self.loginLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginLbl.setStyleSheet("backgorund-color: transparent;\n"
"color: #fff;\n"
"text-align: center;")
        self.loginLbl.setObjectName("loginLbl")
        
        # Python code corresponding to "REGISTER" heading in Registration MainWindow in GUI:
        self.registerLbl = QtWidgets.QLabel(self.Levi)
        self.registerLbl.setGeometry(QtCore.QRect(390, 100, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.registerLbl.setFont(font)
        self.registerLbl.setStyleSheet("color: #fff;\n"
"backgorund-color: transparent;\n"
"")
        self.registerLbl.setObjectName("registerLbl")
        
        # Python code corresponding to REGISTER button in Registration MainWindow in GUI:
        self.registerButton = QtWidgets.QPushButton(self.Levi)
        self.registerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerButton.setGeometry(QtCore.QRect(370, 320, 160, 70))
        self.registerButton.setAutoFillBackground(False)
        self.registerButton.setStyleSheet("background: transparent;\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Register_btn.png)")
        self.registerButton.setText("")
        self.registerButton.setObjectName("registerButton")
        
        # Python code corresponding to BACK button in Registration MainWindow in GUI:
        self.backButton_2 = QtWidgets.QPushButton(self.Levi)
        self.backButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton_2.setGeometry(QtCore.QRect(100, 480, 160, 70))
        self.backButton_2.setAutoFillBackground(False)
        self.backButton_2.setStyleSheet("background: transparent;\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Back_btn.png)")
        self.backButton_2.setText("")
        self.backButton_2.setObjectName("backButton_2")
        
        # Python code corresponding to Username input in both [Register and Login] MainWindow in GUI:
        self.usernameEntry = QtWidgets.QLineEdit(self.Levi)
        self.usernameEntry.setGeometry(QtCore.QRect(110, 160, 660, 60))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.usernameEntry.setFont(font)
        self.usernameEntry.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 3px solid #ffffff;\n"
"border-radius: 12px;\n"
"padding-left: 5px;")
        self.usernameEntry.setFrame(False)
        self.usernameEntry.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.usernameEntry.setClearButtonEnabled(True)
        self.usernameEntry.setObjectName("usernameEntry")
        
        # Python code corresponding to Password input in both [Register and Login] MainWindow in GUI:
        self.passwordEntry = QtWidgets.QLineEdit(self.Levi)
        self.passwordEntry.setGeometry(QtCore.QRect(110, 250, 660, 60))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.passwordEntry.setFont(font)
        self.passwordEntry.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 3px solid #ffffff;\n"
"border-radius: 12px;\n"
"padding-left: 5px;")
        self.passwordEntry.setFrame(False)
        self.passwordEntry.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.passwordEntry.setClearButtonEnabled(True)
        self.passwordEntry.setObjectName("passwordEntry")
        
        # Python code corresponding to LOGIN button in Login MainWindow in GUI:
        self.loginButton = QtWidgets.QPushButton(self.Levi)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setGeometry(QtCore.QRect(370, 320, 160, 70))
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet("background: transparent;\n"
"border-image: url(F:/Ava - Personal AI Assistant/G.U.I Material/Buttons/Login_btn.png)")
        self.loginButton.setText("")
        self.loginButton.setObjectName("loginButton")
        
        # Python code corresponding to ILLEGAL AUTHORIZATION label in both [Register and Login] MainWindow in GUI:
        self.illegalEntry = QtWidgets.QLabel(self.Levi)
        self.illegalEntry.setEnabled(True)
        self.illegalEntry.setGeometry(QtCore.QRect(110, 160, 670, 300))
        self.illegalEntry.setStyleSheet("background: transparent;")
        self.illegalEntry.setText("")
        self.illegalEntry.setPixmap(QtGui.QPixmap("F:/Ava - Personal AI Assistant/G.U.I Material/B.G/Invalid_Credentials_btn.png"))
        self.illegalEntry.setScaledContents(True)
        self.illegalEntry.setObjectName("illegalEntry")

        # Python code corresponding to "Registration Successful" in Register MainWindow in GUI:
        self.registrationSuccessful = QtWidgets.QPushButton(self.Levi)
        self.registrationSuccessful.setGeometry(QtCore.QRect(350, 400, 220, 70))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.registrationSuccessful.setFont(font)
        self.registrationSuccessful.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.registrationSuccessful.setAutoFillBackground(False)
        self.registrationSuccessful.setStyleSheet("background: transparent;\n"
"color: rgb(55, 252, 255);")
        self.registrationSuccessful.setObjectName("registrationSuccessful")
        
        # Python code for setting Levi as the CENTRAL WIDGET in our MAIN WINDOW:
        MainWindow.setCentralWidget(self.Levi)

        # Python code for raising all the WIDGETS in our MAIN WINDOW [which will be manipulated as user interacts with the GUI]:
        self.loginLbl.raise_()
        self.registerLbl.raise_()
        self.usernameEntry.raise_()
        self.passwordEntry.raise_()
        self.loginButton.raise_()
        self.registerButton.raise_()
        self.newRegisterButton.raise_()
        self.registrationSuccessful.raise_()
        self.retryButton.raise_()
        self.backButton.raise_()
        self.backButton_2.raise_()
        self.exitButton.raise_()
        self.illegalEntry.raise_()

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Python code for setting neccessary things for the reguired elements in the GUI [both Registration and Login]:        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Levi - Login"))
        self.newRegisterLbl.setText(_translate("MainWindow", "New User?"))
        self.newRegisterButton.setText(_translate("MainWindow", "Click here to register"))
        self.loginLbl.setText(_translate("MainWindow", "LOGIN"))
        self.registerLbl.setText(_translate("MainWindow", "REGISTER"))
        self.usernameEntry.setPlaceholderText(_translate("MainWindow", "Enter username..."))
        self.passwordEntry.setPlaceholderText(_translate("MainWindow", "Enter password..."))
        self.registrationSuccessful.setText(_translate("MainWindow", "Registration Successful"))

# Main code:
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
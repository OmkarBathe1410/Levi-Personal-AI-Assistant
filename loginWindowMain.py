# Importing necessary modules:
from subprocess import call
import sys
import bcrypt
from PyQt5.QtWidgets import QWidget, QLineEdit, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import mysql.connector as myConn

# Importing the user interface class from loginWindowGui module:
from loginWindowGui import Ui_MainWindow

# Defining the loginWindow class that inherits from QMainWindow:
class loginWindow(QMainWindow):
    def __init__(self):
        super(loginWindow, self).__init__()
        print("Setting Up GUI")

        # Creating an instance of the Ui_MainWindow class to set up the UI:
        self.loginUI = Ui_MainWindow()
        self.loginUI.setupUi(self)

         # Establishing a connection to the MySQL database:
        self.db = myConn.connect(
            host="localhost",
            user="root",
            password="OmkarBathe@1410",
            database="leviAI"
        )

        # Hiding various UI elements initially:
        self.loginUI.illegalEntry.hide()
        self.loginUI.registerLbl.hide()
        self.loginUI.backButton_2.hide()
        self.loginUI.registerButton.hide()
        self.loginUI.registrationSuccessful.hide()

        # Setting password entry to display dots for privacy:
        self.loginUI.passwordEntry.setEchoMode(QLineEdit.Password)

        # Creating a QMovie instance for the illegalEntry animation:
        self.loginUI.illegalEntryMovie = QtGui.QMovie("F:/Ava - Personal AI Assistant/G.U.I Material/B.G/Invalid_Credentials_btn.png")
        self.loginUI.illegalEntry.setMovie(self.loginUI.illegalEntryMovie)

        # Connecting UI elements to corresponding functions/methods:
        self.loginUI.exitButton.clicked.connect(self.close)
        self.loginUI.retryButton.clicked.connect(self.retryButton)
        self.loginUI.loginButton.clicked.connect(self.validateLogin)
        self.loginUI.backButton.clicked.connect(self.backToMainPage)
        self.loginUI.newRegisterButton.clicked.connect(self.register_user)
        self.loginUI.registerButton.clicked.connect(self.registerNewUser)
        self.loginUI.backButton_2.clicked.connect(self.backToLoginPage)


    def retryButton(self):
        # Clearing the username and password entries:
        self.loginUI.usernameEntry.clear()    
        self.loginUI.passwordEntry.clear()
        # Stopping the illegalEntry movie:    
        self.stopMovie()


    def validateLogin(self):
        # Retrieving username and password from the UI:
        username = self.loginUI.usernameEntry.text()
        password = self.loginUI.passwordEntry.text()
        # Creating a cursor for database operations:
        cursor = self.db.cursor()

        # Retrieve the hashed password from the database
        cursor.execute('SELECT upass FROM leviusers WHERE uname = %s', (username,))
        hashed_password = cursor.fetchone()

        if hashed_password and bcrypt.checkpw(password.encode('utf-8'), hashed_password[0].encode('utf-8')):
            # Passwords match, login successful
            print("Login Successful")
            self.connectToLeviMain()
        else:
            # Playing the illegalEntry movie for incorrect credentials:
            self.playMovie()              


    def playMovie(self):
        # Showing and starting the illegalEntry movie:
        self.loginUI.illegalEntry.show()
        self.loginUI.illegalEntryMovie.start()

    def stopMovie(self):
        # Hiding and stopping the illegalEntry movie:
        self.loginUI.illegalEntry.hide()
        self.loginUI.illegalEntryMovie.stop()

    def backToMainPage(self):
        # Closing the current window and calling the main.py script:
        self.close()
        call(["python", "main.py"])  

    def backToLoginPage(self):
        # Closing the current window and calling the loginWindowMain.py script:
        self.close()
        call(["python", "loginWindowMain.py"])   

    def register_user(self):
        # Clearing username and password entries, and configuring UI elements for registration:
        self.loginUI.usernameEntry.clear()    
        self.loginUI.passwordEntry.clear()         
        self.loginUI.backButton.hide()
        self.loginUI.newRegisterLbl.hide()
        self.loginUI.loginLbl.hide()
        self.loginUI.loginButton.hide()
        self.loginUI.backButton_2.show()
        self.loginUI.registerButton.show()
        self.loginUI.registerLbl.show()
        self.loginUI.retryButton.hide()
        self.loginUI.newRegisterButton.hide()

    def registerNewUser(self):
        # Hiding UI elements and inserting new user into the database:
        self.loginUI.registerButton.hide()
        self.loginUI.newRegisterLbl.hide()
        loginid = self.loginUI.usernameEntry.text()
        password = self.loginUI.passwordEntry.text()

        # Hash the password before storing it in the database
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO leviusers (uname, upass) VALUES (%s, %s)', (loginid, hashed_password))
        self.db.commit()
        
        # Showing registration success message:
        self.loginUI.registrationSuccessful.show()

    def connectToLeviMain(self):
        # Closing the current window and calling the main.py script:
        self.close()
        call(["python", "leviMain.py"])            
                

# Main code:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = loginWindow()
    ui.show()
    sys.exit(app.exec_()) 
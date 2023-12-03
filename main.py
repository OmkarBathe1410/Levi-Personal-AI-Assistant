from subprocess import call
import sys
import typing
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from faceRecog import faceRecog

from mainGUIFILE import Ui_MainWindow

class mainFile(QMainWindow):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Setting Up GUI")
        self.firstUI = Ui_MainWindow()
        self.firstUI.setupUi(self)

        self.firstUI.movie = QtGui.QMovie("F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Hero_Template.gif")
        self.firstUI.mainGUI.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()

        self.firstUI.exitButton.clicked.connect(self.close)
        self.firstUI.startButton.clicked.connect(self.connectToFaceRecognition)
        self.firstUI.loginButton.clicked.connect(self.connectToLogin)

    def connectToFaceRecognition(self):
        self.showFaceRecogWindow = faceRecog()
        ui.close()
        self.showFaceRecogWindow.show()

    def connectToLogin(self):
        self.close()
        call(["python", "loginWindowMain.py"])    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())
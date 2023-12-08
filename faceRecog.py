# Importing required libraries and classes:
import sys
import os.path
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot,QTimer
from PyQt5.QtGui import QImage, QPixmap
import cv2  
import face_recognition
import numpy

from faceRecognitionGui import Ui_MainWindow

# Method for getting the name of the user from the image:
def nameList(nameOfImg):
    if nameOfImg.startswith('Pra', 0):
        return "Prathm"    
    elif nameOfImg.startswith('Omk', 0):
        return "Omkar"

# Class of the faceRecognition module:
class faceRecog(QMainWindow):
    def __init__(self):
        super(faceRecog, self).__init__()
        print("Setting Up GUI")
        self.faceUI = Ui_MainWindow()
        self.faceUI.setupUi(self)

        self.name = None
        self.videoCapture_ = None
        self.name = None
    
        self.faceUI.exitButton.clicked.connect(self.close)
        self.faceUI.loginButton.clicked.connect(self.connectToLogin)
        
        #for camera input:
        self.startVideo()                                                                               


    # for camera input:
    @pyqtSlot()                                                         
    def startVideo(self):                                                                               
        print("Encoding Started")
        
        #for camera input:
        self.capture = cv2.VideoCapture(0)                                                              
        self.timer = QTimer(self)
        path = 'images'
        if not os.path.exists(path):
            os.mkdir(path)

        images = []                 #images for faces 
        self.classNames = []        #names of images   
        self.encodeList = []        #encodings of faces
        photoList = os.listdir(path)

        for cl in photoList:
            currentImage = cv2.imread(f'{path}/{cl}')
            images.append(currentImage)
            self.classNames.append(os.path.splitext(cl)[0])

        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img,boxes)[0]
            self.encodeList.append(encodes_cur_frame)
        
        print("Faces Encoded Successfully")

        self.timer.timeout.connect(self.updateFrames)
        self.timer.start(10) 

    # For updating the frames to be recognized:
    def updateFrames(self):
        ret, self.image = self.capture.read()
        self.displayImage(self.image , self.encodeList , self.classNames , 1)

    # Method for displaying the image:
    def displayImage(self, image, encodeList, className, window=1):
        #remove for video input:
        image = cv2.resize(image, (641, 441))                                                           
        try:
            image = self.faceRec(image, encodeList, className)       
        except:
            print("Cannot Show Image")

        #For Simple formatting:
        qformat = QImage.Format_Indexed8             
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:    
                qformat = QImage.Format_RGB888
        #Data ,width, height, bytesPerLine, format:
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)     
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.faceUI.videoBack.setPixmap(QPixmap.fromImage(outImage))
            self.faceUI.videoBack.setScaledContents(True)
            if self.name == "Omkar":
                self.connectToLeviMain()
                self.timer.stop()

    # Method for recognizing the face:
    def faceRec(self, image, encodeList, className):
        faces_cur_frames = face_recognition.face_locations(image)
        encodes_cur_frames = face_recognition.face_encodings(image, faces_cur_frames)

        for encodeFace, faceLoc in zip(encodes_cur_frames, faces_cur_frames):
            match = face_recognition.compare_faces(encodeList, encodeFace ,tolerance=0.50)
            face_dis = face_recognition.face_distance(encodeList,encodeFace)
            self.name = "Unknown"

            #bestMatcIndex = no. of image in folder which is matching.. i.e if it is 2nd image in folder bestMatchIndex = 2:
            bestMatchIndex = numpy.argmin(face_dis)         

            if match[bestMatchIndex]:
                #className[bestMatchIndex] = className[2] it will get name of 2nd image in folder:
                self.name = className[bestMatchIndex]         
                self.name = nameList(self.name)
                y1,x2,y2,x1 = faceLoc      
                #image , point1, point2, color, thickness of rectangle:
                cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)        
                #image, text, point, fontface, fontsize, color, thickness:
                cv2.putText(image,self.name, (x1-6 , y2+20),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),1)    
        return image        

    # Method for redirecting/connecting to the MAIN module of our system:
    def connectToLeviMain(self):
        from subprocess import call
        self.capture.release()     
        self.close()
        call(["python", "leviMain.py"])

    # Method for redirecting/connecting to the Login module of our system:
    def connectToLogin(self):
        from subprocess import call
        self.capture.release()     
        self.close()
        call(["python", "loginWindowMain.py"])      


# Main code:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = faceRecog()
    ui.show()
    sys.exit(app.exec_())
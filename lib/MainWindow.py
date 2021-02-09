import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from SubWindow import SubWindow
from lib.SubWindow import SubWindow
#import lib.swLCD
from lib.swLCD import swLCD
from lib.swSpeaker import swSpeaker
from lib.swCamera import swCamera
from lib.swMIC import swMIC


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()
        layout.addStretch(1)
        label = QLabel("Head Test")
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        self.label = label
        layout.addWidget(label)
        layout.addStretch(1)
        
        #thread set
        #thLCD = threading.Thread(target=swLCD.runLCDdisplay)
        #thLCD.start()
        #thLCD.stop()
        
        #1-CAMERA
        btnCAM = QPushButton("CAMERA")
        btnCAM.clicked.connect(self.onBtnCamClicked)
        layout.addWidget(btnCAM)
        
        #2-MIC_REC
        btnMIC = QPushButton("MIC_REC")
        btnMIC.clicked.connect(self.onBtnMicClicked)
        layout.addWidget(btnMIC)
        
        #3-LCD
        btnLCD = QPushButton("LCD")
        btnLCD.clicked.connect(self.onBtnLcdClicked)
        layout.addWidget(btnLCD)
        
        #4-Speaker
        btnSpeaker = QPushButton("Speaker")
        btnSpeaker.clicked.connect(self.onBtnSpeakerClicked)
        layout.addWidget(btnSpeaker)
     
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    
    
    def onBtnCamClicked(self):
        thCAM = threading.Thread(target=swCamera.run)
        thCAM.start()
    
    def onBtnMicClicked(self):
        #iMIC = swMIC()
        #thMIC = threading.Thread(target=iMIC.run)
        #thMIC.start()
        #thMIC.join()
        
        micTestResult = 0
        iMIC = swMIC()
        iMIC.start()
        micTestResult = iMIC.join()
        print("test result:",str(micTestResult))
        
        #resultMICtest = thMIC.join()
        
        #print('result',str(resultMICtest))
        #if resultMICtest == 1:
        #    self.label.setText = 'mic test ok'
        #elif resultMICtest == 2:
        #    self.label.setText = 'mic test fail'
        
    
    def onBtnLcdClicked(self):
        #swLCD.runLCDdisplay()
        #t = threading.Thread(target=swLCD.runLCDdisplay)
        #t.start()
        thLCD = threading.Thread(target=swLCD.run)
        
        if not thLCD.is_alive():
            thLCD.start()
        else:
            thLCD.kill()
            thLCD.start()
        
    
    def onBtnSpeakerClicked(self):
        speakerTestResult = None
        sout = swSpeaker()
        sout.start()
        speakerTestResult = sout.join()
        print(speakerTestResult)
    
   
    def show(self):
        super().show()
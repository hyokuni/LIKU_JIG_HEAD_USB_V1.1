import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from SubWindow import SubWindow
from lib.SubWindow import SubWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()
        layout.addStretch(1)
        label = QLabel("미지정")
        label.setAlignment(Qt.AlignCenter)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        self.label = label
        btn = QPushButton("값 얻어오기")
        btn.clicked.connect(self.onButtonClicked)
        layout.addWidget(label)
        layout.addWidget(btn)
        layout.addStretch(1)
        
        btn2 = QPushButton("하나 더 추가하기")
        btn2.clicked.connect(self.onBtn2Clicked)
        layout.addWidget(btn2)
        
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    def onButtonClicked(self):
        win = SubWindow()
        r = win.showModal()
        if r:
            text = win.edit.text()
            self.label.setText(text)
            
    def onBtn2Clicked(self):
        win = SubWindow()
        r = win.showModal()
    
    def show(self):
        super().show()
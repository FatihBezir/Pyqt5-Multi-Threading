import threading
from PyQt5 import QtCore, QtWidgets
import sys, time, ctypes
from threading import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(389, 251)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 25)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.progressBar_2 = QtWidgets.QProgressBar(Form)
        self.progressBar_2.setProperty("value", 25)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_2.addWidget(self.progressBar_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.progressBar_3 = QtWidgets.QProgressBar(Form)
        self.progressBar_3.setProperty("value", 25)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_3.addWidget(self.progressBar_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.pushButton_2.setText(_translate("Form", "Start"))
        self.pushButton_3.setText(_translate("Form", "Start"))

        self.pushButton.clicked.connect(lambda:self.Tr("A",self.pushButton,self.progressBar))
        self.pushButton_2.clicked.connect(lambda:self.Tr("B",self.pushButton_2,self.progressBar_2))
        self.pushButton_3.clicked.connect(lambda:self.Tr("C",self.pushButton_3,self.progressBar_3))
    
    def Tr(self,tName,sender,progressBar):
        
        flag = False
        for thread in threading.enumerate(): 
            if(thread.name == tName):
                flag = True
                sender.setText("Start")
                ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, ctypes.py_object(SystemExit))              
                break        
        if(not flag):
            t=Thread(target=self.run,args=(progressBar,))
            t.name = tName
            sender.setText("Stop")
            t.start()

    def run(self,progressBar):     
            i = progressBar.value()
            while(True):         
                time.sleep(0.2)
                progressBar.setValue(i)
                i+=5
                if(i >= 100): i = 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import os


class MainWindow(QtWidgets.QTabWidget):
    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)

        self.setFixedSize(900, 500)


# Tab widget initialization
class TabContent(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)


# Front UI for first task
class FirstTabContentVidget(TabContent):
    def __init__(self):
        TabContent.__init__(self)

        self.okButton = QtWidgets.QPushButton(self)
        self.inputsTextField = QtWidgets.QPlainTextEdit(self)
        self.setInputsLabel = QtWidgets.QLabel(self)
        self.setFileButton = QtWidgets.QPushButton(self)
        self.setFileLabel = QtWidgets.QLabel(self)
        self.showOutputPathLabel = QtWidgets.QLabel(self)
        self.showOutputPathLine = QtWidgets.QLineEdit(self)
        self.openOutputButton = QtWidgets.QPushButton(self)

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.setFileLabel.setGeometry(QtCore.QRect(20, 60, 81, 20))
        self.setFileLabel.setObjectName("setFileLabel")
        self.setFileLabel.setText("Choose file:")

        self.setFileButton.setGeometry(QtCore.QRect(305, 60, 75, 23))
        self.setFileButton.setObjectName("setFileButton")
        self.setFileButton.setText("Find the way")
        self.setFileButton.clicked.connect(self.setFileButtonClicked)

        self.setInputsLabel.setGeometry(QtCore.QRect(20, 120, 131, 16))
        self.setInputsLabel.setObjectName("setInputsLabel")
        self.setInputsLabel.setText("Input data:")

        self.inputsTextField.setGeometry(QtCore.QRect(20, 150, 361, 141))
        self.inputsTextField.setObjectName("inputsTextField")

        self.okButton.setGeometry(QtCore.QRect(305, 310, 75, 23))
        self.okButton.setObjectName("okButton")
        self.okButton.setText("Done")
        
        # if the button pressed, okButtonClicked initialized
        self.okButton.clicked.connect(self.okButtonClicked)

        self.showOutputPathLabel.setGeometry(QtCore.QRect(400, 60, 81, 20))
        self.showOutputPathLabel.setObjectName("showOutputPathLabel")
        self.showOutputPathLabel.setText("Answer:")

        self.showOutputPathLine.setGeometry(QtCore.QRect(400, 90, 361, 20))
        self.showOutputPathLine.setObjectName("showOutputPathLine")

        self.openOutputButton.setGeometry(771, 89, 75, 22)
        self.openOutputButton.setObjectName("openOutputButton")
        self.openOutputButton.setText("Open")
        self.openOutputButton.clicked.connect(self.openOutputButtonClicked)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def setFileButtonClicked(self):
        
        dialog = QtWidgets.QFileDialog(self)
        dialog.setViewMode(QtWidgets.QFileDialog.List)
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        
        if dialog.exec_():
            filePath = dialog.selectedFiles()
    
        self.showOutputPath()

    def okButtonClicked(self):
        inputs = self.inputsTextField.toPlainText()
        self.saveDataToFile(inputs)
        self.showOutputPath()

    def openOutputButtonClicked(self):
        os.startfile('input.txt')

    def saveDataToFile(self, data):
        with open("input.txt", 'w') as new_file:
            new_file.write(data)

    def showOutputPath(self):
        path = "input.txt"
        self.showOutputPathLine.setText(path)


# Front UI for second task
class SecondTabContentVidget(TabContent):
    def __init__(self):
        TabContent.__init__(self)
        

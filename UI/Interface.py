import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import os


class MainWindow(QtWidgets.QTabWidget):
    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)

        # self.resize(900, 500)
        self.setFixedSize(900, 500)


# клас, який робить з рандомного UI віджет, який можна засунути в в вкладку
class TabContent(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)


# фронт першого пункта завдання
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
        self.setFileLabel.setText("Вибрати файл:")

        self.setFileButton.setGeometry(QtCore.QRect(305, 60, 75, 23))
        self.setFileButton.setObjectName("setFileButton")
        self.setFileButton.setText("Задати шлях")
        self.setFileButton.clicked.connect(self.setFileButtonClicked)

        self.setInputsLabel.setGeometry(QtCore.QRect(20, 120, 131, 16))
        self.setInputsLabel.setObjectName("setInputsLabel")
        self.setInputsLabel.setText("Ввести дані з клавіатури:")

        self.inputsTextField.setGeometry(QtCore.QRect(20, 150, 361, 141))
        self.inputsTextField.setObjectName("inputsTextField")

        self.okButton.setGeometry(QtCore.QRect(305, 310, 75, 23))
        self.okButton.setObjectName("okButton")
        self.okButton.setText("Готово")
        # якшо кнопка нажата, визиваєся okButtonClicked
        self.okButton.clicked.connect(self.okButtonClicked)

        self.showOutputPathLabel.setGeometry(QtCore.QRect(400, 60, 81, 20))
        self.showOutputPathLabel.setObjectName("showOutputPathLabel")
        self.showOutputPathLabel.setText("Відповідь тут:")

        self.showOutputPathLine.setGeometry(QtCore.QRect(400, 90, 361, 20))
        self.showOutputPathLine.setObjectName("showOutputPathLine")
        # self.showOutputPathLine.setText("Тут міг бути путь до вашого ответа, но ви його не зробили")

        self.openOutputButton.setGeometry(771, 89, 75, 22)
        self.openOutputButton.setObjectName("openOutputButton")
        self.openOutputButton.setText("Відкрити")
        self.openOutputButton.clicked.connect(self.openOutputButtonClicked)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def setFileButtonClicked(self):
        # ініціалізація діалогового вікна вибора каталогу
        dialog = QtWidgets.QFileDialog(self)
        # режим діалогового вікна, при якому виводиться вся доступна інфа по файлам
        dialog.setViewMode(QtWidgets.QFileDialog.List)
        # режим діалогового вікна, при якому можна вибрати файл з будь яким розширенням
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        # якшо кнопка ОК діалогового вікна, була натиснута, записуем путь в файл
        if dialog.exec_():
            filePath = dialog.selectedFiles()
            # print(filePath)
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
        path = "C:\\Users\\Major\\Desktop\\Progs\\tui2020\\input.txt"
        self.showOutputPathLine.setText(path)


# фронт другого пункта завдання
class SecondTabContentVidget(TabContent):
    def __init__(self):
        TabContent.__init__(self)
        

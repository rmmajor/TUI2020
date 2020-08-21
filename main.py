import sys
from PyQt5 import QtWidgets, QtGui,QtCore
from UI.Interface import MainWindow, FirstTabContentVidget, SecondTabContentVidget

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()

    application.addTab(FirstTabContentVidget(), "Створення імітаційної моделі")
    application.addTab(SecondTabContentVidget(), "пуста хуета")

    application.show()

    sys.exit(app.exec())
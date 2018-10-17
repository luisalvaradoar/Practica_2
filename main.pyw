import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from window import *

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    main_window = Ui_MainWindow()
    main_window.setupUi(window)
    window.show()
    app.exec_()

subprocess.call(["rm",'-rf', "__pycache__"])
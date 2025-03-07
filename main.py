#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from app.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app_icon.ico'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
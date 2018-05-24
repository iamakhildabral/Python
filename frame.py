"""
Lets practice with the Icon object closely
"""

import sys
from PyQt5.QtWidgets import (QApplication,QWidget)
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Home:Welcome to the Billig System:")
w.setWindowIcon(QIcon("WTP.png"))
w.resize(300,300)
w.move(100,100)
w.show()
sys.exit(app.exec_())

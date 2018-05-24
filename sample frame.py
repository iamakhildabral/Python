import sys
from PyQt5.QtWidgets import(QApplication,QWidget,QPushButton,QToolTip)
from PyQt5.QtGui import(QFont,QIcon)
from PyQt5.QtCore import (QCoreApplication)

class Frame1(QWidget,QCoreApplication):
       def __init__(self):
              super().__init__()
              self.ui()

       def ui(self):
              QToolTip.setFont(QFont("Seoge UI",10))
              Btn1 = QPushButton("Close Window",self)
              Btn1.setToolTip("This will close your window :")
              Btn1.clicked.connect(QCoreApplication.instance().quit)
              Btn1.resize(Btn1.sizeHint())
              Btn1.move(20,20)

              self.setGeometry(300,300,50,50)
              self.setWindowTitle("Frame1:")
              self.setWindowIcon(QIcon("C:\\Users\\ADABRAL\\Downloads\\WTP.png"))
              self.show()

if __name__ == "__main__":
       app = QApplication(sys.argv)
       w = Frame1()
       sys.exit(app.exec_())
              

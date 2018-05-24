###########################  Message Box on Close Button ################

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QMessageBox)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import (QIcon,QFont)

class Home(QWidget):

       def __init__(self):
              super().__init__()
              self.initUI()

       def initUI(self):
              self.setGeometry(300,300,100,100)
              self.setWindowTitle("Home Page:")
              self.setWindowIcon(QIcon("C:\\Users\\ADABRAL\\Downloads\\WTP.png"))
              self.show()

       def closeEvent(self,event):
              reply = QMessageBox.question(self,'Message to you Darling'," Really you\
really want to close this window",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

              if reply == QMessageBox.Yes:
                     event.accept()
              else:
                     event.ignore()



if __name__ == "__main__":
       app = QApplication(sys.argv)
       w = Home()
       sys.exit(app.exec_())
       
              
       

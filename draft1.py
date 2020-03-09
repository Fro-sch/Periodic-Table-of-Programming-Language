import sys
from PyQt5.QtWidgets import QWidget,QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):
    
    def __init__(self):
        super().__init__() 
        self.title = "Periodic Table of Programming Language"
        self.x = 30
        self.y = 30
        self.width = 1300
        self.height = 700
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('abstract-119_38574.ico'))
        
        self.textboxlbl = QLabel("Periodic Table of Programming Language", self)
        self.textboxlbl.move(500,50)

        self.button1 = QPushButton("A", self)
        self.button1.setToolTip("Analytical Engine Order Code")
        self.button1.move(50,120)
        self.button1.resize(50,50)

        self.button3 = QPushButton("Ft", self)
        self.button3.setToolTip("Fortran")
        self.button3.move(50,180)
        self.button3.resize(50,50)
  
        self.button7 = QPushButton("Sn", self)
        self.button7.setToolTip("SNOBOL")
        self.button7.move(50,240)
        self.button7.resize(50,50)
  
        self.button13 = QPushButton("Fo", self)
        self.button13.setToolTip("Forth")
        self.button13.move(50,300)
        self.button13.resize(50,50)
       
        self.button22 = QPushButton("Ad", self)
        self.button22.setToolTip("Ada")
        self.button22.move(50,360)
        self.button22.resize(50,50)
       
        self.button32 = QPushButton("Vb", self)
        self.button32.setToolTip("Visual BASIC")
        self.button32.move(50,420)
        self.button32.resize(50,50)

        self.button4 = QPushButton("Ag", self)
        self.button4.setToolTip("ALGOL")
        self.button4.move(110,180)
        self.button4.resize(50,50)
       
        self.button8 = QPushButton("Bs", self)
        self.button8.setToolTip("BASIC")
        self.button8.move(110,240)
        self.button8.resize(50,50)

        self.button14 = QPushButton("Pc", self)
        self.button14.setToolTip("Pascal")
        self.button14.move(110,300)
        self.button14.resize(50,50)

        self.button23 = QPushButton("Cp", self)
        self.button23.setToolTip("C++")
        self.button23.move(110,360)
        self.button23.resize(50,50)

        self.button33 = QPushButton("Dp", self)
        self.button33.setToolTip("Delphi")
        self.button33.move(110,420)
        self.button33.resize(50,50)

        self.button9 = QPushButton("Sm", self)
        self.button9.setToolTip("Simula")
        self.button9.move(170,240)
        self.button9.resize(50,50)

        self.button15 = QPushButton("St", self)
        self.button15.setToolTip("Smalltalk")
        self.button15.move(170,300)
        self.button15.resize(50,50)

        self.button24 = QPushButton("Ef", self)
        self.button24.setToolTip("Eiffel")
        self.button24.move(170,360)
        self.button24.resize(50,50)

        self.button34 = QPushButton("Jv", self)
        self.button34.setToolTip("Java")
        self.button34.move(170,420)
        self.button34.resize(50,50)

        self.button16 = QPushButton("Sq", self)
        self.button16.setToolTip("SQL")
        self.button16.move(230,300)
        self.button16.resize(50,50)


        self.button25 = QPushButton("Oc", self)
        self.button25.setToolTip("Objective C")
        self.button25.move(230,360)
        self.button25.resize(50,50)

        self.button35 = QPushButton("Py", self)
        self.button35.setToolTip("Python")
        self.button35.move(230,420)
        self.button35.resize(50,50)

        self.button17 = QPushButton("Pg", self)
        self.button17.setToolTip("Prolog")
        self.button17.move(290,300)
        self.button17.resize(50,50)

        self.button26 = QPushButton("Ps", self)
        self.button26.setToolTip("PostScript")
        self.button26.move(290,360)
        self.button26.resize(50,50)

        self.button36 = QPushButton("As", self)
        self.button36.setToolTip("AppleScript")
        self.button36.move(290,420)
        self.button36.resize(50,50)

        self.button27 = QPushButton("Tc", self)
        self.button27.setToolTip("Tcl")
        self.button27.move(350,360)
        self.button27.resize(50,50)

        self.button37 = QPushButton("Cf", self)
        self.button37.setToolTip("Coldfusion")
        self.button37.move(350,420)
        self.button37.resize(50,50)
        
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

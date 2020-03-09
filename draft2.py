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

        self.button42 = QPushButton("Cs", self)
        self.button42.setToolTip("C#")
        self.button42.move(170,490)
        self.button42.resize(50,50)

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

        self.button43 = QPushButton("Sl", self)
        self.button43.setToolTip("Scala")
        self.button43.move(230,490)
        self.button43.resize(50,50)

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

        self.button44 = QPushButton("Gv", self)
        self.button44.setToolTip("Groovy")
        self.button44.move(290,490)
        self.button44.resize(50,50)

        self.button27 = QPushButton("Tc", self)
        self.button27.setToolTip("Tcl")
        self.button27.move(350,360)
        self.button27.resize(50,50)

        self.button37 = QPushButton("Cf", self)
        self.button37.setToolTip("Coldfusion")
        self.button37.move(350,420)
        self.button37.resize(50,50)

        self.button45 = QPushButton("Rb", self)
        self.button45.setToolTip("Ruby")
        self.button45.move(350,490)
        self.button45.resize(50,50)

        self.button18 = QPushButton("C", self)
        self.button18.setToolTip("C")
        self.button18.move(410,300)
        self.button18.resize(50,50)

        self.button28 = QPushButton("Ht", self)
        self.button28.setToolTip("HyperTalk")
        self.button28.move(410,360)
        self.button28.resize(50,50)

        self.button38 = QPushButton("Js", self)
        self.button38.setToolTip("JavasScript")
        self.button38.move(410,420)
        self.button38.resize(50,50)

        self.button46 = QPushButton("G", self)
        self.button46.setToolTip("GO")
        self.button46.move(410,490)
        self.button46.resize(50,50)

        self.button10 = QPushButton("P", self)
        self.button10.setToolTip("PL/1")
        self.button10.move(470,240)
        self.button10.resize(50,50)

        self.button19 = QPushButton("M", self)
        self.button19.setToolTip("Modula")
        self.button19.move(470,300)
        self.button19.resize(50,50)

        self.button46 = QPushButton("Pl", self)
        self.button46.setToolTip("Perl")
        self.button46.move(470,360)
        self.button46.resize(50,50)

        self.button29 = QPushButton("Pp", self)
        self.button29.setToolTip("PHP")
        self.button29.move(470,420)
        self.button29.resize(50,50)

        self.button47 = QPushButton("Cj", self)
        self.button47.setToolTip("Clojure")
        self.button47.move(470,490)
        self.button47.resize(50,50)

        self.button5 = QPushButton("Cb", self)
        self.button5.setToolTip("COBOL")
        self.button5.move(530,180)
        self.button5.resize(50,50)

        self.button11 = QPushButton("B", self)
        self.button11.setToolTip("B")
        self.button11.move(530,240)
        self.button11.resize(50,50)

        self.button20 = QPushButton("Ml", self)
        self.button20.setToolTip("ML")
        self.button20.move(530,300)
        self.button20.resize(50,50)

        self.button30 = QPushButton("Cl", self)
        self.button30.setToolTip("Common LISP")
        self.button30.move(530,360)
        self.button30.resize(50,50)

        self.button40 = QPushButton("Fs", self)
        self.button40.setToolTip("F#")
        self.button40.move(530,420)
        self.button40.resize(50,50)
        
        self.button2 = QPushButton("E", self)
        self.button2.setToolTip("ENIAC Short Code")
        self.button2.move(590,120)
        self.button2.resize(50,50)

        self.button6 = QPushButton("L", self)
        self.button6.setToolTip("LISP")
        self.button6.move(590,180)
        self.button6.resize(50,50)

        self.button12 = QPushButton("Lg", self)
        self.button12.setToolTip("LOGO")
        self.button12.move(590,240)
        self.button12.resize(50,50)

        self.button21 = QPushButton("Sc", self)
        self.button21.setToolTip("Scheme")
        self.button21.move(590,300)
        self.button21.resize(50,50)

        self.button31 = QPushButton("Er", self)
        self.button31.setToolTip("Erlang")
        self.button31.move(590,360)
        self.button31.resize(50,50)

        self.button41 = QPushButton("Hk", self)
        self.button41.setToolTip("Haskel")
        self.button41.move(590,420)
        self.button41.resize(50,50)
        
        # Mechanical
        self.button01 = QPushButton(self)
        self.button01.move(50,560)
        self.button01.resize(20,20)
        self.textboxlbl01 = QLabel("Mechanical",self)
        self.textboxlbl01.move(80,562)

        # Imperative
        self.button02 = QPushButton(self)
        self.button02.move(50,600)
        self.button02.resize(20,20)     
        self.textboxlbl02 = QLabel("Imperative",self)
        self.textboxlbl02.move(80,602)

        # Object Oriented
        self.button03 = QPushButton(self)
        self.button03.move(50,640)
        self.button03.resize(20,20)
        self.textboxlbl03 = QLabel("Object Oriented",self)
        self.textboxlbl03.move(80,642)

        # Scripting
        self.button04 = QPushButton(self)
        self.button04.move(270,560)
        self.button04.resize(20,20)
        self.textboxlbl04 = QLabel("Scripting",self)
        self.textboxlbl04.move(300,562)

        # Declarative
        self.button05 = QPushButton(self)
        self.button05.move(270,600)
        self.button05.resize(20,20)
        self.textboxlbl05 = QLabel("Declarative",self)
        self.textboxlbl05.move(300,602)

        # Functional
        self.button06 = QPushButton(self)
        self.button06.move(270,640)
        self.button06.resize(20,20)
        self.textboxlbl06 = QLabel("Functional",self)
        self.textboxlbl06.move(300,642)

        # Dynamic
        self.button07 = QPushButton(self)
        self.button07.move(490,560)
        self.button07.resize(20,20)
        self.textboxlbl07 = QLabel("Dynamic",self)
        self.textboxlbl07.move(520,562)

        # Concurrent
        self.button08 = QPushButton(self)
        self.button08.move(490,600)
        self.button08.resize(20,20)
        self.textboxlbl08 = QLabel("Concurrent",self)
        self.textboxlbl08.move(520,602)

        # Multi-Paradigm
        self.button09 = QPushButton(self)
        self.button09.move(490,640)
        self.button09.resize(20,20)
        self.textboxlbl09 = QLabel("Multi-Paradigm",self)
        self.textboxlbl09.move(520,642)

        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

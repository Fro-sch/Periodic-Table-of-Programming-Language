import sys
from sqlitedict import *
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, \
                            QTabWidget, QGridLayout, QVBoxLayout, QDialog, QComboBox, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Periodic Table of Programming"
        self.x = 30
        self.y = 30
        self.width = 1300
        self.height = 700
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('program.ico'))

# Title
        self.textboxlbl = QLabel("THE PERIODIC TABLE OF PROGRAMMING LANGUAGES",self)
        self.textboxlbl.move(400,10)
        self.textboxlbl.setFont(QtGui.QFont('Impact', 18))
        self.textboxlbl1 = QLabel("Visualization of the evolution of popular programming languages",self)
        self.textboxlbl1.move(465,40)
        self.textboxlbl1.setFont(QtGui.QFont('Perpetua', 11))
# Periodic Table Buttons
        self.button1 = QPushButton("A", self)
        self.button1.setFont(QtGui.QFont('Impact', 14))
        self.button1.setToolTip("Analytical Engine Order Code")
        self.button1.move(50,120)
        self.button1.resize(50,50)
        self.button1.setStyleSheet("background-color: #CD5C5C; border-radius: 5px")

        self.button3 = QPushButton("Ft", self)
        self.button3.setFont(QtGui.QFont('Impact', 14))
        self.button3.setToolTip("Fortran")
        self.button3.move(50,180)
        self.button3.resize(50,50)
        self.button3.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button7 = QPushButton("Sn", self)
        self.button7.setFont(QtGui.QFont('Impact', 14))
        self.button7.setToolTip("SNOBOL")
        self.button7.move(50,240)
        self.button7.resize(50,50)
        self.button7.setStyleSheet("background-color: #F0E68C; border-radius: 5px")
 
        self.button13 = QPushButton("Fo", self)
        self.button13.setFont(QtGui.QFont('Impact', 14))
        self.button13.setToolTip("Forth")
        self.button13.move(50,300)
        self.button13.resize(50,50)
        self.button13.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button22 = QPushButton("Ad", self)
        self.button22.setFont(QtGui.QFont('Impact', 14))
        self.button22.setToolTip("Ada")
        self.button22.move(50,360)
        self.button22.resize(50,50)
        self.button22.setStyleSheet("background-color: #A9A9A9; border-radius: 5px")

        self.button32 = QPushButton("Vb", self)
        self.button32.setFont(QtGui.QFont('Impact', 14))
        self.button32.setToolTip("Visual BASIC")
        self.button32.move(50,420)
        self.button32.resize(50,50)
        self.button32.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button4 = QPushButton("Ag", self)
        self.button4.setFont(QtGui.QFont('Impact', 14))
        self.button4.setToolTip("ALGOL")
        self.button4.move(110,180)
        self.button4.resize(50,50)
        self.button4.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button8 = QPushButton("Bs", self)
        self.button8.setFont(QtGui.QFont('Impact', 14))
        self.button8.setToolTip("BASIC")
        self.button8.move(110,240)
        self.button8.resize(50,50)
        self.button8.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button14 = QPushButton("Pc", self)
        self.button14.setFont(QtGui.QFont('Impact', 14))
        self.button14.setToolTip("Pascal")
        self.button14.move(110,300)
        self.button14.resize(50,50)
        self.button14.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button23 = QPushButton("Cp", self)
        self.button23.setFont(QtGui.QFont('Impact', 14))
        self.button23.setToolTip("C++")
        self.button23.move(110,360)
        self.button23.resize(50,50)
        self.button23.setStyleSheet("background-color: #FFA07A; border-radius: 5px")

        self.button33 = QPushButton("Dp", self)
        self.button33.setFont(QtGui.QFont('Impact', 14))
        self.button33.setToolTip("Delphi")
        self.button33.move(110,420)
        self.button33.resize(50,50)
        self.button33.setStyleSheet("background-color: #FFA07A; border-radius: 5px")

        self.button9 = QPushButton("Sm", self)
        self.button9.setFont(QtGui.QFont('Impact', 14))
        self.button9.setToolTip("Simula")
        self.button9.move(170,240)
        self.button9.resize(50,50)
        self.button9.setStyleSheet("background-color: #FFA07A; border-radius: 5px")

        self.button15 = QPushButton("St", self)
        self.button15.setFont(QtGui.QFont('Impact', 14))
        self.button15.setToolTip("Smalltalk")
        self.button15.move(170,300)
        self.button15.resize(50,50)
        self.button15.setStyleSheet("background-color: #FFA07A; border-radius: 5px")

        self.button24 = QPushButton("Ef", self)
        self.button24.setFont(QtGui.QFont('Impact', 14))
        self.button24.setToolTip("Eiffel")
        self.button24.move(170,360)
        self.button24.resize(50,50)
        self.button24.setStyleSheet("background-color: #FFA07A; border-radius: 5px")

        self.button34 = QPushButton("Jv", self)
        self.button34.setFont(QtGui.QFont('Impact', 14))
        self.button34.setToolTip("Java")
        self.button34.move(170,420)
        self.button34.resize(50,50)
        self.button34.setStyleSheet("background-color: #FFA07A; border-radius: 5px")

        self.button42 = QPushButton("Cs", self)
        self.button42.setFont(QtGui.QFont('Impact', 14))
        self.button42.setToolTip("C#")
        self.button42.move(170,490)
        self.button42.resize(50,50)
        self.button42.setStyleSheet("background-color: #40E0D0; border-radius: 5px")
    
        self.button16 = QPushButton("Sq", self)
        self.button16.setFont(QtGui.QFont('Impact', 14))
        self.button16.setToolTip("SQL")
        self.button16.move(230,300)
        self.button16.resize(50,50)
        self.button16.setStyleSheet("background-color: #FF00FF; border-radius: 5px")

        self.button25 = QPushButton("Oc", self)
        self.button25.setFont(QtGui.QFont('Impact', 14))
        self.button25.setToolTip("Objective C")
        self.button25.move(230,360)
        self.button25.resize(50,50)
        self.button25.setStyleSheet("background-color: #FFA07A; border-radius: 5px")

        self.button35 = QPushButton("Py", self)
        self.button35.setFont(QtGui.QFont('Impact', 14))
        self.button35.setToolTip("Python")
        self.button35.move(230,420)
        self.button35.resize(50,50)
        self.button35.setStyleSheet("background-color: #40E0D0; border-radius: 5px")

        self.button43 = QPushButton("Sl", self)
        self.button43.setFont(QtGui.QFont('Impact', 14))
        self.button43.setToolTip("Scala")
        self.button43.move(230,490)
        self.button43.resize(50,50)
        self.button43.setStyleSheet("background-color: #40E0D0; border-radius: 5px")

        self.button17 = QPushButton("Pg", self)
        self.button17.setFont(QtGui.QFont('Impact', 14))
        self.button17.setToolTip("Prolog")
        self.button17.move(290,300)
        self.button17.resize(50,50)
        self.button17.setStyleSheet("background-color: #FF00FF; border-radius: 5px")

        self.button26 = QPushButton("Ps", self)
        self.button26.setFont(QtGui.QFont('Impact', 14))
        self.button26.setToolTip("PostScript")
        self.button26.move(290,360)
        self.button26.resize(50,50)
        self.button26.setStyleSheet("background-color: #7FFF00; border-radius: 5px")

        self.button36 = QPushButton("As", self)
        self.button36.setFont(QtGui.QFont('Impact', 14))
        self.button36.setToolTip("AppleScript")
        self.button36.move(290,420)
        self.button36.resize(50,50)
        self.button36.setStyleSheet("background-color: #7FFF00; border-radius: 5px")

        self.button44 = QPushButton("Gv", self)
        self.button44.setFont(QtGui.QFont('Impact', 14))
        self.button44.setToolTip("Groovy")
        self.button44.move(290,490)
        self.button44.resize(50,50)
        self.button44.setStyleSheet("background-color: #FF69B4; border-radius: 5px")

        self.button27 = QPushButton("Tc", self)
        self.button27.setFont(QtGui.QFont('Impact', 14))
        self.button27.setToolTip("Tcl")
        self.button27.move(350,360)
        self.button27.resize(50,50)
        self.button27.setStyleSheet("background-color: #7FFF00; border-radius: 5px")

        self.button37 = QPushButton("Cf", self)
        self.button37.setFont(QtGui.QFont('Impact', 14))
        self.button37.setToolTip("Coldfusion")
        self.button37.move(350,420)
        self.button37.resize(50,50)
        self.button37.setStyleSheet("background-color: #7FFF00; border-radius: 5px")

        self.button45 = QPushButton("Rb", self)
        self.button45.setFont(QtGui.QFont('Impact', 14))
        self.button45.setToolTip("Ruby")
        self.button45.move(350,490)
        self.button45.resize(50,50)
        self.button45.setStyleSheet("background-color: #FF69B4; border-radius: 5px")

        self.button18 = QPushButton("C", self)
        self.button18.setFont(QtGui.QFont('Impact', 14))
        self.button18.setToolTip("C")
        self.button18.move(410,300)
        self.button18.resize(50,50)
        self.button18.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button28 = QPushButton("Ht", self)
        self.button28.setFont(QtGui.QFont('Impact', 14))
        self.button28.setToolTip("HyperTalk")
        self.button28.move(410,360)
        self.button28.resize(50,50)
        self.button28.setStyleSheet("background-color: #7FFF00; border-radius: 5px")

        self.button38 = QPushButton("Js", self)
        self.button38.setFont(QtGui.QFont('Impact', 14))
        self.button38.setToolTip("JavasScript")
        self.button38.move(410,420)
        self.button38.resize(50,50)
        self.button38.setStyleSheet("background-color: #7FFF00; border-radius: 5px")

        self.button46 = QPushButton("G", self)
        self.button46.setFont(QtGui.QFont('Impact', 14))
        self.button46.setToolTip("GO")
        self.button46.move(410,490)
        self.button46.resize(50,50)
        self.button46.setStyleSheet("background-color: #A9A9A9; border-radius: 5px")

        self.button10 = QPushButton("P", self)
        self.button10.setFont(QtGui.QFont('Impact', 14))
        self.button10.setToolTip("PL/1")
        self.button10.move(470,240)
        self.button10.resize(50,50)
        self.button10.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button19 = QPushButton("M", self)
        self.button19.setFont(QtGui.QFont('Impact', 14))
        self.button19.setToolTip("Modula")
        self.button19.move(470,300)
        self.button19.resize(50,50)
        self.button19.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button46 = QPushButton("Pl", self)
        self.button46.setFont(QtGui.QFont('Impact', 14))
        self.button46.setToolTip("Perl")
        self.button46.move(470,360)
        self.button46.resize(50,50)
        self.button46.setStyleSheet("background-color: #7FFF00; border-radius: 5px")

        self.button29 = QPushButton("Pp", self)
        self.button29.setFont(QtGui.QFont('Impact', 14))
        self.button29.setToolTip("PHP")
        self.button29.move(470,420)
        self.button29.resize(50,50)
        self.button29.setStyleSheet("background-color: #7FFF00; border-radius: 5px")

        self.button47 = QPushButton("Cj", self)
        self.button47.setFont(QtGui.QFont('Impact', 14))
        self.button47.setToolTip("Clojure")
        self.button47.move(470,490)
        self.button47.resize(50,50)
        self.button47.setStyleSheet("background-color: #1E90FF; border-radius: 5px")

        self.button5 = QPushButton("Cb", self)
        self.button5.setFont(QtGui.QFont('Impact', 14))
        self.button5.setToolTip("COBOL")
        self.button5.move(530,180)
        self.button5.resize(50,50)
        self.button5.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button11 = QPushButton("B", self)
        self.button11.setFont(QtGui.QFont('Impact', 14))
        self.button11.setToolTip("B")
        self.button11.move(530,240)
        self.button11.resize(50,50)
        self.button11.setStyleSheet("background-color: #F0E68C; border-radius: 5px")

        self.button20 = QPushButton("Ml", self)
        self.button20.setFont(QtGui.QFont('Impact', 14))
        self.button20.setToolTip("ML")
        self.button20.move(530,300)
        self.button20.resize(50,50)
        self.button20.setStyleSheet("background-color: #1E90FF; border-radius: 5px")

        self.button30 = QPushButton("Cl", self)
        self.button30.setFont(QtGui.QFont('Impact', 14))
        self.button30.setToolTip("Common LISP")
        self.button30.move(530,360)
        self.button30.resize(50,50)
        self.button30.setStyleSheet("background-color: #1E90FF; border-radius: 5px")

        self.button40 = QPushButton("Fs", self)
        self.button40.setFont(QtGui.QFont('Impact', 14))
        self.button40.setToolTip("F#")
        self.button40.move(530,420)
        self.button40.resize(50,50)
        self.button40.setStyleSheet("background-color: #1E90FF; border-radius: 5px")
        
        self.button2 = QPushButton("E", self)
        self.button2.setFont(QtGui.QFont('Impact', 14))
        self.button2.setToolTip("ENIAC Short Code")
        self.button2.move(590,120)
        self.button2.resize(50,50)
        self.button2.setStyleSheet("background-color: #CD5C5C; border-radius: 5px")

        self.button6 = QPushButton("L", self)
        self.button6.setFont(QtGui.QFont('Impact', 14))
        self.button6.setToolTip("LISP")
        self.button6.move(590,180)
        self.button6.resize(50,50)
        self.button6.setStyleSheet("background-color: #1E90FF; border-radius: 5px")

        self.button12 = QPushButton("Lg", self)
        self.button12.setFont(QtGui.QFont('Impact', 14))
        self.button12.setToolTip("LOGO")
        self.button12.move(590,240)
        self.button12.resize(50,50)
        self.button12.setStyleSheet("background-color: #1E90FF; border-radius: 5px")

        self.button21 = QPushButton("Sc", self)
        self.button21.setFont(QtGui.QFont('Impact', 14))
        self.button21.setToolTip("Scheme")
        self.button21.move(590,300)
        self.button21.resize(50,50)
        self.button21.setStyleSheet("background-color: #1E90FF; border-radius: 5px")

        self.button31 = QPushButton("Er", self)
        self.button31.setFont(QtGui.QFont('Impact', 14))
        self.button31.setToolTip("Erlang")
        self.button31.move(590,360)
        self.button31.resize(50,50)
        self.button31.setStyleSheet("background-color: #1E90FF; border-radius: 5px")

        self.button41 = QPushButton("Hk", self)
        self.button41.setFont(QtGui.QFont('Impact', 14))
        self.button41.setToolTip("Haskell")
        self.button41.move(590,420)
        self.button41.resize(50,50)
        self.button41.setStyleSheet("background-color: #1E90FF; border-radius: 5px")
# Mechanical
        self.button01 = QPushButton(self)
        self.button01.move(50,560)
        self.button01.resize(20,20)
        self.button01.setStyleSheet("background-color: #CD5C5C; border-radius: 2px")
        
        self.textboxlbl01 = QLabel("Mechanical",self)
        self.textboxlbl01.move(80,562)
        self.textboxlbl01.setFont(QtGui.QFont('Perpetua', 12))
# Imperative
        self.button02 = QPushButton(self)
        self.button02.move(50,600)
        self.button02.resize(20,20)
        self.button02.setStyleSheet("background-color: #F0E68C; border-radius: 2px")
        
        self.textboxlbl02 = QLabel("Imperative",self)
        self.textboxlbl02.move(80,602)
        self.textboxlbl02.setFont(QtGui.QFont('Perpetua', 12))
# Object Oriented
        self.button03 = QPushButton(self)
        self.button03.move(50,640)
        self.button03.resize(20,20)
        self.button03.setStyleSheet("background-color: #FFA07A; border-radius: 2px")
        
        self.textboxlbl03 = QLabel("Object Oriented",self)
        self.textboxlbl03.move(80,642)
        self.textboxlbl03.setFont(QtGui.QFont('Perpetua', 12))
# Scripting
        self.button04 = QPushButton(self)
        self.button04.move(270,560)
        self.button04.resize(20,20)
        self.button04.setStyleSheet("background-color: #7FFF00; border-radius: 2px")
        
        self.textboxlbl04 = QLabel("Scripting",self)
        self.textboxlbl04.move(300,562)
        self.textboxlbl04.setFont(QtGui.QFont('Perpetua', 12))
# Declarative
        self.button05 = QPushButton(self)
        self.button05.move(270,600)
        self.button05.resize(20,20)
        self.button05.setStyleSheet("background-color: #FF00FF; border-radius: 2px")
        
        self.textboxlbl05 = QLabel("Declarative",self)
        self.textboxlbl05.move(300,602)
        self.textboxlbl05.setFont(QtGui.QFont('Perpetua', 12))
# Functional
        self.button06 = QPushButton(self)
        self.button06.move(270,640)
        self.button06.resize(20,20)
        self.button06.setStyleSheet("background-color: #1E90FF; border-radius: 2px")
        
        self.textboxlbl06 = QLabel("Functional",self)
        self.textboxlbl06.move(300,642)
        self.textboxlbl06.setFont(QtGui.QFont('Perpetua', 12))
# Dynamic
        self.button07 = QPushButton(self)
        self.button07.move(490,560)
        self.button07.resize(20,20)
        self.button07.setStyleSheet("background-color: #FF69B4; border-radius: 2px")
        
        self.textboxlbl07 = QLabel("Dynamic",self)
        self.textboxlbl07.move(520,562)
        self.textboxlbl07.setFont(QtGui.QFont('Perpetua', 12))
# Concurrent
        self.button08 = QPushButton(self)
        self.button08.move(490,600)
        self.button08.resize(20,20)
        self.button08.setStyleSheet("background-color: #A9A9A9; border-radius: 2px")
        
        self.textboxlbl08 = QLabel("Concurrent",self)
        self.textboxlbl08.move(520,602)
        self.textboxlbl08.setFont(QtGui.QFont('Perpetua', 12))
# Multi-Paradigm
        self.button09 = QPushButton(self)
        self.button09.move(490,640)
        self.button09.resize(20,20)
        self.button09.setStyleSheet("background-color: #40E0D0; border-radius: 2px")
        
        self.textboxlbl09 = QLabel("Multi-Paradigm",self)
        self.textboxlbl09.move(520,642)
        self.textboxlbl09.setFont(QtGui.QFont('Perpetua', 12))
# Create Account 
        self.textboxlbl = QLabel(" Let's Get", self)
        self.textboxlbl.move(850, 100)
        self.textboxlbl.setFont(QtGui.QFont('Berlin Sans FB', 18))

        self.textboxlbl = QLabel("Started", self)
        self.textboxlbl.move(850,120)
        self.textboxlbl.setFont(QtGui.QFont('Berlin Sans FB',36))

        self.textboxlbl = QLabel("Create an account to learn more programming languages", self)
        self.textboxlbl.move(850,170)
        self.textboxlbl.setFont(QtGui.QFont('Berlin Sans FB',9))

# first name
        self.textboxlbl = QLabel(" First Name",self)
        self.textboxlbl.move(850,230)
        self.textboxlbl.setFont(QtGui.QFont('Berlin Sans FB',10))

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(850,250)
        self.textbox1.resize(130,25)

# last name
        self.textboxlbl = QLabel(" Last Name",self)
        self.textboxlbl.move(1000,230)
        self.textboxlbl.setFont(QtGui.QFont('Berlin Sans FB',10))

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(1000,250)
        self.textbox2.resize(130,25)

# email address
        self.textboxlbl = QLabel(" Email Address",self)
        self.textboxlbl.move(850,290)
        self.textboxlbl.setFont(QtGui.QFont('Berlin Sans FB',10))

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(850,310)
        self.textbox3.resize(280,25)

# password
        self.textboxlbl = QLabel(" Password",self)
        self.textboxlbl.move(850,350)
        self.textboxlbl.setFont(QtGui.QFont('Berlin Sans FB',10))

        self.textbox4 = QLineEdit(self)
        self.textbox4.setEchoMode(QLineEdit.Password)
        self.textbox4.move(850,370)
        self.textbox4.resize(280,25)

#contact number
        self.textboxlbl5 = QLabel(" Contact Number",self)
        self.textboxlbl5.move(850,410)
        self.textboxlbl5.setFont(QtGui.QFont('Berlin Sans FB',10))

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(850,430)
        self.textbox5.resize(280,25)

        self.buttonc = QPushButton("CREATE ACCOUNT", self)
        self.buttonc.setFont(QtGui.QFont('Arial Rounded MT Bold', 9))
        self.buttonc.move(850,480)
        self.buttonc.resize(280,40)
        self.buttonc.clicked.connect(self.account)

        self.show()

    @pyqtSlot()

    def account(self):
        first_Name = self.textbox1.text()
        last_Name = self.textbox2.text()
        email_Add = self.textbox3.text()
        password = self.textbox4.text()
        con_number = self.textbox5.text()
        self.submitdata(first_Name, last_Name, email_Add, password, con_number)

        
    def submitdata(self, first_Name, last_Name, email_Add, password, con_number):
        submit = QMessageBox.question(self, "Creating Account", "Do you want to submit all the information?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if submit == QMessageBox.Yes and first_Name != "" and last_Name != "" and email_Add != "" and password != ""  and con_number != "":
            dataDB = SqliteDict("acc_reg.db", autocommit=True)
            reg_list = dataDB.get('registration',[])
            list_dict = {"First Name": first_Name, "Last Name": last_Name, "Email Address": email_Add, "Password": password, "Contact Number": con_number}
            reg_list.append(list_dict)
            dataDB['registration'] = reg_list
            print(dataDB['registration'])

            QMessageBox.information(self, "Registration", "Registration Complete!", QMessageBox.Ok, QMessageBox.Ok)
        
        elif submit == QMessageBox.No:
            pass
        elif submit == QMessageBox.No and first_Name == "" and last_Name == "" and email_Add == "" and password == "" and con_number == "":
            pass
        elif submit == QMessageBox.No and first_Name == "" or last_Name == "" or email_Add == "" or password == "" or con_number == "":
            QMessageBox.warning(self, "Error","Please fill-in all the blank spaces.", QMessageBox.Ok, QMessageBox.Ok)

        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")
        self.textbox5.setText("")


    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Confirmation',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

    

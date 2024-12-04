from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton , QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit

import random as rdn
from nltk.corpus import words
import nltk

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import re


# Main App Objects and Settings
app           = QApplication([]) 

main_window   = QWidget() 

main_window.setWindowTitle("Calculator")

main_window.resize( 250 , 300)

main_Layout     = QGridLayout()

main_Layout_1   = QGridLayout()

master_Layout    = QVBoxLayout() 

# Calculator screen
Calc_text = QLineEdit()
Calc_text.setPlaceholderText("0")
Calc_text.setFixedWidth(500)
main_Layout_1.addWidget(Calc_text,0,0)

# create all App Objects

Buttons = [ "AC" , "+/-" , "%" , "/", "7", "8", "9", "*", "4" , "5", "6" , 
           "-", "1", "2", "3", "+" , "0", "="]

#Buttons = [ "7" , "8" , "9" , "/", "4", "5", "6", "*", "1" , "2", "3" , 
#           "+", "1", "2", "3", "+" , "0", "="]

def is_number(value):
    try:
        float(value)
        return True
    except(ValueError, TypeError):
        return False
    
def SetCalxcText(value_test):
    Calc_text.setPlaceholderText(value_test)

rows    = 1 
col     = 0 
but_num = 0 ; 
Button_calc =[]
for button_calc in Buttons:
    Button_calc.append( QPushButton(button_calc) ) 
    main_Layout.addWidget(Button_calc[but_num], rows,col)  # zeile row, column col
    col                 = col     + 1 
    if col > 3:
        col = 0 
        rows  = rows+1

    if is_number(button_calc):
        Button_calc[but_num].clicked.connect(lambda: Calc_text.setPlaceholderText(Button_calc[but_num].text()))

    but_num              = but_num  + 1



but_num = 0 ; 

master_Layout.addLayout(main_Layout_1) 
master_Layout.addLayout(main_Layout) 

main_window.setLayout(master_Layout)




#for pos_numb in np.arange(0,len(Buttons),1):
 #   if is_number(Button_calc[pos_numb].text()):
 #       Button_calc[pos_numb].clicked.connect(lambda: Calc_text.setPlaceholderText(str(Button_calc[pos_numb].text())))

#Button_calc[4].clicked.connect(lambda: Calc_text.setPlaceholderText("7"))
#Button_calc[5].clicked.connect(lambda: Calc_text.setPlaceholderText("8"))
#Button_calc[6].clicked.connect(lambda: Calc_text.setPlaceholderText("9"))
#Button_calc[8].clicked.connect(lambda: Calc_text.setPlaceholderText("4"))
#Button_calc[9].clicked.connect(lambda: Calc_text.setPlaceholderText("5"))
#Button_calc[10].clicked.connect(lambda: Calc_text.setPlaceholderText("6"))
#Button_calc[12].clicked.connect(lambda: Calc_text.setPlaceholderText("1"))
#Button_calc[13].clicked.connect(lambda: Calc_text.setPlaceholderText("2"))
#Button_calc[14].clicked.connect(lambda: Calc_text.setPlaceholderText("3"))
#Button_calc[16].clicked.connect(lambda: Calc_text.setPlaceholderText("0"))


# Show/ Run our App

main_window.show()
app.exec_()

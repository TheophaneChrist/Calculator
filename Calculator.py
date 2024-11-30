from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton , QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit

import random as rdn
from nltk.corpus import words
import nltk

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


# Main App Objects and Settings
app           = QApplication([]) 

main_window   = QWidget() 

main_window.setWindowTitle("Calculator")

main_window.resize( 700 , 1000)

main_Layout   = QGridLayout()


# create all App Objects

Buttons = [ "AC" , "+/-" , "%" , "/", "7", "8", "9", "*", "4" , "5", "6" , 
           "-", "1", "2", "3", "+" , "0", "="]

Buttons = [ "7" , "8" , "9" , "/", "4", "5", "6", "*", "1" , "2", "3" , 
           "+", "1", "2", "3", "+" , "0", "="]
rows    = 0 
col     = 0 
but_num = 0 ; 
Button_calc =[]
for button_calc in Buttons:
    Button_calc.append( QPushButton(button_calc) ) 
    main_Layout.addWidget(Button_calc[but_num], col,rows)  # zeile row, column col
    rows                 = rows     + 1 
    but_num              = but_num  + 1
    if rows > 3:
        rows = 0 
        col  = col+1

main_window.setLayout(main_Layout)

# Show/ Run our App

main_window.show()
app.exec_()

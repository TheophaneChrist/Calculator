from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton , QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtCore import QCoreApplication, QEvent


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
           "-", "1", "2", "3", "+" , "0","<", "="]



def button_click():
    button = main_window.sender()
    text   = button.text()

    if text == "=":
        symbol = Calc_text.text()
        try:
            res = eval(symbol)
            Calc_text.setText(str(res))
        except Exception as e:
            print("Error:", e)

    elif text == "AC":                      # Clear button
        Calc_text.clear()
    
    elif text == "%" :
        current_value = Calc_text.text()
        current_value = eval(current_value)
        Calc_text.setText(str(current_value/100))

    elif text == "+/-"  :
        current_value = Calc_text.text()
        current_value = eval(current_value)
        Calc_text.setText(str(-1*current_value))

    elif text == "<" :
        current_value = Calc_text.text()
        Calc_text.setText(current_value[:-1])                  # Delete button

    else:
        current_value = Calc_text.text()
        Calc_text.setText( current_value + text)








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
    Button_calc[but_num].clicked.connect(button_click)
    main_Layout.addWidget(Button_calc[but_num], rows,col)  # zeile row, column col
    col      += 1
    if col > 3:
        col = 0 
        rows  = rows+1

#    if is_number(button_calc):
        #Button_calc[but_num].clicked.connect(lambda: Calc_text.setPlaceholderText(Button_calc[but_num].text()))
        #Button_calc[but_num].clicked.connect(lambda but_num=but_num: Calc_text.setPlaceholderText(Button_calc[but_num].text()))
#        Button_calc[but_num].clicked.connect(lambda _, but_num=but_num: Calc_text.setPlaceholderText(Button_calc[but_num].text()))
    but_num  += 1 



but_num = 0 ; 

master_Layout.addLayout(main_Layout_1) 
master_Layout.addLayout(main_Layout) 
main_window.setLayout(master_Layout)




# Show/ Run our App

main_window.show()
app.exec_()

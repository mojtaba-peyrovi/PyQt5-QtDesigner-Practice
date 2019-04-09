# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:11:51 2019

@author: mojiway
"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

app = QtWidgets.QApplication([])
dlg = uic.loadUi("shopping-list.ui")

def addItem():
    if not dlg.input.text() == "":
        dlg.output.addItem(dlg.input.text())
        dlg.input.setText("")
    else:
        show_message("Warning","Please add an item first!")

def  show_message(title, message):
    QMessageBox.information(None,title,message)


show_message("Welcome!","Hi User, Welcome to Moji's Shopping List App" )
dlg.input.setFocus()
dlg.input.setPlaceholderText("what item would you like to add?")
dlg.input.returnPressed.connect(addItem)
    
dlg.add_btn.clicked.connect(addItem)

dlg.show()
app.exec()

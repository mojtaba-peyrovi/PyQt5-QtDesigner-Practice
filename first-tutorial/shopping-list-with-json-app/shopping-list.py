# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:11:51 2019

@author: mojiway
"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import json
app = QtWidgets.QApplication([])
dlg = uic.loadUi("shopping-list.ui")

def addItem():
    if not dlg.input.text() == "":
        dlg.output.addItem(dlg.input.text())     
       
    else:
        show_message("Warning","Please add an item first!")
      
    with open('data.json','r') as file:
        data = json.load(file)
    data["items"].append(dlg.input.text())
       
    with open('data.json','w') as file:
        json.dump(data,file)
        
    dlg.input.setText("")    
    
    
def  show_message(title, message):
    QMessageBox.information(None,title,message)


show_message("Welcome!","Hi User, Welcome to Moji's Shopping List App" )
dlg.input.setFocus()
dlg.input.setPlaceholderText("what item would you like to add?")

def main():
    with open('data.json','r') as file:
        data = json.load(file)
        
    for item in data["items"]:
        dlg.output.addItem(item)
        
if __name__ == "__main__":
    main()    

dlg.input.returnPressed.connect(addItem)
dlg.add_btn.clicked.connect(addItem)

dlg.show()
app.exec()

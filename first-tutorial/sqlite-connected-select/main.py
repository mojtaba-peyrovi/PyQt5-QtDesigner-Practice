# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:33:19 2019

@author: mojiway
"""
#PyQt imports:
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

# database connection import
from  sqlite import  SqliteHelper

app = QtWidgets.QApplication([])
dlg =uic.loadUi("test.ui")


def loadData():
    helper = SqliteHelper("test.db")
    users = helper.select("SELECT * FROM user")
    
    for row_number, user in enumerate(users):
        dlg.test_table.insertRow(row_number)        
        for column_number, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.test_table.setItem(row_number, column_number, cell)

dlg.load_btn.clicked.connect(loadData)    


dlg.show()
app.exec()

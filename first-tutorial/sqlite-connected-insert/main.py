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

helper = SqliteHelper("test.db")

def loadData():

    users = helper.select("SELECT * FROM user")
    
    for row_number, user in enumerate(users):
        dlg.test_table.insertRow(row_number)        
        for column_number, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.test_table.setItem(row_number, column_number, cell)

def clearData():
    while(dlg.test_table.rowCount() > 0):
        dlg.test_table.removeRow(0)
        

def add_user():
     name = dlg.lineEdit_name.text()
     year = dlg.lineEdit_year.text()
     admin = dlg.checkBox_admin.isChecked()     
     a=0 
     if admin:
        a = 1
     user = (name, int(year), admin)        
     helper.insert("INSERT INTO user (name, year, admin) VALUES (?,?,?)", user )
     clearData() 
     loadData()
dlg.insert_btn.clicked.connect(add_user)    
    
loadData()    



dlg.show()
app.exec()

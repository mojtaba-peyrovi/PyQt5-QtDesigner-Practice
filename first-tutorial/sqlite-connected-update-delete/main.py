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
    dlg.test_table.clearSelection()
    while(dlg.test_table.rowCount() > 0):
        dlg.test_table.removeRow(0)
        dlg.test_table.clearSelection()
        

def add_user():
     name = dlg.lineEdit_name.text()
     year = dlg.lineEdit_year.text()
     admin = dlg.checkBox_admin.isChecked()     
     a=0 
     if admin:
        a = 1
     if name.strip(" ") != "" and year.strip(" ") !="":   
         user = (name, int(year), admin)        
         helper.insert("INSERT INTO user (name, year, admin) VALUES (?,?,?)", user )
         refresh()
     else:
         QMessageBox.information(None, 'Error','Empty field found!')
         
def selectionChanged():
    selected_row = getSelectedRowId()
    name = dlg.test_table.item(selected_row-1, 1).text()
    year = dlg.test_table.item(selected_row-1, 2).text()
    admin = dlg.test_table.item(selected_row-1, 3).text()
    if admin == "1":
        dlg.checkBox_admin.setChecked(True)
    else:
        dlg.checkBox_admin.setChecked(False)
    dlg.lineEdit_name.setText(name)
    dlg.lineEdit_year.setText(year)

def getSelectedRowId():
    return dlg.test_table.currentRow() + 1


def deleteUser():
    id_delete = str(getSelectedRowId())
    helper.delete("DELETE from user WHERE id="+id_delete)        
    refresh()
def refresh():
    clearData()
    loadData()    
def updateUser():
    id_update = str(getSelectedRowId())
    
    name = dlg.lineEdit_name.text()
    year = dlg.lineEdit_year.text()
    admin = dlg.checkBox_admin.isChecked()     
    a=0 
    if admin:
        a = 1
    if name.strip(" ") != "" and year.strip(" ") !="":   
        user = (name, int(year), admin)        
        helper.edit("UPDATE user SET name=?, year=?, admin=? WHERE id="+id_update, user)
        refresh()
    else:
        QMessageBox.information(None, 'Error','Empty field found!')
    

        
dlg.insert_btn.clicked.connect(add_user) 
dlg.test_table.itemSelectionChanged.connect(selectionChanged)   

dlg.update_btn.clicked.connect(updateUser)
dlg.delete_btn.clicked.connect(deleteUser)    
loadData()    



dlg.show()
app.exec()

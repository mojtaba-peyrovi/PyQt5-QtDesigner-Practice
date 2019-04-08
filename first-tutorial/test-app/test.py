# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:28:47 2019

@author: mojiway
"""

from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")

dlg.show()
app.exec()
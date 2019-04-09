# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:41:58 2019

@author: mojiway
"""

from PyQt5 import QtWidgets, uic

def convert():
    dlg.output.setText(str(float(dlg.input.text())* 1.12))


app = QtWidgets.QApplication([])
dlg = uic.loadUi("converter.ui")

dlg.input.setFocus()
dlg.input.setPlaceholderText("EUR")
dlg.output.setPlaceholderText("USD")

dlg.conv_btn.clicked.connect(convert)
dlg.input.returnPressed.connect(convert)

dlg.output.setReadOnly(True)

dlg.show()
app.exec()


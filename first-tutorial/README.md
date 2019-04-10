#### PyQt5 Tutorial:

Source: [Ziga Benko YouTube channel](https://www.youtube.com/watch?v=mBvpoNLb654&list=PLuTktZ8WcEGTdId-Kjbj6gsZTk65yudJh)

---

A good guide for installing pyqt5 and designer: [here](https://www.youtube.com/watch?v=_hgWvuhreHA)

First we need to make a .ui file. In Qt Designer we make a new form and make sure we choose Main Window. Then for testing purpose, we place a button on it. Then we save it as test.ui.

Next step, is making the py file to interact with the ui.

Here is the code at test.py file:

```
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")

dlg.show()
app.exec()
```
And we save it in the same folder as the ui file is. Now when we load test.py file, the ui will load. 

#### Currency converter app:

Now we make a new ui using a button and two "Line Edit" widgets. 

The first Line Edit for EURO as input, and another for USD as output. 

Then we will have to write the python app for it. we call it converter.py. 

__NOTE:__ Anytime we want to reference any object in the ui, we need to uave dgl. behind it. and dlg is coming from here:

```
dlg = uic.loadUi("ui_file_name")
```

__setText():__ prints the value of a textbox to whatever we write inside brackets.

__setPlaceholderText():__ It sets placeholder for the input field.

In order to connect an action or function to a button-click event:

```
dlg.btn_name.clicked.connect(function_name)
```
__setFocus():__ we can set the focus on any object we need.

__returnPressed():__ we can trigger a function, once we press enter on an object.
```
dlg.object_name.returnPressed.connect(function_name)
```
__setReadOnly(True):__ Anytime we want to make a field read-only we can use this.
```
dlg.object_name.setReadOnly(True)
```
__addItem():__ It is used for list widgets and adds items to the list.

__QMessageBox:__ It is a library inside QtWidgets that shows message boxes:
```
QtMessageBox.information(None,"title","message")
```
 
__Note:__ Anytime we want some functions run as soon as the app runs we say:

```
def main():
    <write the code here>
if __name__ == "__main__":
    main()
```

We can make the application read/write from/into json file. the code is located in an app folder called "shopping-list-with-json-app"

#### Connecting SQlite to the app:


The code can be seem in the file sqlite.py. And we imported sqlite3, and made the class and construct, and instantiated a test database as test.db.

Now we see that when we run the py file, the database will be created in the same folder.

Next thing,we made a function in the py file, that runs a sql code and creates a table called users.

We made all update, insert, and select data into the table inside sqlite.py. 

#### Connect SQLite functionality to table widget in PyQt table widget:

__Select functionality:__ The code has been saved at sqlite-connected-select.



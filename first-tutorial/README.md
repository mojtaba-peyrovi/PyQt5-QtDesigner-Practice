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



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

import windows
import utils

def search(ui):
    month= ui.lineEdit.text()
    day=ui.lineEdit_2.text()
    d=utils.date(month,day)
    ui.textBrowser.setText(d.get_todevs())
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = windows.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(search, ui))
    
    sys.exit(app.exec_())
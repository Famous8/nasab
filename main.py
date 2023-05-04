from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from UI.GrampsUI import Ui_MainWindow
from widgets.dialog import Dialog
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dialog = Dialog(self)
        self.ui.sources.mainApp = self

        self.parsedGedcom = None

        self.ui.topBar.loadTreeButton.clicked.connect(lambda: self.dialog.show())
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.dashboard)

    def load(self):
        self.ui.peopleList.loadPeopleList(self.parsedGedcom.fullGedcom)
        self.ui.familyList.loadFamilyList(self.parsedGedcom.familyList)
        self.ui.sources.loadSourcesList(self.parsedGedcom.sourcesList)

    def closeEvent(self, event):
        self.dialog.dump()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.dialog.show()
    app.exec()

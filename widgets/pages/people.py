from PyQt6 import QtWidgets, QtCore


class peoplePage(QtWidgets.QWidget):
    def __init__(self, ui):
        QtWidgets.QWidget.__init__(self)

        self.tree = None
        self.mainApp = None
        self.ui = ui

        self.setObjectName("peopleList")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.peopleList_2 = QtWidgets.QTableWidget(self)
        self.peopleList_2.setObjectName("peopleList_2")
        self.verticalLayout_5.addWidget(self.peopleList_2)

        self.peopleList_2.itemDoubleClicked.connect(
            lambda: self.ui.profile.loadProfile(
                self.findPersonByName(self.peopleList_2.item(self.peopleList_2.currentRow(), 0).text())))

    def findPersonByName(self, name):
        for person in self.tree:
            if person.name == name:
                return person

        return None

    def loadPeopleList(self, tree):
        self.tree = tree
        self.peopleList_2.clear()
        self.peopleList_2.setColumnCount(3)
        self.peopleList_2.setRowCount(len(tree))
        self.peopleList_2.setHorizontalHeaderLabels(["Name", "Birth Date", "Death Date"])

        self.peopleList_2.setColumnWidth(0, 300)
        self.peopleList_2.setColumnWidth(1, 250)
        self.peopleList_2.setColumnWidth(2, 100)

        row = 0

        for person in self.tree:
            self.peopleList_2.setItem(row, 0, QtWidgets.QTableWidgetItem(person.name))

            try:
                if person.birth:
                    self.peopleList_2.setItem(row, 1, QtWidgets.QTableWidgetItem(person.birth[0][0]))

                if person.death:
                    self.peopleList_2.setItem(row, 2, QtWidgets.QTableWidgetItem(person.death[0][0]))

            except IndexError:
                pass

            row += 1

from PyQt6 import QtWidgets, QtCore, QtGui

class familyPage(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.mainApp = None

        self.setObjectName("familyList")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.familyListArea = QtWidgets.QListWidget(self)
        self.familyListArea.setObjectName("familyListArea")
        self.verticalLayout_6.addWidget(self.familyListArea)

    def loadFamilyList(self, list):
        self.familyListArea.clear()

        for family in list:
            item = None

            if family.parentOne and family.parentTwo:
                item = QtWidgets.QListWidgetItem(f"{family.parentOne.name} and {family.parentTwo.name}'s family")

            elif family.parentOne:
                item = QtWidgets.QListWidgetItem(f"{family.parentOne.name}'s family")

            elif family.children:
                item = QtWidgets.QListWidgetItem(
                    f"This family has no parents. It includes - {family.children[0].name} and {len(family.children) - 1} more members")

            if item:
                self.familyListArea.addItem(item)

class familyView(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.mainApp = None
        self.setObjectName("familyView")
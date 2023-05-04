from PyQt6 import QtWidgets, QtCore, QtGui

class topBar(QtWidgets.QWidget):
    def __init__(self, parent, ui):
        QtWidgets.QWidget.__init__(self)
        
        self.parent = parent
        self.ui = ui

        self.setMinimumSize(QtCore.QSize(0, 70))
        self.setStyleSheet("background-color: #F5F5F5;\n""")
        self.setObjectName("topBar")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pageName = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pageName.setFont(font)
        self.pageName.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.pageName.setObjectName("pageName")
        self.horizontalLayout_10.addWidget(self.pageName)
        self.searchButton = QtWidgets.QPushButton(self)
        self.searchButton.setEnabled(True)
        self.searchButton.setMinimumSize(QtCore.QSize(40, 40))
        self.searchButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("background-color: #85A09A;\n"
                                        "border: 1px solid white;\n"
                                        "border-radius: 20;\n"
                                        "color: white")
        self.searchButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Icons/PNG/search_FILL0_wght400_GRAD0_opsz48.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.searchButton.setIcon(icon)
        self.searchButton.setIconSize(QtCore.QSize(20, 20))
        self.searchButton.setAutoDefault(False)
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(True)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_10.addWidget(self.searchButton)
        self.searchLineEdit = QtWidgets.QLineEdit(self)
        self.searchLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.searchLineEdit.setStyleSheet("border-radius: 15;\n"
                                          "background-color: #F5F5F5;\nborder: 1px solid #85A09A"
                                          "")
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.searchLineEdit.setMaximumWidth(0)
        self.horizontalLayout_10.addWidget(self.searchLineEdit)
        self.loadTreeButton = QtWidgets.QPushButton(self)
        self.loadTreeButton.setEnabled(True)
        self.loadTreeButton.setMinimumSize(QtCore.QSize(150, 40))
        self.loadTreeButton.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.loadTreeButton.setFont(font)
        self.loadTreeButton.setStyleSheet("background-color: #85A09A;\n"
                                          "border: 1px solid white;\n"
                                          "border-radius: 20;\n"
                                          "color: white")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Icons/PNG/Icon material-file-uploadwhite.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.loadTreeButton.setIcon(icon1)
        self.loadTreeButton.setIconSize(QtCore.QSize(20, 20))
        self.loadTreeButton.setAutoDefault(False)
        self.loadTreeButton.setDefault(False)
        self.loadTreeButton.setFlat(True)
        self.loadTreeButton.setObjectName("loadTreeButton")
        self.horizontalLayout_10.addWidget(self.loadTreeButton)

        self.searchButton.clicked.connect(self.searchAnimation)
        self.searchLineEdit.textChanged.connect(self.search)
        
    def search(self):
        query = self.searchLineEdit.text().lower()
        if self.ui.GrampsMainPages.currentWidget() == self.ui.peopleList:
            currentList = self.ui.peopleList.peopleList_2
            count = currentList.rowCount()

            for row in range(count):
                item = currentList.item(row, 0)
                currentList.setRowHidden(row, query not in item.text().lower())

        elif self.ui.GrampsMainPages.currentWidget() == self.ui.familyList:
            currentList = self.ui.familyList.familyListArea
            count = currentList.count()

            for row in range(count):
                item = currentList.item(row)
                currentList.setRowHidden(row, query not in item.text().lower())

        elif self.ui.GrampsMainPages.currentWidget() == self.ui.sources:
            currentList = self.ui.sources.sourcesList
            count = currentList.count()

            for row in range(count):
                item = currentList.item(row)
                currentList.setRowHidden(row, query not in item.text().lower())

    def searchAnimation(self):
        width = self.searchLineEdit.width()

        self.animation = QtCore.QPropertyAnimation(self.searchLineEdit, b"maximumWidth")
        self.animation.setDuration(150)

        if width == 250:
            self.animation.setStartValue(250)
            self.animation.setEndValue(0)
            self.searchLineEdit.clear()
            self.animation.start()

        if width == 0:
            self.animation.setStartValue(0)
            self.animation.setEndValue(250)

            self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animation.start()

        if width not in (250, 0):
            self.searchLineEdit.clear()
            self.animation.setStartValue(250)
            self.animation.setEndValue(0)
            self.animation.start()
from PyQt6 import QtCore, QtWidgets, QtGui

class Sidebar(QtWidgets.QWidget):
    def __init__(self, parent, ui):
        super().__init__()

        self.setEnabled(True)
        self.setMinimumSize(QtCore.QSize(240, 520))
        self.setMaximumSize(QtCore.QSize(240, 16777215))
        self.setGeometry(QtCore.QRect(0, 0, 240, 788))
        self.setStyleSheet("background-color: #F5F5F5")
        self.setObjectName("sidebar")
        self.parent = parent
        self.ui = ui

        self.ui.topBar.searchButton.hide()

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 51, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.iconsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.iconsLayout.setContentsMargins(0, 0, 0, 0)
        self.iconsLayout.setObjectName("iconsLayout")
        self.menuButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.menuButton.setEnabled(True)
        self.menuButton.setStyleSheet("QPushButton {\n"
                                      "            background-color: #F5F5F5;\n"
                                      "            border: 1px solid #F5F5F5;\n"
                                      "        }\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "            color: #7e8896;\n"
                                      "        }")
        self.menuButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/PNG/Icon open-grid-three-up.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon open-grid-three-up.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.menuButton.setIcon(icon3)
        self.menuButton.setIconSize(QtCore.QSize(28, 28))
        self.menuButton.setFlat(True)
        self.menuButton.setObjectName("menuButton")
        self.iconsLayout.addWidget(self.menuButton)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.iconsLayout.addItem(spacerItem12)
        self.dashIcon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dashIcon.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.dashIcon.setFont(font)
        self.dashIcon.setStyleSheet("QPushButton {\n"
                                    "            background-color: #F5F5F5;\n"
                                    "            border: 1px solid #F5F5F5;\n"
                                    "        }\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "            color: #7e8896;\n"
                                    "        }")
        self.dashIcon.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/PNG/Icon material-dashboard.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon material-dashboard.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.dashIcon.setIcon(icon4)
        self.dashIcon.setIconSize(QtCore.QSize(28, 28))
        self.dashIcon.setAutoDefault(False)
        self.dashIcon.setDefault(False)
        self.dashIcon.setFlat(True)
        self.dashIcon.setObjectName("dashIcon")
        self.iconsLayout.addWidget(self.dashIcon)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.iconsLayout.addItem(spacerItem13)
        self.treeIcon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.treeIcon.setEnabled(True)
        self.treeIcon.setStyleSheet("QPushButton {\n"
                                    "            background-color: #F5F5F5;\n"
                                    "            border: 1px solid #F5F5F5;\n"
                                    "        }\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "            color: #7e8896;\n"
                                    "        }")
        self.treeIcon.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/PNG/Icon metro-tree.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon5.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon metro-tree.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.treeIcon.setIcon(icon5)
        self.treeIcon.setIconSize(QtCore.QSize(28, 28))
        self.treeIcon.setFlat(True)
        self.treeIcon.setObjectName("treeIcon")
        self.iconsLayout.addWidget(self.treeIcon)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.iconsLayout.addItem(spacerItem14)
        self.sourcesIcon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sourcesIcon.setEnabled(True)
        self.sourcesIcon.setStyleSheet("QPushButton {\n"
                                       "            background-color: #F5F5F5;\n"
                                       "            border: 1px solid #F5F5F5;\n"
                                       "        }\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "            color: #7e8896;\n"
                                       "        }")
        self.sourcesIcon.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/PNG/Icon ionic-md-document.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon6.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon ionic-md-document.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.sourcesIcon.setIcon(icon6)
        self.sourcesIcon.setIconSize(QtCore.QSize(28, 28))
        self.sourcesIcon.setFlat(True)
        self.sourcesIcon.setObjectName("sourcesIcon")
        self.iconsLayout.addWidget(self.sourcesIcon)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.iconsLayout.addItem(spacerItem15)
        self.mediaIcon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.mediaIcon.setEnabled(True)
        self.mediaIcon.setStyleSheet("QPushButton {\n"
                                     "            background-color: #F5F5F5;\n"
                                     "            border: 1px solid #F5F5F5;\n"
                                     "        }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "            color: #7e8896;\n"
                                     "        }")
        self.mediaIcon.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/PNG/Icon material-perm-media.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon7.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon material-perm-media.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.mediaIcon.setIcon(icon7)
        self.mediaIcon.setIconSize(QtCore.QSize(28, 28))
        self.mediaIcon.setFlat(True)
        self.mediaIcon.setObjectName("mediaIcon")
        self.iconsLayout.addWidget(self.mediaIcon)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.iconsLayout.addItem(spacerItem16)
        self.placesIcon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.placesIcon.setEnabled(True)
        self.placesIcon.setStyleSheet("QPushButton {\n"
                                      "            background-color: #F5F5F5;\n"
                                      "            border: 1px solid #F5F5F5;\n"
                                      "        }\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "            color: #7e8896;\n"
                                      "        }")
        self.placesIcon.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/PNG/Icon ionic-md-pin.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon8.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon ionic-md-pin.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.placesIcon.setIcon(icon8)
        self.placesIcon.setIconSize(QtCore.QSize(28, 28))
        self.placesIcon.setFlat(True)
        self.placesIcon.setObjectName("placesIcon")
        self.iconsLayout.addWidget(self.placesIcon)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.iconsLayout.addItem(spacerItem17)
        self.notesIcon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.notesIcon.setEnabled(True)
        self.notesIcon.setStyleSheet("QPushButton {\n"
                                     "            background-color: #F5F5F5;\n"
                                     "            border: 1px solid #F5F5F5;\n"
                                     "        }\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "            color: #7e8896;\n"
                                     "        }")
        self.notesIcon.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/PNG/Icon awesome-pen.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon9.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon awesome-pen.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.notesIcon.setIcon(icon9)
        self.notesIcon.setIconSize(QtCore.QSize(28, 28))
        self.notesIcon.setFlat(True)
        self.notesIcon.setObjectName("notesIcon")
        self.iconsLayout.addWidget(self.notesIcon)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.iconsLayout.addItem(spacerItem18)
        self.moreIcon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.moreIcon.setEnabled(True)
        self.moreIcon.setStyleSheet("QPushButton {\n"
                                    "            background-color: #F5F5F5;\n"
                                    "            border: 1px solid #F5F5F5;\n"
                                    "        }\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "            color: #7e8896;\n"
                                    "        }")
        self.moreIcon.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Icons/PNG/Icon feather-more-horizontal.png"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        icon10.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon feather-more-horizontal.png"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.On)
        self.moreIcon.setIcon(icon10)
        self.moreIcon.setIconSize(QtCore.QSize(28, 28))
        self.moreIcon.setFlat(True)
        self.moreIcon.setObjectName("moreIcon")
        self.iconsLayout.addWidget(self.moreIcon)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.iconsLayout.addItem(spacerItem19)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 60, 160, 441))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.buttonsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonsLayout.setObjectName("buttonsLayout")
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.buttonsLayout.addItem(spacerItem20)
        self.dashButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.dashButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.dashButton.setFont(font)
        self.dashButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.dashButton.setStyleSheet("text-align:left;\n"
                                      "\n"
                                      "QPushButton {\n"
                                      "            background-color: #F5F5F5;\n"
                                      "            border: 1px solid #F5F5F5;\n"
                                      "        }\n"
                                      "\n"
                                      "")
        self.dashButton.setIconSize(QtCore.QSize(28, 28))
        self.dashButton.setAutoDefault(False)
        self.dashButton.setDefault(False)
        self.dashButton.setFlat(True)
        self.dashButton.setObjectName("dashButton")
        self.buttonsLayout.addWidget(self.dashButton)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.buttonsLayout.addItem(spacerItem21)
        self.treeButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.treeButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.treeButton.setFont(font)
        self.treeButton.setStyleSheet("text-align:left;\n"
                                      "\n"
                                      "QPushButton {\n"
                                      "            background-color: #F5F5F5;\n"
                                      "            border: 1px solid #F5F5F5;\n"
                                      "        }\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "            color: #7e8896;\n"
                                      "        }")
        self.treeButton.setIconSize(QtCore.QSize(28, 28))
        self.treeButton.setAutoDefault(False)
        self.treeButton.setDefault(False)
        self.treeButton.setFlat(True)
        self.treeButton.setObjectName("treeButton")
        self.buttonsLayout.addWidget(self.treeButton)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.buttonsLayout.addItem(spacerItem22)
        self.sourcesButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.sourcesButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.sourcesButton.setFont(font)
        self.sourcesButton.setStyleSheet("text-align:left;\n"
                                         "\n"
                                         "QPushButton {\n"
                                         "            background-color: #F5F5F5;\n"
                                         "            border: 1px solid #F5F5F5;\n"
                                         "        }\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "            color: #7e8896;\n"
                                         "        }")
        self.sourcesButton.setIconSize(QtCore.QSize(28, 28))
        self.sourcesButton.setAutoDefault(False)
        self.sourcesButton.setDefault(False)
        self.sourcesButton.setFlat(True)
        self.sourcesButton.setObjectName("sourcesButton")
        self.buttonsLayout.addWidget(self.sourcesButton)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.buttonsLayout.addItem(spacerItem23)
        self.mediaButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.mediaButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.mediaButton.setFont(font)
        self.mediaButton.setStyleSheet("text-align:left;\n"
                                       "\n"
                                       "QPushButton {\n"
                                       "            background-color: #F5F5F5;\n"
                                       "            border: 1px solid #F5F5F5;\n"
                                       "        }\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "            color: #7e8896;\n"
                                       "        }")
        self.mediaButton.setIconSize(QtCore.QSize(28, 28))
        self.mediaButton.setAutoDefault(False)
        self.mediaButton.setDefault(False)
        self.mediaButton.setFlat(True)
        self.mediaButton.setObjectName("mediaButton")
        self.buttonsLayout.addWidget(self.mediaButton)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.buttonsLayout.addItem(spacerItem24)
        self.placesButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.placesButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.placesButton.setFont(font)
        self.placesButton.setStyleSheet("text-align:left;\n"
                                        "\n"
                                        "QPushButton {\n"
                                        "            background-color: #F5F5F5;\n"
                                        "            border: 1px solid #F5F5F5;\n"
                                        "        }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "            color: #7e8896;\n"
                                        "        }")
        self.placesButton.setIconSize(QtCore.QSize(28, 28))
        self.placesButton.setAutoDefault(False)
        self.placesButton.setDefault(False)
        self.placesButton.setFlat(True)
        self.placesButton.setObjectName("placesButton")
        self.buttonsLayout.addWidget(self.placesButton)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.buttonsLayout.addItem(spacerItem25)
        self.notesButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.notesButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.notesButton.setFont(font)
        self.notesButton.setStyleSheet("text-align:left;\n"
                                       "\n"
                                       "QPushButton {\n"
                                       "            background-color: #F5F5F5;\n"
                                       "            border: 1px solid #F5F5F5;\n"
                                       "        }\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "            color: #7e8896;\n"
                                       "        }")
        self.notesButton.setIconSize(QtCore.QSize(28, 28))
        self.notesButton.setAutoDefault(False)
        self.notesButton.setDefault(False)
        self.notesButton.setFlat(True)
        self.notesButton.setObjectName("notesButton")
        self.buttonsLayout.addWidget(self.notesButton)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.buttonsLayout.addItem(spacerItem26)
        self.moreButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.moreButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.moreButton.setFont(font)
        self.moreButton.setStyleSheet("text-align:left;\n"
                                      "\n"
                                      "QPushButton {\n"
                                      "            background-color: #F5F5F5;\n"
                                      "            border: 1px solid #F5F5F5;\n"
                                      "        }\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "            color: #7e8896;\n"
                                      "        }")
        self.moreButton.setIconSize(QtCore.QSize(28, 28))
        self.moreButton.setAutoDefault(False)
        self.moreButton.setDefault(False)
        self.moreButton.setFlat(True)
        self.moreButton.setObjectName("moreButton")
        self.buttonsLayout.addWidget(self.moreButton)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.buttonsLayout.addItem(spacerItem27)
        self.logo = QtWidgets.QLabel(self)
        self.logo.setGeometry(QtCore.QRect(70, 10, 158, 51))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.logo.setFont(font)
        self.logo.setStyleSheet("")
        self.logo.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.logo.setObjectName("logo")

        self.menuButton.clicked.connect(lambda: self.toggleMenu())

        self.dashButton.clicked.connect(self.clickDash)
        self.dashIcon.clicked.connect(self.clickDash)

        self.treeButton.clicked.connect(self.clickTree)
        self.treeIcon.clicked.connect(self.clickTree)

        self.sourcesButton.clicked.connect(self.clickSources)
        self.sourcesIcon.clicked.connect(self.clickSources)

        self.mediaButton.clicked.connect(self.clickMedia)
        self.mediaIcon.clicked.connect(self.clickMedia)

        self.placesButton.clicked.connect(self.clickPlaces)
        self.placesIcon.clicked.connect(self.clickPlaces)

        self.notesButton.clicked.connect(self.clickNotes)
        self.notesIcon.clicked.connect(self.clickNotes)

        self.moreButton.clicked.connect(self.clickMore)
        self.moreIcon.clicked.connect(self.clickMore)

        self.ui.peopleButton.clicked.connect(self.clickPeople)
        self.ui.familiesButton.clicked.connect(self.clickFamilies)
        self.ui.settingsButton.clicked.connect(self.clickSettings)

        self.ui.GrampsMainPages.currentChanged.connect(self.onPageChange)

    def toggleMenu(self):
        width = self.width()

        self.animation = QtCore.QPropertyAnimation(self, b"minimumWidth")
        self.animation.setDuration(210)

        if width == 240:
            self.animation.setStartValue(240)
            self.animation.setEndValue(70)

        if width == 70:
            self.animation.setStartValue(70)
            self.animation.setEndValue(240)

        self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation.start()

        if self.width() not in (240, 70):
            self.animation.setStartValue(240)
            self.animation.setEndValue(70)
            self.animation.start()

    def clickDash(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.dashboard)
        self.ui.topBar.pageName.setText("Dashboard")
        self.ui.topBar.searchButton.hide()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def clickTree(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.tree)
        self.ui.topBar.pageName.setText("Tree")
        self.ui.topBar.searchButton.show()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def clickSources(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.sources)
        self.ui.topBar.pageName.setText("Sources")
        self.ui.topBar.searchButton.show()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def clickMedia(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.media)
        self.ui.topBar.pageName.setText("Media")
        self.ui.topBar.searchButton.show()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def clickPlaces(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.places)
        self.ui.topBar.pageName.setText("Places")
        self.ui.topBar.searchButton.show()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def clickNotes(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.notes)
        self.ui.topBar.pageName.setText("Notes")
        self.ui.topBar.searchButton.show()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def clickMore(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.more)
        self.ui.topBar.pageName.setText("More")
        self.ui.topBar.searchButton.hide()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def clickPeople(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.peopleList)
        self.ui.topBar.pageName.setText("People")
        self.ui.topBar.searchButton.show()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def clickFamilies(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.familyList)
        self.ui.topBar.pageName.setText("Families")
        self.ui.topBar.searchButton.show()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def clickSettings(self):
        self.ui.GrampsMainPages.setCurrentWidget(self.ui.settings)
        self.ui.topBar.pageName.setText("Settings")
        self.ui.topBar.searchButton.show()
        self.ui.topBar.searchLineEdit.clear()
        self.ui.topBar.searchLineEdit.setMaximumWidth(0)

    def onPageChange(self):
        if self.ui.GrampsMainPages.currentWidget() in (self.ui.profile, self.ui.sources, self.ui.notes):
            self.ui.GrampsMainPages.setStyleSheet("background-color: #F5F5F5")

        else:
            self.ui.GrampsMainPages.setStyleSheet("background-color: #85A09A")


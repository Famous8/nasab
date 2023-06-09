from PyQt6 import QtWidgets, QtCore, QtGui


class sourcesPage(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.mainApp = None

        self.setObjectName("sources")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sourcesList = QtWidgets.QListWidget(self)
        self.sourcesList.setObjectName("sourcesList")
        self.horizontalLayout_4.addWidget(self.sourcesList)
        self.sourceInfo = QtWidgets.QFrame(self)
        self.sourceInfo.setMinimumSize(QtCore.QSize(400, 0))
        self.sourceInfo.setMaximumSize(QtCore.QSize(550, 16777215))
        self.sourceInfo.setStyleSheet("background-color: white")
        self.sourceInfo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sourceInfo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sourceInfo.setObjectName("sourceInfo")
        self.gridLayout = QtWidgets.QGridLayout(self.sourceInfo)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.sourceAuthorLabelEditable = QtWidgets.QLabel(self.sourceInfo)
        self.sourceAuthorLabelEditable.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.sourceAuthorLabelEditable.setFont(font)
        self.sourceAuthorLabelEditable.setStyleSheet("")
        self.sourceAuthorLabelEditable.setObjectName("sourceAuthorLabelEditable")
        self.gridLayout.addWidget(self.sourceAuthorLabelEditable, 3, 0, 1, 1)
        self.sourceAuthorLabel = QtWidgets.QLabel(self.sourceInfo)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sourceAuthorLabel.setFont(font)
        self.sourceAuthorLabel.setObjectName("sourceAuthorLabel")
        self.gridLayout.addWidget(self.sourceAuthorLabel, 2, 0, 1, 1)
        self.sourceNotesLabel = QtWidgets.QLabel(self.sourceInfo)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sourceNotesLabel.setFont(font)
        self.sourceNotesLabel.setObjectName("sourceNotesLabel")
        self.gridLayout.addWidget(self.sourceNotesLabel, 6, 2, 1, 1)
        self.sourceRepoLabel = QtWidgets.QLabel(self.sourceInfo)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sourceRepoLabel.setFont(font)
        self.sourceRepoLabel.setObjectName("sourceRepoLabel")
        self.gridLayout.addWidget(self.sourceRepoLabel, 2, 2, 1, 1)
        self.sourcePubLabel = QtWidgets.QLabel(self.sourceInfo)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sourcePubLabel.setFont(font)
        self.sourcePubLabel.setObjectName("sourcePubLabel")
        self.gridLayout.addWidget(self.sourcePubLabel, 0, 2, 1, 1)
        self.sourceIDLabel = QtWidgets.QLabel(self.sourceInfo)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sourceIDLabel.setFont(font)
        self.sourceIDLabel.setObjectName("sourceIDLabel")
        self.gridLayout.addWidget(self.sourceIDLabel, 4, 0, 1, 1)
        self.sourceAttachedLabel = QtWidgets.QLabel(self.sourceInfo)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sourceAttachedLabel.setFont(font)
        self.sourceAttachedLabel.setObjectName("sourceAttachedLabel")
        self.gridLayout.addWidget(self.sourceAttachedLabel, 6, 0, 1, 1)
        self.sourcePubDateLabel = QtWidgets.QLabel(self.sourceInfo)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.sourcePubDateLabel.setFont(font)
        self.sourcePubDateLabel.setObjectName("sourcePubDateLabel")
        self.gridLayout.addWidget(self.sourcePubDateLabel, 0, 0, 1, 1)
        self.sourcePublisherLabelEditable = QtWidgets.QLabel(self.sourceInfo)
        self.sourcePublisherLabelEditable.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.sourcePublisherLabelEditable.setFont(font)
        self.sourcePublisherLabelEditable.setStyleSheet("")
        self.sourcePublisherLabelEditable.setObjectName("sourcePublisherLabelEditable")
        self.gridLayout.addWidget(self.sourcePublisherLabelEditable, 1, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem7, 7, 1, 1, 1)
        self.sourceAttachedList = QtWidgets.QListWidget(self.sourceInfo)
        self.sourceAttachedList.setMinimumSize(QtCore.QSize(0, 450))
        self.sourceAttachedList.setObjectName("sourceAttachedList")
        self.gridLayout.addWidget(self.sourceAttachedList, 7, 0, 1, 1)
        self.sourceDateLabelEditable = QtWidgets.QLabel(self.sourceInfo)
        self.sourceDateLabelEditable.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.sourceDateLabelEditable.setFont(font)
        self.sourceDateLabelEditable.setStyleSheet("")
        self.sourceDateLabelEditable.setObjectName("sourceDateLabelEditable")
        self.gridLayout.addWidget(self.sourceDateLabelEditable, 1, 0, 1, 1)
        self.sourceIDLabelEditable = QtWidgets.QLabel(self.sourceInfo)
        self.sourceIDLabelEditable.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.sourceIDLabelEditable.setFont(font)
        self.sourceIDLabelEditable.setStyleSheet("")
        self.sourceIDLabelEditable.setObjectName("sourceIDLabelEditable")
        self.gridLayout.addWidget(self.sourceIDLabelEditable, 5, 0, 1, 1)
        self.sourceNotesList = QtWidgets.QListWidget(self.sourceInfo)
        self.sourceNotesList.setMinimumSize(QtCore.QSize(0, 450))
        self.sourceNotesList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sourceNotesList.setObjectName("sourceNotesList")
        self.gridLayout.addWidget(self.sourceNotesList, 7, 2, 1, 1)
        self.sourceRepoLabelEditable = QtWidgets.QLabel(self.sourceInfo)
        self.sourceRepoLabelEditable.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.sourceRepoLabelEditable.setFont(font)
        self.sourceRepoLabelEditable.setStyleSheet("")
        self.sourceRepoLabelEditable.setObjectName("sourceRepoLabelEditable")
        self.gridLayout.addWidget(self.sourceRepoLabelEditable, 3, 2, 1, 1)
        self.horizontalLayout_4.addWidget(self.sourceInfo)
        self.sourcePublisherLabelEditable.setWordWrap(True)

        self.sourcesList.currentItemChanged.connect(self.loadSourcesPage)

    def loadSourcesList(self, list):
        self.sourcesList.clear()

        for source in list:
            if source.name is not None:
                item = QtWidgets.QListWidgetItem(source.name)
                self.sourcesList.addItem(item)

    def loadSourcesPage(self):
        self.sourceAttachedList.clear()

        if self.sourcesList.currentItem():
            source = self.findSourceFromName(self.sourcesList.currentItem().text())

            self.sourceIDLabelEditable.setText(source.id)
            self.sourcePublisherLabelEditable.setText(source.publisher)
            self.sourceAuthorLabelEditable.setText(source.author)
            self.sourceDateLabelEditable.setText(source.date)
            self.sourceRepoLabelEditable.setText(source.repository)

            for person in source.attachedTo:
                self.sourceAttachedList.addItem(person.name)

    def findSourceFromName(self, name):
        for source in self.mainApp.parsedGedcom.sourcesList:
            if name == source.name:
                return source

        return None

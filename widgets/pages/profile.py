from PyQt6 import QtWidgets, QtCore, QtGui
from widgets.listwidgets import EventListWidget, TwoTextListWidget

class profilePage(QtWidgets.QWidget):
    def __init__(self, ui):
        QtWidgets.QWidget.__init__(self)

        self.ui = ui

        self.setObjectName("profile")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_profile = QtWidgets.QFrame(self)
        self.main_profile.setMinimumSize(QtCore.QSize(0, 300))
        self.main_profile.setStyleSheet("background-color: white;")
        self.main_profile.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_profile.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_profile.setObjectName("main_profile")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_profile)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pictureFrame = QtWidgets.QLabel(self.main_profile)
        self.pictureFrame.setMinimumSize(QtCore.QSize(200, 0))
        self.pictureFrame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.pictureFrame.setStyleSheet("border-style: solid;\n"
                                        "border-width: 1px;\n"
                                        "border-height: 1px;\n"
                                        "border-color: black;")
        self.pictureFrame.setObjectName("pictureFrame")
        self.horizontalLayout.addWidget(self.pictureFrame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.profileOverviewLayout = QtWidgets.QVBoxLayout()
        self.profileOverviewLayout.setSpacing(0)
        self.profileOverviewLayout.setObjectName("profileOverviewLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.profileOverviewLayout.addItem(spacerItem2)
        self.profileName = QtWidgets.QLabel(self.main_profile)
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(24)
        self.profileName.setFont(font)
        self.profileName.setStyleSheet("")
        self.profileName.setObjectName("profileName")
        self.profileOverviewLayout.addWidget(self.profileName)
        self.profileTitles = QtWidgets.QLabel(self.main_profile)
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(24)
        self.profileTitles.setFont(font)
        self.profileTitles.setStyleSheet("")
        self.profileTitles.setObjectName("profileTitles")
        self.profileOverviewLayout.addWidget(self.profileTitles)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.profileOverviewLayout.addItem(spacerItem3)
        self.mainBirthLayout = QtWidgets.QHBoxLayout()
        self.mainBirthLayout.setObjectName("mainBirthLayout")
        self.mainBirthIndicator = QtWidgets.QLabel(self.main_profile)
        self.mainBirthIndicator.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.mainBirthIndicator.setFont(font)
        self.mainBirthIndicator.setStyleSheet("")
        self.mainBirthIndicator.setObjectName("mainBirthIndicator")
        self.mainBirthLayout.addWidget(self.mainBirthIndicator)
        self.mainBirthText = QtWidgets.QLabel(self.main_profile)
        self.mainBirthText.setMinimumSize(QtCore.QSize(500, 0))
        self.mainBirthText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.mainBirthText.setFont(font)
        self.mainBirthText.setStyleSheet("")
        self.mainBirthText.setObjectName("mainBirthText")
        self.mainBirthLayout.addWidget(self.mainBirthText)
        self.profileOverviewLayout.addLayout(self.mainBirthLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Maximum)
        self.profileOverviewLayout.addItem(spacerItem4)
        self.mainDeathLayout = QtWidgets.QHBoxLayout()
        self.mainDeathLayout.setObjectName("mainDeathLayout")
        self.mainDeathIndicator = QtWidgets.QLabel(self.main_profile)
        self.mainDeathIndicator.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.mainDeathIndicator.setFont(font)
        self.mainDeathIndicator.setStyleSheet("")
        self.mainDeathIndicator.setObjectName("mainDeathIndicator")
        self.mainDeathLayout.addWidget(self.mainDeathIndicator)
        self.mainDeathText = QtWidgets.QLabel(self.main_profile)
        self.mainDeathText.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.mainDeathText.setFont(font)
        self.mainDeathText.setStyleSheet("")
        self.mainDeathText.setObjectName("mainDeathText")
        self.mainDeathLayout.addWidget(self.mainDeathText)
        self.profileOverviewLayout.addLayout(self.mainDeathLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.profileOverviewLayout.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.profileOverviewLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Ignored,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_3.addWidget(self.main_profile)
        self.profileTabs = QtWidgets.QTabWidget(self)
        self.profileTabs.setStyleSheet("QTabBar {"
                                       "background-color: #85A09A;\n"
                                       "width: 100"
                                       "}"
                                       "QTabWidget::pane {\n"
                                       "  border: 1px solid black;\n"
                                       "  top:-1px; \n"
                                       "  background: rgb(245, 245, 245);\n"
                                       "} \n"
                                       "\n"
                                       "QTabBar::tab {\n"
                                       "  background: #85A09A;\n"
                                       "  margin-left:30px;\n"
                                       "  margin-right:30px;\n"
                                       "} \n"
                                       "\n"
                                       "QTabBar::tab:selected { \n"
                                       "  background: rgb(230, 230, 230); \n"
                                       "  border: 3px solid rgb(230, 230, 230); \n"
                                       "  padding: 15px;\n"
                                       "  border-radius: 25px;\n"
                                       "  width: 50px;\n"
                                       "}")
        self.profileTabs.setObjectName("profileTabs")
        self.profileEvents = QtWidgets.QWidget()
        self.profileEvents.setObjectName("profileEvents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.profileEvents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.eventsList = QtWidgets.QListWidget(self.profileEvents)
        self.eventsList.setStyleSheet("""QListWidget::item {
                                    background: rgb(255,255,255);\n
                                    }
                                    QListWidget::item:selected
                                    {
                                        background: rgb(128,128,255);})""")

        self.eventsList.setObjectName("eventsList")
        self.horizontalLayout_3.addWidget(self.eventsList)
        self.profileTabs.addTab(self.profileEvents, "")
        self.profileNotes = QtWidgets.QWidget()
        self.profileNotes.setObjectName("profileNotes")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.profileNotes)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.profileNotesList = QtWidgets.QTableWidget(self.profileNotes)
        self.profileNotesList.setObjectName("profileNotesList")
        self.horizontalLayout_5.addWidget(self.profileNotesList)
        self.profileTabs.addTab(self.profileNotes, "")
        self.profileSources = QtWidgets.QWidget()
        self.profileSources.setObjectName("profileSources")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.profileSources)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.profileSourcesList = QtWidgets.QListWidget(self.profileSources)
        self.profileSourcesList.setObjectName("profileSourcesList")
        self.horizontalLayout_6.addWidget(self.profileSourcesList)
        self.pushButton = QtWidgets.QPushButton(self.profileSources)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet("background-color: #697C77;\n"
                                      "border-radius: 25")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon feather-plus.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("../Icons/PNG/Icon feather-plus.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.profileTabs.addTab(self.profileSources, "")
        self.profileLocations = QtWidgets.QWidget()
        self.profileLocations.setObjectName("profileLocations")
        self.profileTabs.addTab(self.profileLocations, "")
        self.profileGallery = QtWidgets.QWidget()
        self.profileGallery.setObjectName("profileGallery")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.profileGallery)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.profileGalleryScroll = QtWidgets.QScrollArea(self.profileGallery)
        self.profileGalleryScroll.setWidgetResizable(True)
        self.profileGalleryScroll.setObjectName("profileGalleryScroll")
        self.profileGalleryScrollContents = QtWidgets.QWidget()
        self.profileGalleryScrollContents.setGeometry(QtCore.QRect(0, 0, 80, 16))
        self.profileGalleryScrollContents.setObjectName("profileGalleryScrollContents")
        self.profileGalleryScroll.setWidget(self.profileGalleryScrollContents)
        self.horizontalLayout_7.addWidget(self.profileGalleryScroll)
        self.profileTabs.addTab(self.profileGallery, "")
        self.profileRelations = QtWidgets.QWidget()
        self.profileRelations.setObjectName("profileRelations")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.profileRelations)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.profileRelationsScroll = QtWidgets.QScrollArea(self.profileRelations)
        self.profileRelationsScroll.setWidgetResizable(True)
        self.profileRelationsScroll.setObjectName("profileRelationsScroll")
        self.profileRelationsScrollContents = QtWidgets.QWidget()
        self.profileRelationsScrollContents.setGeometry(QtCore.QRect(0, 0, 80, 16))
        self.profileRelationsScrollContents.setObjectName("profileRelationsScrollContents")
        self.profileRelationsScroll.setWidget(self.profileRelationsScrollContents)
        self.horizontalLayout_8.addWidget(self.profileRelationsScroll)
        self.profileTabs.addTab(self.profileRelations, "")
        self.verticalLayout_3.addWidget(self.profileTabs)
        self.eventsList.setSpacing(5)
        self.profileSourcesList.setSpacing(5)
        
    def loadProfile(self, person):
        birth, death = None, None

        try:
            if person.birth:
                birth = person.birth[0][0]

            if person.death:
                death = person.death[0][0]

        except IndexError:
            pass

        self.profileName.setText(person.name)
        self.mainBirthText.setText(birth)
        self.mainDeathText.setText(death)

        titles = ""

        for title in person.titles:
            titles.join(f"{title} ")

        self.profileTitles.setText(titles)
        self.ui.GrampsMainPages.setCurrentWidget(self)
        self.loadProfileTabs(person)

    def loadProfileTabs(self, person):
        self.eventsList.clear()
        self.profileSourcesList.clear()
        self.profileNotesList.clear()

        self.profileTabs.setCurrentWidget(self.profileEvents)

        for y in range(len(person.allEvents)):
            event = person.allEvents[y]
            item = QtWidgets.QListWidgetItem()

            if event[5]:
                eventText = event[5]

            else:
                eventText = event[2]

            itemWidget = EventListWidget(event[4], event[0], event[1], eventText)
            item.setSizeHint(itemWidget.sizeHint())

            self.eventsList.addItem(item)
            self.eventsList.setItem  Widget(item, itemWidget)

        for y in range(len(person.notes)):
            note = person.notes[y]
            for x in range(3):
                self.profileNotesList.setItem(y, x, QtWidgets.QTableWidgetItem(note[x]))

        for source in person.sources:
            item = QtWidgets.QListWidgetItem()
            itemWidget = TwoTextListWidget(source.name, source.link)
            self.profileSourcesList.addItem(item)
            self.profileSourcesList.setItemWidget(item, itemWidget)



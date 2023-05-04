from PyQt6 import QtWidgets, QtGui, QtCore

class EventListWidget(QtWidgets.QFrame):
    def __init__(self, type, date, place, text):
        QtWidgets.QFrame.__init__(self)
        self.setMinimumSize(QtCore.QSize(500, 80))
        self.setStyleSheet("QWidget{\n"
                                            "background-color: #85A09A;\n"
                                            "border-radius: 20\n"
                                            "}")
        self.setObjectName("EventsListWidget")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(26, 41, 461, 27))
        self.widget.setObjectName("widget")
        self.infoLayout = QtWidgets.QHBoxLayout(self.widget)
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.infoLayout.setObjectName("infoLayout")
        self.eventItemDateLabel = QtWidgets.QLabel(self.widget)
        self.eventItemDateLabel.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.eventItemDateLabel.setFont(font)
        self.eventItemDateLabel.setStyleSheet("color: white")
        self.eventItemDateLabel.setObjectName("eventItemDateLabel")
        self.infoLayout.addWidget(self.eventItemDateLabel)
        self.eventItemPlaceLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.eventItemPlaceLabel.setFont(font)
        self.eventItemPlaceLabel.setStyleSheet("color: white")
        self.eventItemPlaceLabel.setObjectName("eventItemPlaceLabel")
        self.infoLayout.addWidget(self.eventItemPlaceLabel)
        self.eventItemTextLabel = QtWidgets.QLabel(self)
        self.eventItemTextLabel.setGeometry(QtCore.QRect(26, 74, 461, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.eventItemTextLabel.setFont(font)
        self.eventItemTextLabel.setStyleSheet("color: white")
        self.eventItemTextLabel.setWordWrap(True)
        self.eventItemTextLabel.setObjectName("eventItemTextLabel")
        self.eventItemTypeLabel = QtWidgets.QLabel(self)
        self.eventItemTypeLabel.setGeometry(QtCore.QRect(26, 10, 78, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.eventItemTypeLabel.setFont(font)
        self.eventItemTypeLabel.setStyleSheet("color: white")
        self.eventItemTypeLabel.setObjectName("eventItemTypeLabel")

        self.eventItemTypeLabel.setText(type)
        self.eventItemDateLabel.setText(date)
        self.eventItemPlaceLabel.setText(place)
        self.eventItemTextLabel.setText(text)

        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(2)

        #self.setGraphicsEffect(shadow)

class TwoTextListWidget(QtWidgets.QFrame):
    def __init__(self, textOne, textTwo):
        QtWidgets.QFrame.__init__(self)

        self.setMinimumSize(QtCore.QSize(500, 80))
        self.setStyleSheet("QWidget{\n"
                                             "background-color: #85A09A;\n"
                                             "border-radius: 20\n"
                                             "}")
        self.setObjectName("TwoItemListWidget")
        self.twoItemFirst = QtWidgets.QLabel(self)
        self.twoItemFirst.setGeometry(QtCore.QRect(26, 10, 140, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.twoItemFirst.setFont(font)
        self.twoItemFirst.setStyleSheet("color: white")
        self.twoItemFirst.setObjectName("twoItemFirst")
        self.twoItemSecond = QtWidgets.QLabel(self)
        self.twoItemSecond.setGeometry(QtCore.QRect(26, 44, 464, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.twoItemSecond.setFont(font)
        self.twoItemSecond.setStyleSheet("color: white")
        self.twoItemSecond.setWordWrap(True)
        self.twoItemSecond.setObjectName("twoItemSecond")

        self.twoItemFirst.setText(textOne)
        self.twoItemSecond.setText(textTwo)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    listwidget = QtWidgets.QListWidget()
    widget = EventListWidget('Residence', '1 Jan 1900', 'Uttar Pradesh, India', 'EAH Blunt woke up.')

    for x in range(5):
        item = QtWidgets.QListWidgetItem()
        listwidget.addItem(item)
        listwidget.setItemWidget(item, widget)

    listwidget.show()
    app.exec()

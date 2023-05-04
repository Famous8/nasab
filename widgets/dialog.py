import json

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from pathlib import Path

import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from UI.dialog import Ui_Dialog
from assets.gedcomparser import gedcomParse
from assets.classes import Tree

class Dialog(QDialog):
    def __init__(self, main):
        QDialog.__init__(self)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


        self.mainApp = main
        self.setWindowTitle("Load Tree")

        self.currentTree = None
        self.ui.treesList.itemSelectionChanged.connect(self.setCurrentTree)

        self.ui.importTreeButton.clicked.connect(self.importTree)
        self.ui.removeTreeButton.clicked.connect(lambda: self.removeItem(self.ui.treesList.currentRow(),
                                                                         self.ui.treesList.currentItem()))
        self.ui.addTreeButton.clicked.connect(self.addTree)
        self.ui.loadTreeButton.clicked.connect(self.loadTree)

        self.treesList = []

        self.load()

    def load(self):
        fileContents = open("./assets/data/trees.json").read()
        trees = json.loads(fileContents)

        for tree in trees:
            entry = Tree(**tree)
            self.treesList.append(entry)

        for tree in self.treesList:
            listWidgetItem = QListWidgetItem(tree.name)
            self.ui.treesList.addItem(listWidgetItem)

    def dump(self):
        trees = []

        for tree in self.treesList:
            trees.append(vars(tree))

        trees = json.dumps(trees)

        with open("./assets/data/trees.json", "w") as f:
            f.write(trees)

    def setCurrentTree(self):
        if self.ui.treesList.currentItem():
            name = self.ui.treesList.currentItem().text()
            self.currentTree = (name, self.findTree(name))

    def addTree(self):
        file = QFileDialog.getSaveFileName(self, "Save File", "", "GEDCOM Files(*.ged)")

        if file:
            tree = Tree()

            tree.path = file[0]
            tree.name = Path(tree.path).stem

            if self.findTree(tree.name) is None and file[0]:
                saveFile = open(file[0], "x")
                saveFile.close()

            listWidgetItem = QListWidgetItem(tree.name)
            self.ui.treesList.addItem(listWidgetItem)
            self.treesList.append(tree)

    def importTree(self):
        file = QFileDialog.getOpenFileName(self, "Load File", "", "GEDCOM Files(*.ged)")

        if file:
            tree = Tree()

            tree.path = file[0]
            tree.name = Path(tree.path).stem

            listWidgetItem = QListWidgetItem(tree.name)
            self.ui.treesList.addItem(listWidgetItem)
            self.treesList.append(tree)

    def loadTree(self):
        path = self.currentTree[1].path

        if Path(path).is_file():
            self.ui.progressBar.show()
            self.ui.progressBar.setValue(5)
            self.mainApp.parsedGedcom = gedcomParse(path)
            self.ui.progressBar.setValue(75)

            self.mainApp.load()

            self.ui.progressBar.setValue(100)
            self.ui.progressBar.hide()
            self.close()

        else:
            messagebox = QMessageBox()
            messagebox.setText(f"Error! {path} does not exist. Removing tree from list.")
            messagebox.setWindowTitle("Error")
            messagebox.exec()
            self.removeItem(self.ui.treesList.currentRow(), self.ui.treesList.currentItem())

    def removeItem(self, row, item):
        self.treesList.remove(self.currentTree[1])
        self.ui.treesList.takeItem(row)

        savedTreesFile = open("./assets/data/trees.json", "r")
        savedTrees = json.loads(savedTreesFile.read())

        index = 0

        for tree in savedTrees:
            if tree["name"] == item.text():
                savedTrees.pop(index)

            index += 1

        savedTreesFile = open("./assets/data/trees.json", "w")
        savedTreesFile.write(json.dumps(savedTrees))

    def findTree(self, name):
        for tree in self.treesList:
            if tree.name == name:
                return tree

        return None






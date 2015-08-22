#!/usr/bin/env python
"""This is my doc string.

Keyword arguments:
A -- apple
"""
# Copyright 2015 Austin Fox
# Program is distributed under the terms of the
# GNU General Public License see ./License for more information.

import sys
from PyQt4 import QtCore, QtGui
import sys  # list of comand line argus need to run Gui
import PUT_Gui
import time        # yep importing time that way we can go back to the future


class APP(PUT_Gui.gui):
    """"This Class is used to create the Gui for the PUT_app and
    to controll it."""

# Creat a python signal that will be used to pass app history stuff

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)  # See PUT GUI
        # initialize the serial connections

    def run(self):
        # Set up Button Click and change event refs (Slots)
        self.page0.StartButton.clicked.connect(self.program_start)
        self.page1.StartButton.clicked.connect(self.user_add)
        self.page2.QuitButton.clicked.connect(self.program_close)
        self.page3.StartButton.clicked.connect(self.program_setup)

        self.show()         # show the Gui

# Start the program if password is correct or open admin page
    def program_start(self):
        pass

        txt = str(self.laser_messages.toPlainText())

        self.laser_messages.setPlainText(txt)

# Quit the program
    def program_close(self):
        pass

# Set up program to start and change all shortcuts
    def program_setup(self):
        pass

# Add a User
    def user_add(self):
        pass

# Remove a user after checking admin Password
    def User_rm(self):
        pass

# Chage User Password
    def user_chpass(self):
        pass

# ###            Capture Close and do Stuff          ####
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(
                self, 'Message',
                "Are you sure to quit?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No
                )

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
# start it all up
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = APP()
    # ex.show()
    QtCore.QTimer.singleShot(10, ex.run)
    sys.exit(app.exec_())

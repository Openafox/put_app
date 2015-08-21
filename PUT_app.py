#!/usr/bin/env python
"""This is my doc string.

Keyword arguments:
A -- apple
"""
#Copyright 2015 Austin Fox
#Program is distributed under the terms of the
#GNU General Public License see ./License for more information.

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
        self.page0.StartButton.clicked.connect(self.Program_Start) 

        self.show()         # show the Gui

# Start the program if password is correct or open admin page
    def Program_Start(self):
        pass


        
# ###            Capture Close and do Stuff          ####
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(
                self, 'Message',
                "Are you sure to quit?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No
                )

        if reply == QtGui.QMessageBox.Yes:
            self.motor_cmd("MD")
            self.motor_cmd("QT")
            print "motor done"
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

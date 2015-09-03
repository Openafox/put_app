#!/usr/bin/env python
"""This is my doc string.

Keyword arguments:
A -- apple
"""
# Copyright 2015 Austin Fox
# Program is distributed under the terms of the
# GNU General Public License see ./License for more information.

import pdb
import sys
from PyQt4 import QtCore, QtGui
import sys  # list of comand line argus need to run Gui
import PUT_Gui
import time        # yep importing time that way we can go back to the future
import Pass     # My Password Modul
import subprocess  # running other processes


class APP(PUT_Gui.gui):
    """"This Class is used to create the Gui for the PUT_app and
    to controll it."""

# define globals
    quit = False
    with open("Dest.txt", "r") as data_file:
        dest = data_file.readline()
        print dest
    process = None
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
        self.page4.StartButton.clicked.connect(self.user_rm)
        self.page5.StartButton.clicked.connect(self.user_chpass)
        
        # on page start
        self.stack.currentChanged.connect(self.refresh)

        # 
        self.page0.Box1.currentIndexChanged.connect(lambda: self.user_update(False))
        self.refresh()
        self.show()         # show the Gui

    def refresh(self):
        allusers = Pass.getallusers()

        currentindex = self.page0.Box1.currentIndex()
        self.page0.Box1.blockSignals(True)
        self.page0.Box1.clear()
        self.page0.Box1.addItems(allusers)
        self.page0.Box1.setCurrentIndex(-1)
        self.page0.Box1.blockSignals(False)
        self.page0.Box1.setCurrentIndex(currentindex)
        self.page0.Box2.clear()

        self.page4.Box1.clear()
        self.page4.Box2.clear()
        self.page4.Box3.clear()
        self.page4.Box4.clear()
        self.page4.Box1.addItems(allusers[1:])
        self.page4.Box1.setCurrentIndex(currentindex)

        self.page5.Box1.clear()
        self.page5.Box2.clear()
        self.page5.Box3.clear()
        self.page5.Box4.clear()
        self.page5.Box1.addItems(allusers)
        self.page5.Box1.setCurrentIndex(currentindex)

# Start the program if password is correct or open admin page
    def program_start(self):
        name = str(self.page0.Box1.currentText())
        pass1 = str(self.page0.Box2.text())
        print name
        print pass1
        test = Pass.checkpass(name, pass1)
        if test is True:
            if self.user_checks(name) is True:
                self.user_update(True)
                if name == "Admin":
                    self.stack.setPage(1)
                else:
                    self.page2.Box1.setText(name)
                    self.page2.Box2.setText(time.strftime("%y-%m-%d-%H:%M:%S"))
                    self.page2.Box4.setText("Under Construction")
                    self.stack.setPage(2)
                    self.quit = False
                    self.process = subprocess.Popen([self.dest])
                    self.program_check()
            else:
                return
        else:
            QtGui.QMessageBox.warning(self, "Incorrect username or password!",
                                      test, QtGui.QMessageBox.Ok,
                                      QtGui.QMessageBox.NoButton,
                                      QtGui.QMessageBox.NoButton)

# checking last user logon
    def user_checks(self, name):
        userdata = Pass.getuserdata(name, False)
        index = str(self.page0.Box3.text())
        if index == "index":
            QtGui.QMessageBox.warning(self, "Index.",
                                  "You must supply a valid billing index to "\
                                  "use the instrument.<br>Cost is $30/hr for"\
                                  " internal users.", QtGui.QMessageBox.Ok,
                                  QtGui.QMessageBox.NoButton,
                                  QtGui.QMessageBox.NoButton)
            self.page0.Box2.clear()
            return
        date = time.mktime(time.strptime(userdata[4],"%y-%m-%d-%H:%M"))
        month = 30*24*60*60
        duration = time.time() - date
        if duration > month * 12:
            mess = "You have not used the instrument for Greater than 1 year!"\
                   "<br>Your account has been suspended." \
                   "<br>Please contact the XRD Manager to reactivate your"\
                   " account pending training."
            out = False
        elif duration > month * 6:
            mess = "You have not used the instrument for Greater than 6 "\
                   "months!<br>If you at all feel unconfortable using the "\
                   "instrument. Please contact the XRD Manager"\
                   " for assistance.<br>Do not break me! I will cut you!"
            out = True
        else:
            return True
        QtGui.QMessageBox.warning(self, "Infrequent Instrument Use.",
                                  mess, QtGui.QMessageBox.Ok,
                                  QtGui.QMessageBox.NoButton,
                                  QtGui.QMessageBox.NoButton)
        self.page0.Box2.clear()
        return out

# Update user information when name selected
    def user_update(self, update):
        name = str(self.page0.Box1.currentText())
        if update is True:
            userdata = Pass.getuserdata(name, True)
            userdata[3] = str(self.page0.Box3.text())  # index
            userdata[2] = str(self.page0.Box4.text())  # advisor
            userdata[5] = str(self.page0.Box5.text())  # email
            userdata[4] = time.strftime("%y-%m-%d-%H:%M")  # lastlogin
            Pass.userup(userdata)
        else:
            userdata = Pass.getuserdata(name, False)
            self.page0.Box3.setText(userdata[3])
            self.page0.Box4.setText(userdata[2])
            self.page0.Box5.setText(userdata[5])  # email
            self.page0.Box2.setText("")
            self.page0.Box2.setFocus()



# Check if program is running
    def program_check(self):
        if self.process.poll() != None:
            self.quit = True
        if self.quit is False:
            start = time.mktime(time.strptime(self.page2.Box2.text(),
                                "%y-%m-%d-%H:%M:%S"))
            print start
            diff = time.time() - start
            print diff
            self.page2.Box3.setText(time.strftime("%H:%M:%S",
                                                  time.gmtime(diff)))
            QtCore.QTimer.singleShot(5000, self.program_check)
        else:
            self.stack.setPage(0)


# Quit the program
    def program_close(self):
        self.quit = True
        self.stack.setPage(0)
        self.process.terminate()

# Set up program to start and change all shortcuts
    def program_setup(self):
        pass

# Add a User
    def user_add(self):
        name = str(self.page1.Box1.text())
        pass1 = str(self.page1.Box2.text())
        pass2 = str(self.page1.Box3.text())
        advisor = str(self.page1.Box4.text())
        email = str(self.page1.Box5.text())
        mess = Pass.Addusr(name, pass1, pass2, advisor, email)
        QtGui.QMessageBox.warning(self, "Adding User", mess,
                                  QtGui.QMessageBox.Ok,
                                  QtGui.QMessageBox.NoButton,
                                  QtGui.QMessageBox.NoButton)
        self.page1.Box1.clear()
        self.page1.Box2.clear()
        self.page1.Box3.clear()
        self.page1.Box4.clear()
        self.page1.Box5.clear()

# Remove a user after checking admin Password
    def user_rm(self):
        pass1 = self.page4.Box2.text()
        mess = Pass.checkpass("Admin", pass1)
        if mess:
            name = str(self.page4.Box1.currentText())
            print name
            Pass.getuserdata(name)
        else:
            QtGui.QMessageBox.warning(self, "Adding User", mess,
                                      QtGui.QMessageBox.Ok,
                                      QtGui.QMessageBox.NoButton,
                                      QtGui.QMessageBox.NoButton)

# Chage User Password
    def user_chpass(self):
        name = str(self.page5.Box1.currentText())
        oldpass = str(self.page5.Box2.text())
        pass1 = str(self.page5.Box3.text())
        pass2 = str(self.page5.Box4.text())
        mess = Pass.changepass(name, oldpass, pass1, pass2)
        QtGui.QMessageBox.warning(self, "Change Password", mess,
                                  QtGui.QMessageBox.Ok,
                                  QtGui.QMessageBox.NoButton,
                                  QtGui.QMessageBox.NoButton)
        if mess[0:3] == "Suc":
            self.stack.setPage(0)

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

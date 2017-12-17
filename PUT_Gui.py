# -*- coding: utf-8 -*-

# 'LogOnGui.py'
#
# Created: Sat Feb 28 21:00:21 2015
#      by: Austin Fox#
# GPL


from PyQt4 import QtCore, QtGui
import sys  # list of comand line argus need to run Gui
# ####################################################
# Try Encoding (Error prevention)
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
# ####################################################

# Set Up Fonts
# Normal font
font_N = QtGui.QFont()
font_N.setFamily(_fromUtf8("Georgia"))
font_N.setPointSize(14)
# Lable Font
font_L = QtGui.QFont()
font_L.setFamily(_fromUtf8("Georgia"))
font_L.setPointSize(18)
# Bold Font
font_B = QtGui.QFont()
font_B.setFamily(_fromUtf8("Georgia"))
font_B.setPointSize(18)
# Greyed Box Style
styl = "Background-color: transparent; color: black; "\
       "border-style: ridge; border-width: 1px; border-color: grey;"

QtGui.QToolTip.setFont(QtGui.QFont('Georgia', 12))  # set the font


# #####################################################
# Setup Main Window
class gui(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        # could also use 'super(gui, self).__init__()' calls the parent class

        self.setupUi(self)  # make the UI  See Bellow

    def setupUi(self, MainWindow):

        # System Checks.  Avoid errors!!
        if sys.platform == "darwin":  # check if you are on a mac
            QtGui.qt_mac_set_native_menubar(False)  # disable native menues

# Set Up Widget(Form)
        # set up size policy
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                MainWindow.sizePolicy().hasHeightForWidth())

        # Setup Main Window
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setMaximumSize(100, 100)  # height, width
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle("Program Log On")
        MainWindow.center()
        # MainWindow.setWindowIcon(QtGui.QIcon('web.png'))
        # does not work may be interesting to get to work tho

        # central widget
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

    # Notes Box
        # Box
        self.Note = QtGui.QTextEdit()
        self.Note.setFont(font_N)
        self.Note.setMaximumHeight(70)
        self.Note.setToolTip("Please Add/Delete Notes for other users here.")
        # Label
        self.NoteLabel = QtGui.QLabel()
        self.NoteLabel.setText("Notes:")
        self.NoteLabel.setFont(font_L)

    # Page Buttons #for testing#
        # page0Button = QtGui.QPushButton("Page 0")
        # page1Button = QtGui.QPushButton("Page 1")
        # page2Button = QtGui.QPushButton("Page 2")
        # page3Button = QtGui.QPushButton("Page 3")
        # page4Button = QtGui.QPushButton("Page 4")

# Setup Layout
# bring in other class widgets
        self.stack = StackedWidget()
        self.page0 = Page0()
        self.page1 = Page1()
        self.page2 = Page2()
        self.page3 = Page3()
        self.page4 = Page4()
        self.page5 = Page5()
    # Set up stack
        self.stack.addWidget(self.page0)
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)
        self.stack.addWidget(self.page4)
        self.stack.addWidget(self.page5)

    # create layout Horizontal test buttons
        # self.layoutH = QtGui.QHBoxLayout()
        # self.layoutH.addWidget(page0Button)
        # self.layoutH.addWidget(page1Button)
        # self.layoutH.addWidget(page2Button)
        # self.layoutH.addWidget(page3Button)
        # self.layoutH.addWidget(page4Button)

    # create vertical layout
        self.layoutV = QtGui.QVBoxLayout(self.centralwidget)
        self.layoutV.addWidget(self.stack)
        self.layoutV.addWidget(self.NoteLabel)
        self.layoutV.addWidget(self.Note)
        # self.layoutV.addLayout(self.layoutH)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        # Button Actions #for testing#
        # self.page0.StartButton.clicked.connect(lambda: self.stack.setPage(1))
        # page0Button.clicked.connect(lambda: self.stack.setPage(0))
        # page1Button.clicked.connect(lambda: self.stack.setPage(1))
        # page2Button.clicked.connect(lambda: self.stack.setPage(2))
        # page3Button.clicked.connect(lambda: self.stack.setPage(3))
        # page4Button.clicked.connect(lambda: self.stack.setPage(4))
        # All Buttons
        self.page1.QuitButton.clicked.connect(lambda: self.stack.setPage(0))
        self.page5.QuitButton.clicked.connect(lambda: self.stack.setPage(0))

        self.page0.st_prog.triggered.connect(lambda: self.stack.setPage(0))
        self.page0.ch_pass.triggered.connect(lambda: self.stack.setPage(5))

        self.page5.st_prog.triggered.connect(lambda: self.stack.setPage(0))
        self.page5.ch_pass.triggered.connect(lambda: self.stack.setPage(5))

        self.page1.LogOut.triggered.connect(lambda: self.stack.setPage(0))
        self.page1.add_user.triggered.connect(lambda: self.stack.setPage(1))
        self.page1.rm_user.triggered.connect(lambda: self.stack.setPage(4))
        self.page1.Prog.triggered.connect(lambda: self.stack.setPage(3))
        self.page3.LogOut.triggered.connect(lambda: self.stack.setPage(0))
        self.page3.add_user.triggered.connect(lambda: self.stack.setPage(1))
        self.page3.rm_user.triggered.connect(lambda: self.stack.setPage(4))
        self.page3.Prog.triggered.connect(lambda: self.stack.setPage(3))
        self.page4.LogOut.triggered.connect(lambda: self.stack.setPage(0))
        self.page4.add_user.triggered.connect(lambda: self.stack.setPage(1))
        self.page4.rm_user.triggered.connect(lambda: self.stack.setPage(4))
        self.page4.Prog.triggered.connect(lambda: self.stack.setPage(3))


    def center(self):

        qr = self.frameGeometry()  # rectangle of self
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)  # center our rectangle in the screen
        self.move(qr.topLeft())  # use top left point


# ###################################################
# Setup Page (LogOn)
class Pagesetup(QtGui.QWidget):
    def __init__(self):
        super(Pagesetup, self).__init__()
        self.setupUi()  # make the UI  See Bellow

# Setup page 1 (Log On)
    def setupUi(self):
        self.Title = QtGui.QLabel()
        self.Title.setFont(font_B)
        self.Title.setAlignment(QtCore.Qt.AlignCenter |
                                QtCore.Qt.AlignVCenter)
        # User Name
        self.Box1 = QtGui.QComboBox()
        self.Box1.setEditable(True)
        self.Label1 = QtGui.QLabel()
        self.Label1.setText(_fromUtf8("User Name:"))
        self.Label1.setFont(font_L)
        # Password
        self.Box2 = QtGui.QLineEdit()
        self.Box2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Box2.setEchoMode(QtGui.QLineEdit.Password)
        self.Label2 = QtGui.QLabel()
        self.Label2.setText(_fromUtf8("Password:"))
        self.Label2.setFont(font_L)
        # Index, Password Repeat
        self.Box3 = QtGui.QLineEdit()
        self.Box3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Label3 = QtGui.QLabel()
        self.Label3.setText(_fromUtf8("Index:"))
        self.Label3.setFont(font_L)
        # Adviser
        self.Box4 = QtGui.QLineEdit()
        self.Box4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Label4 = QtGui.QLabel()
        self.Label4.setText(_fromUtf8("Adviser:"))
        self.Label4.setFont(font_L)
        # Email
        self.Box5 = QtGui.QLineEdit()
        self.Box5.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Label5 = QtGui.QLabel()
        self.Label5.setText(_fromUtf8("Email:"))
        self.Label5.setFont(font_L)

    # Setup Buttons
        # Start, Add Button
        self.StartButton = QtGui.QPushButton("Start")
        self.StartButton.resize(100, 60)
        self.StartButton.setFont(font_B)
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartButton.setAutoDefault(True)

        # Quit Button
        self.QuitButton = QtGui.QPushButton("Quit")
        self.QuitButton.resize(100, 60)
        self.QuitButton.setFont(font_B)
        self.QuitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

# Set up Menu items for Admin
        self.add_user = QtGui.QAction(QtGui.QIcon('img/add_user.png'),
                                      'Add User', self)  # set up the action
        # add_user.setShortcut('Ctrl+Q')    #give it a shortcut
        # add_user.setStatusTip('Exit application') #Status tip

        self.rm_user = QtGui.QAction(QtGui.QIcon('img/remove_user.png'),
                                     'Remove User', self)  # set up the action
        # add_user.setShortcut('Ctrl+Q')    #give it a shortcut
        # add_user.setStatusTip('Exit application') #Status tip

        self.Prog = QtGui.QAction(QtGui.QIcon('img/program.png'),
                                  'Prog Setup', self)  # set up the action
        # add_user.setShortcut('Ctrl+Q')    #give it a shortcut
        # add_user.setStatusTip('Exit application') #Status tip

        self.LogOut = QtGui.QAction(QtGui.QIcon('img/sign_out.png'),
                                    'Log Out', self)  # set up the action
        self.LogOut.setShortcut('Ctrl+Q')    # give it a shortcut
        self.LogOut.setStatusTip('Exit Admin Session')  # Status tip
    # Setup Menu Bar
        self.menu = QtGui.QMenuBar()
        self.fileMenu = self.menu.addMenu('&Menu')
        self.fileMenu.addAction(self.add_user)
        self.fileMenu.addAction(self.rm_user)
        self.fileMenu.addAction(self.Prog)
        self.fileMenu.addAction(self.LogOut)


# ####################################################
# Setup Page0 (Logon)
class Page0(Pagesetup):
    def __init__(self):
        super(Page0, self).__init__()
        self.setupUiedits()
        self.initUi()

    def setupUiedits(self):
        self.Title.setText(_fromUtf8("Log On"))
        self.Box1.setToolTip('Please select your name')
        self.Box2.setToolTip('Please input your password')
        self.Box3.setToolTip('Please input the index code you would like to '
                             'bill. \n Use of this instrument is $30 per hour'
                             ' for internal users')
        # self.Box4.setToolTip('Please add notes here for all users to see')

# Set up Menu items
        self.st_prog= QtGui.QAction(QtGui.QIcon('img/program.png'),
                                    'Main', self)  # set up the action
        # add_user.setShortcut('Ctrl+Q')    #give it a shortcut
        # add_user.setStatusTip('Exit application') #Status tip

        self.ch_pass = QtGui.QAction(QtGui.QIcon('img/add_user.png'),
                                     'Change Password', self)
        # add_user.setShortcut('Ctrl+Q')    #give it a shortcut
        # add_user.setStatusTip('Exit application') #Status tip
    # Setup Menu Bar
        self.menu = QtGui.QMenuBar()
        self.fileMenu = self.menu.addMenu('&Menu')
        self.fileMenu.addAction(self.st_prog)
        self.fileMenu.addAction(self.ch_pass)

    def initUi(self):
        # Setup Form
        self.FormLayout = QtGui.QFormLayout()
        self.FormLayout.addRow(self.Label1, self.Box1)
        self.FormLayout.addRow(self.Label2, self.Box2)
        self.FormLayout.addRow(self.Label3, self.Box3)
        self.FormLayout.addRow(self.Label4, self.Box4)
        self.FormLayout.addRow(self.Label5, self.Box5)

    # Setup Vertical Box Layout
        self.vbox = QtGui.QVBoxLayout()
        # add Layouts
        self.vbox.addWidget(self.menu)
        self.vbox.addWidget(self.Title)
        self.vbox.addLayout(self.FormLayout)
        self.vbox.addWidget(self.StartButton)

    # Finish Page Setup
        self.setLayout(self.vbox)


# ###################################################
# Setup Page1 (Add User)
class Page1(Pagesetup):
    def __init__(self):
        super(Page1, self).__init__()
        self.setupUiedits()
        self.initUi()

    def setupUiedits(self):
        self.Title.setText(_fromUtf8("Add User"))
        self.Box1.setToolTip('Please use your full name as'
                             'on your student ID.')
        self.Box2.setToolTip('Please select a unique Password.<br>'
                             'Passwords are hashed and realitivly secure.<br>'
                             '<b>Do Not share your Password with anyone!</b>')
        self.Box3.setToolTip('Please repeat your Password.')
        self.Box4.setToolTip('Please input your PI\'s first and last name')

        self.Box1 = QtGui.QLineEdit()
        self.Label3.setText(_fromUtf8("Repeat Password:"))
        self.Box3.setEchoMode(QtGui.QLineEdit.Password)

        self.StartButton.setText("Add User")
        self.QuitButton.setText("Cancel")

    def initUi(self):
        # Setup Form
        self.FormLayout = QtGui.QFormLayout()
        self.FormLayout.addRow(self.Label1, self.Box1)
        self.FormLayout.addRow(self.Label2, self.Box2)
        self.FormLayout.addRow(self.Label3, self.Box3)
        self.FormLayout.addRow(self.Label4, self.Box4)
        self.FormLayout.addRow(self.Label5, self.Box5)

        # Buttons (horisontal box)
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.StartButton)
        self.hbox.addWidget(self.QuitButton)

    # Setup Vertical Box Layout
        self.vbox = QtGui.QVBoxLayout()
        # add Layouts
        self.vbox.addWidget(self.menu)
        self.vbox.addWidget(self.Title)
        self.vbox.addLayout(self.FormLayout)
        self.vbox.addLayout(self.hbox)
    # Finish Page Setup
        self.setLayout(self.vbox)


# ####################################################
# Setup Page2 (Logged-On User)
class Page2(Pagesetup):
    def __init__(self):
        super(Page2, self).__init__()
        self.setupUiedits()
        self.initUi()

    def setupUiedits(self):
        self.Title.setText(_fromUtf8("Active"))

        # username
        self.Box1 = QtGui.QLineEdit()
        self.Box1.setReadOnly(True)
        self.Box1.setStyleSheet(styl)
        # Start Time
        self.Label2.setText(_fromUtf8("Start Time:"))
        self.Box2.setReadOnly(True)
        self.Box2.setEchoMode(QtGui.QLineEdit.Normal)
        self.Box2.setStyleSheet(styl)
        # Total time
        self.Label3.setText(_fromUtf8("Total Time Today:"))
        self.Box3.setReadOnly(True)
        self.Box3.setStyleSheet(styl)
        # Tolal Time this Month
        self.Label4.setText(_fromUtf8("Total Time This Month:"))
        self.Box4.setReadOnly(True)
        self.Box4.setStyleSheet(styl)

        # Button
        self.QuitButton.setText("Quit")

    def initUi(self):
        # Setup Form
        self.FormLayout = QtGui.QFormLayout()
        self.FormLayout.addRow(self.Label1, self.Box1)
        self.FormLayout.addRow(self.Label2, self.Box2)
        self.FormLayout.addRow(self.Label3, self.Box3)
        self.FormLayout.addRow(self.Label4, self.Box4)

        # Buttons (horisontal box)
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.QuitButton)

    # Setup Vertical Box Layout
        self.vbox = QtGui.QVBoxLayout()
        # add Layouts
        self.vbox.addWidget(self.Title)
        self.vbox.addLayout(self.FormLayout)
        self.vbox.addLayout(self.hbox)
    # Finish Page Setup
        self.setLayout(self.vbox)


# ###################################################
# Setup Page3 (Program to run setup)
class Page3(Pagesetup):
    def __init__(self):
        super(Page3, self).__init__()
        self.setupUiedits()
        self.initUi()

    def setupUiedits(self):
        self.Title.setText(_fromUtf8("Program Setup"))

        # Program
        self.Box1 = QtGui.QLineEdit()
        self.Label1.setText(_fromUtf8("Program Path"))
        self.Box1.setReadOnly(True)
        self.Box1.setStyleSheet(styl)

        self.ChButton = QtGui.QPushButton("Change Shortcuts")
        self.ChButton.resize(100, 60)
        self.ChButton.setFont(font_B)
        self.ChButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.StartButton.setText("Change Program")
        self.QuitButton.setText("Revert Shortcuts")

    def initUi(self):
        # Buttons (horisontal box)
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.ChButton)
        self.hbox.addWidget(self.QuitButton)

    # Setup Vertical Box Layout
        self.vbox = QtGui.QVBoxLayout()
        # add Layouts
        self.vbox.addWidget(self.menu)
        self.vbox.addWidget(self.Title)
        self.vbox.addWidget(self.Label1)
        self.vbox.addWidget(self.Box1)
        self.vbox.addWidget(self.StartButton)
        self.vbox.addLayout(self.hbox)
    # Finish Page Setup
        self.setLayout(self.vbox)


# ####################################################
# Setup Page4 (Remove User)
class Page4(Pagesetup):
    def __init__(self):
        super(Page4, self).__init__()
        self.setupUiedits()
        self.initUi()

    def setupUiedits(self):
        self.Title.setText(_fromUtf8("Remove User"))
        self.Box1.setToolTip('Please select user to remove')
        self.Box2.setToolTip('Please input admin password')
        self.Label2.setText(_fromUtf8("Admin Password:"))

    def initUi(self):
        # Setup Form
        self.FormLayout = QtGui.QFormLayout()
        self.FormLayout.addRow(self.Label1, self.Box1)
        self.FormLayout.addRow(self.Label2, self.Box2)
        self.StartButton.setText("Remove User")

        # Buttons (horizontal box)
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.StartButton)
        # self.hbox.addWidget(self.QuitButton)
    # Setup Vertical Box Layout
        self.vbox = QtGui.QVBoxLayout()
        # add Layouts
        self.vbox.addWidget(self.menu)
        self.vbox.addWidget(self.Title)
        self.vbox.addLayout(self.FormLayout)
        self.vbox.addLayout(self.hbox)

    # Finish Page Setup
        self.setLayout(self.vbox)


# ###################################################
# Setup Page5 (Change Password)
class Page5(Pagesetup):
    def __init__(self):
        super(Page5, self).__init__()
        self.setupUiedits()
        self.initUi()

    def setupUiedits(self):
        self.Title.setText(_fromUtf8("Change Password"))
        self.Box1.setToolTip('Select User Name')
        self.Box3.setToolTip('Please select a unique Password.<br>'
                             'Passwords are hashed and realitivly secure.<br>'
                             '<b>Do Not share your Password with anyone!</b>')
        self.Box4.setToolTip('Please repeat your Password.')

        self.Label2.setText(_fromUtf8("Old Password:"))
        self.Label3.setText(_fromUtf8("New Password:"))
        self.Label4.setText(_fromUtf8("Repeat Password:"))
        self.Box3.setEchoMode(QtGui.QLineEdit.Password)
        self.Box4.setEchoMode(QtGui.QLineEdit.Password)

        self.StartButton.setText("Submit")
        self.QuitButton.setText("Cancel")

# Set up Menu items
        self.st_prog= QtGui.QAction(QtGui.QIcon('img/program.png'),
                                    'Main', self)  # set up the action
        # add_user.setShortcut('Ctrl+Q')    #give it a shortcut
        # add_user.setStatusTip('Exit application') #Status tip

        self.ch_pass = QtGui.QAction(QtGui.QIcon('img/add_user.png'),
                                     'Change Password', self)
        # add_user.setShortcut('Ctrl+Q')    #give it a shortcut
        # add_user.setStatusTip('Exit application') #Status tip
    # Setup Menu Bar
        self.menu = QtGui.QMenuBar()
        self.fileMenu = self.menu.addMenu('&Menu')
        self.fileMenu.addAction(self.st_prog)
        self.fileMenu.addAction(self.ch_pass)

    def initUi(self):
        # Setup Form
        self.FormLayout = QtGui.QFormLayout()
        self.FormLayout.addRow(self.Label1, self.Box1)
        self.FormLayout.addRow(self.Label2, self.Box2)
        self.FormLayout.addRow(self.Label3, self.Box3)
        self.FormLayout.addRow(self.Label4, self.Box4)

        # Buttons (horisontal box)
        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addWidget(self.StartButton)
        self.hbox.addWidget(self.QuitButton)

    # Setup Vertical Box Layout
        self.vbox = QtGui.QVBoxLayout()
        # add Layouts
        self.vbox.addWidget(self.menu)
        self.vbox.addWidget(self.Title)
        self.vbox.addLayout(self.FormLayout)
        self.vbox.addLayout(self.hbox)
    # Finish Page Setup
        self.setLayout(self.vbox)


# ####################################################
# Setup for fading between 'stacked' widgets.
class FaderWidget(QtGui.QWidget):

    def __init__(self, old_widget, new_widget):
        # print old_widget, new_widget #for debug
        QtGui.QWidget.__init__(self, new_widget)

        self.old_pixmap = QtGui.QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)
        self.pixmap_opacity = 1.0

        self.timeline = QtCore.QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(333)
        self.timeline.start()

        self.resize(new_widget.size())
        self.show()

    def paintEvent(self, event):

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()

    def animate(self, value):

        self.pixmap_opacity = 1.0 - value
        self.repaint()


class StackedWidget(QtGui.QStackedWidget):

    def __init__(self, parent=None):
        QtGui.QStackedWidget.__init__(self, parent)

    def setCurrentIndex(self, index):
        self.fader_widget = FaderWidget(self.currentWidget(),
                                        self.widget(index))
        QtGui.QStackedWidget.setCurrentIndex(self, index)

    def setPage(self, index=0):
        self.setCurrentIndex(index)


def run():

    app = QtGui.QApplication(sys.argv)
    ex = gui()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()

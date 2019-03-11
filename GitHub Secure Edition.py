# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/rohan/FinalLight.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import datetime, random, string, platform
from json import load, dump, dumps

from PyQt5 import QtCore, QtGui, QtWidgets
from pycronofy import *
from apscheduler.schedulers.background import BackgroundScheduler



import datetime
from pycronofy import *
from json import *
from PyQt5 import QtCore, QtGui, QtWidgets





scheduler=BackgroundScheduler()
crono_cal = Client (access_token="Get your own from cronofy.")

listofsubjects = ["English", "Math", "Languages",
                  "Business", "Economics", "Geography", "History", "Psychology",
                  "Biology", "Chemistry", "Physics", "Computers", "Sports Science",
                  "Film", "Music", "Theatre", "Art"]

subjectgroups = {'english': ["English"],
                 'math': ["Math"],
                 'foreignlanguage': ["Languages"],
                 'humanities': ["Business", "Economics", "Geography", "History", "Psychology"],
                 'sciences': ["Biology", "Chemistry", "Physics", "Computers", "Sports Science"],
                 'extras': ["Film", "Music", "Theatre", "Art"]}

# Colour coding lookup table
colourdictionary_light = {  # TODO: Darker versions of colours (for calendar)
    'english': '#66b3ff',  # Blue
    'math': '#9999ff',  # Light purple
    'foreignlanguage': '#e3cd4f',  # Yellow
    'sciences': '#91bc8f',  # Green
    'humanities': '#fc9b1d',  # Orange
    'extras': '#ff8084',  # Red

}

cal_id="Put your cronofy cal id here"


def daysBetween(date2):
    one_day = 1000 * 60 * 60 * 24
    date1_ms = datetime.datetime.now ().date ()
    date2_ms = date2
    difference_delta = date2_ms - date1_ms  # returns a timedelta object
    difference_ms = difference_delta.total_seconds () * 1000
    return round (difference_ms / one_day)


def datefromiso(datestring):
    return datestring.split ('T', 1)[0]


def randomiser_for_ids():
    numbers = [str (i) for i in range (0, 10)]
    ASCII = list (string.ascii_letters) + numbers * 2
    random_id = [random.choice (ASCII) for i in range (0, 10)]
    return ''.join (random_id)

def writetoJSON(dictobj,file='memory.json',):
    with open (file, mode='r+') as memory:
        s = memory.read ().replace (']', '')
        memory.seek (0)
        memory.truncate ()
        memory.write (s)
        # Leaves an unclosed parentheses

    with open (file, mode="a") as memory:
        memory.write (', \n')
        dump (dictobj, memory, indent=3)
        memory.write (']')
        # Closes that parentheses


def stylehandler(self):
    with open('theme.json', mode='r') as memory:
        s = load(memory)
    if s["darktheme"]:
        self.setdarktheme()
        theme = '''{"darktheme":true}'''
    else:
        self.setlighttheme()
        theme = '''{"darktheme":false}'''


def setdarktheme(self):
     with open ('dark.qss','r') as theme:
        self.MainWindow.setStyleSheet(theme.read())


def setlighttheme(self):
    with open ('light.qss','r') as theme:
        self.MainWindow.setStyleSheet(theme.read())


if platform.system == "Linux":
    import notify2
    notify2.init('App Name')
    def notification(title, text,icon=None):
        n=notify2.Notification(title, text,icon)

if platform.system == "Windows":
    from win10toast import ToastNotifier
    toaster=ToastNotifier()
    def notification(title, text,icon=None):
        toaster.show_toast(title, text, icon_path=icon, threaded=True)
        print('You have no taste')

if platform.system() == "Darwin":
    import applescript
    def notification(title, text,icon=None):
        command= 'display notification '+'\"'+text+'\"'
        applescript.run(command, background=True)


class Ui_MainWindow (QtWidgets.QMainWindow):
    def __init__(self, MainWindow, parent=None):
        super (QtWidgets.QMainWindow, self).__init__ (parent)
        MainWindow.setObjectName ("MainWindow")
        MainWindow.resize (656, 581)
        self.MainWindow = MainWindow

        self.centralWidget = QtWidgets.QWidget (MainWindow)
        self.centralWidget.setObjectName ("centralWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget (self.centralWidget)
        self.verticalLayoutWidget.setGeometry (QtCore.QRect (9, 10, 271, 435))
        self.verticalLayoutWidget.setObjectName ("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout (self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint (QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins (11, 11, 11, 11)
        self.verticalLayout.setSpacing (6)
        self.verticalLayout.setObjectName ("verticalLayout")
        self.todaybutton = QtWidgets.QPushButton (self.verticalLayoutWidget)
        self.todaybutton.setMinimumSize (QtCore.QSize (0, 0))
        self.todaybutton.setMaximumSize (QtCore.QSize (16777215, 50))

        self.todaybutton.setObjectName ("todaybutton")
        self.verticalLayout.addWidget (self.todaybutton)
        self.weekbutton = QtWidgets.QPushButton (self.verticalLayoutWidget)
        self.weekbutton.setMinimumSize (QtCore.QSize (0, 0))
        self.weekbutton.setMaximumSize (QtCore.QSize (16777215, 50))

        self.weekbutton.setObjectName ("weekbutton")
        self.verticalLayout.addWidget (self.weekbutton)
        self.eventlist = QtWidgets.QListWidget (self.verticalLayoutWidget)
        self.eventlist.setMaximumSize (QtCore.QSize (16777215, 270))
        self.eventlist.setWordWrap (True)
        self.eventlist.setObjectName ("eventlist")
        item = QtWidgets.QListWidgetItem ()
        font = QtGui.QFont ()
        font.setPointSize (15)
        font.setBold (True)
        font.setItalic (True)
        font.setWeight (75)
        item.setFont (font)
        self.eventlist.addItem (item)
        self.verticalLayout.addWidget (self.eventlist)
        self.calendarbutton = QtWidgets.QPushButton (self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy (QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch (0)
        sizePolicy.setVerticalStretch (0)
        sizePolicy.setHeightForWidth (self.calendarbutton.sizePolicy ().hasHeightForWidth ())
        self.calendarbutton.setSizePolicy (sizePolicy)
        self.calendarbutton.setMinimumSize (QtCore.QSize (0, 45))
        self.calendarbutton.setObjectName ("calendarbutton")
        self.verticalLayout.addWidget (self.calendarbutton)
        self.newexambutton = QtWidgets.QPushButton (self.centralWidget)
        self.newexambutton.setGeometry (QtCore.QRect (480, 20, 161, 31))
        self.newexambutton.setMaximumSize (QtCore.QSize (200, 16777215))
        self.newexambutton.setObjectName ("newexambutton")
        self.label_4 = QtWidgets.QLabel (self.centralWidget)
        self.label_4.setGeometry (QtCore.QRect (320, 30, 91, 51))
        self.label_4.setTextFormat (QtCore.Qt.RichText)
        self.label_4.setObjectName ("label_4")
        self.gridlayout = QtWidgets.QWidget (self.centralWidget)
        self.gridlayout.setGeometry (QtCore.QRect (290, 80, 361, 361))
        self.gridlayout.setObjectName ("gridlayout")
        self.gridLayout = QtWidgets.QGridLayout (self.gridlayout)
        self.gridLayout.setContentsMargins (11, 11, 11, 11)
        self.gridLayout.setSpacing (6)
        self.gridLayout.setObjectName ("gridLayout")
        self.changemodebutton = QtWidgets.QPushButton (self.centralWidget)
        self.changemodebutton.setGeometry (475, 450, 165, 40)
        self.changemodebutton.setText ("Change Color Scheme")
        # self.changemodebutton.setStyleSheet("color:white;")
        self.newsessionbutton = QtWidgets.QPushButton (self.centralWidget)
        self.newsessionbutton.setGeometry (QtCore.QRect (478, 70, 161, 31))
        self.newsessionbutton.setMaximumSize (QtCore.QSize (200, 16777215))
        self.newsessionbutton.setObjectName ("newsessionbutton")
        MainWindow.setCentralWidget (self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar (MainWindow)
        self.menuBar.setGeometry (QtCore.QRect (0, 0, 656, 22))
        self.menuBar.setObjectName ("menuBar")
        MainWindow.setMenuBar (self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar (MainWindow)
        self.mainToolBar.setObjectName ("mainToolBar")
        MainWindow.addToolBar (QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar (MainWindow)
        self.statusBar.setObjectName ("statusBar")
        MainWindow.setStatusBar (self.statusBar)
        # Function calls

        self.todaybutton.clicked.connect (lambda: self.displaycheckboxestoday ('memory.json'))
        self.weekbutton.clicked.connect ((lambda: self.displaycheckboxesweek ('memory.json')))
        self.newsessionbutton.clicked.connect (lambda: self.createsessionform ())
        self.changemodebutton.clicked.connect (lambda: self.changetheme ())
        self.newexambutton.clicked.connect (lambda: self.createform ())
        self.calendarbutton.clicked.connect (lambda: self.showcalendar ())
        QtCore.QMetaObject.connectSlotsByName (MainWindow)
        with open ('theme.json', mode='r') as memory:
            s = load (memory)
            if s["darktheme"]:
                self.setdarktheme ()
                theme = '''{"darktheme":true}'''
                #self.darktheme=True
            else:
                self.setlighttheme ()
                theme = '''{"darktheme":false}'''
                #self.darktheme=False
        with open ('theme.json', mode='w') as memory:
            memory.write (theme)
        self.retranslateUi (MainWindow)
        self.listfrommemory ('memory.json')
        self.displaycheckboxestoday ('memory.json')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle (_translate ("MainWindow", "MainWindow"))
        self.todaybutton.setAccessibleName (_translate ("MainWindow", "todaybutton"))
        self.todaybutton.setText (_translate ("MainWindow", "Today"))
        self.weekbutton.setAccessibleName (_translate ("MainWindow", "weekbutton"))
        self.weekbutton.setText (_translate ("MainWindow", "Next 7 Days"))
        self.eventlist.setAccessibleName (_translate ("MainWindow", "eventlist"))
        __sortingEnabled = self.eventlist.isSortingEnabled ()
        self.eventlist.setSortingEnabled (False)
        item = self.eventlist.item (0)
        item.setText (_translate ("MainWindow", "All Deadlines"))
        self.eventlist.setSortingEnabled (__sortingEnabled)
        self.calendarbutton.setAccessibleName (_translate ("MainWindow", "calendarbutton"))
        self.calendarbutton.setText (_translate ("MainWindow", "View in Calendar"))
        self.newexambutton.setAccessibleName (_translate ("MainWindow", "newexambutton"))
        self.newexambutton.setText (_translate ("MainWindow", "New Exam"))
        self.label_4.setText (_translate ("MainWindow",
                                          "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Today</span></p></body></html>"))

        self.newsessionbutton.setAccessibleName (_translate ("MainWindow", "newsessionbutton"))
        self.newsessionbutton.setText (_translate ("MainWindow", "New Session"))


    def listfrommemory(self, memfile='memory.json'):
        with open (memfile, 'r') as memory:
            date_today = datetime.datetime.now ().date ().isoformat ()
            acceptable_args = ['deadline', 'exam', 'project', 'other']  # All things which are not sessions
            deadlines = [thing for thing in load (memory) if
                         thing['type'].lower () in acceptable_args]  # If thing is a deadline/project/whatever
            upcoming_deadlines = [thing for thing in deadlines if thing['deadline'] >= date_today]
            upcoming_deadlines = sorted (upcoming_deadlines, key=lambda k: k['deadline'])
            # Returns today's date in ISO format (date only)
            for thing in upcoming_deadlines:
                x = thing['name'].upper ()
                y = '[' + thing['subject'] + ']:'
                z = thing['deadline'].split ('T', 1)[0]  # removes the time portion of datetime
                item = QtWidgets.QListWidgetItem (x + y + z)
                for key, value in subjectgroups.items ():
                    if thing['subject'] in value:
                        item.setBackground (QtGui.QColor (colourdictionary_light[key]))
                        break
                        #TODO: Colourdictionarydark
                self.eventlist.addItem (item)
                linebreak = QtWidgets.QListWidgetItem ('')
                self.eventlist.addItem (linebreak)

    def displaycheckboxestoday(self, memory):
        for i in reversed (range (self.gridLayout.count ())):
            self.gridLayout.itemAt (i).widget ().setParent (None)
        boxnumber = 0
        date_today = datetime.datetime.now ().date ()  # Returns today's date in ISO format (date only)
        date_today = str (date_today)
        self.label_4.setText (
                              "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Today</span></p></body></html>")
        with open (memory, 'r') as jsonmem:
            # Get all today's events using iso date handling
            # todayevents = [thing for thing in load (memory) if thing['event_type'].lower() =='session'
            #              and datetime.date.fromisoformat(thing['deadline'])]
            sessions = [item for item in load (jsonmem) if item['type'].lower() == 'session']
            #print(sessions)
            today_sessions = [item for item in sessions if datefromiso (item['start_time']) == date_today]
            today_sessions = sorted (today_sessions, key=lambda k: k['start_time'])
            print(today_sessions)
            # itemdate = item['start_time'].split ('T', 1)[0]  # Returns the date segment only

            # itemdate=None
            # if item['type'].lower() =='session' and date_today == itemdate:
            for item in today_sessions:
                self.eventcheckbox = QtWidgets.QCheckBox (self.gridlayout)
                self.eventcheckbox.setText (item['description'])
                for key, value in subjectgroups.items ():
                    if item['subject'] in value:
                        self.eventcheckbox.setStyleSheet ("background-color:" + colourdictionary_light[key] + '; \n')
                        break
                self.gridLayout.addWidget (self.eventcheckbox, boxnumber, 0, 1, 1)
                boxnumber += 1


    def displaycheckboxesweek(self, memory):
        for i in reversed (range (self.gridLayout.count ())):
            self.gridLayout.itemAt (i).widget ().setParent (None)
        boxnumber = 0
        date_today = datetime.datetime.now ().date ()  # Returns today's date in ISO format (date only)
        date_today = datefromiso(str (date_today))
        print(date_today)
        weeklater = (datetime.datetime.now () + datetime.timedelta (days=7)).isoformat ()
        print(weeklater)
        self.label_4.setText (
                              "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">This Week</span></p></body></html>")

        #print (weeklater)
        with open (memory, 'r') as jsonmem:
            # Get all this week's events using iso date handling
            sessions = [item for item in load (jsonmem) if item['type'].lower() == 'session']
            thisweek = [item for item in sessions if date_today <= datefromiso (item['start_time']) <= datefromiso(weeklater)]
            thisweek = sorted (thisweek, key=lambda k: k['start_time'])

            # itemdate = item['start_time'].split ('T', 1)[0]  # Returns the date segment only

            # itemdate=None
            # if item['type'].lower() =='session' and date_today == itemdate:
            for item in thisweek:
                self.eventcheckbox = QtWidgets.QCheckBox (self.gridlayout)
                self.eventcheckbox.setText (item['description'])
                for key, value in subjectgroups.items ():
                    if item['subject'] in value:
                        self.eventcheckbox.setStyleSheet ("background-color:" + colourdictionary_light[key] + '; \n')
                        break
                self.gridLayout.addWidget (self.eventcheckbox, boxnumber, 0, 1, 1)
                boxnumber += 1

    def createform(self):
        self.window = QtWidgets.QMainWindow ()
        self.dialog = FormWindow (self.window)
        self.window.show ()

    def createsessionform(self):
        self.window = QtWidgets.QMainWindow ()
        self.dialog = Sessionform (self.window)
        self.window.show ()

    def showcalendar(self):
        self.window = QtWidgets.QDialog ()
        self.window.setStyleSheet ("background-color:black")
        self.dialog = Calendar(self.window)
        self.window.show ()



    def setdarktheme(self):
        stylesheet = '''
        border-width: 2px;
        border-radius: 4px;
        padding: 2px;
        border-style: outset;
        border-color:#00FFFF
        '''

        # self.MainWindow.setStyleSheet ("background-color:black")
        # self.changemodebutton.setStyleSheet ("color:white")
        with open ('dark.qss','r') as theme:
            self.MainWindow.setStyleSheet(theme.read())
        self.todaybutton.setStyleSheet (stylesheet)
        self.weekbutton.setStyleSheet (stylesheet)
        self.eventlist.setStyleSheet (stylesheet)
        self.calendarbutton.setStyleSheet (stylesheet)
        self.newexambutton.setStyleSheet (stylesheet)
        self.newsessionbutton.setStyleSheet (stylesheet)
        self.label_4.setStyleSheet ("color:cyan;")
        self.darktheme=True
        self.label_4.setText(
                                          "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Today</span></p></body></html>")

    def setlighttheme(self):
        stylesheet = '''border-style: outset;\n
                      border-width: 2px;\n
                      border-radius: 4px;\n
                      border-color: blue\n

                      '''
        orangestylesheet = '''border-style: outset;\n
                            border-width: 2px;\n
                            border-radius: 4px;\n
                            border-color: darkorange\n
                            '''


        #self.MainWindow.setStyleSheet ("background-color:white")
        # self.changemodebutton.setStyleSheet ("color:black")
        with open ('light.qss','r') as theme:
            self.MainWindow.setStyleSheet(theme.read())
        self.todaybutton.setStyleSheet (stylesheet)
        self.label_4.setStyleSheet ("color:blue;")
        self.weekbutton.setStyleSheet (stylesheet)
        self.eventlist.setStyleSheet (stylesheet)
        self.calendarbutton.setStyleSheet (stylesheet)
        self.newexambutton.setStyleSheet (orangestylesheet)
        self.newsessionbutton.setStyleSheet (orangestylesheet)
        self.darktheme=False
        self.label_4.setText ("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Today</span></p></body></html>")

    def changetheme(self):
        with open ('theme.json', mode='r') as memory:
            s = load (memory)
            if not s["darktheme"]:
                self.setdarktheme ()
                theme = '''{"darktheme":true}'''
            else:
                self.setlighttheme ()
                theme = '''{"darktheme":false}'''
        with open ('theme.json', mode='w') as memory:
            memory.write (theme)

    def schedule(self, event: dict, wordcount, chaptercount):
        self.window.close()
        k = 1  # 'some constant'
        deadline_date = datefromiso (event['deadline'])
        days_available = daysBetween (datetime.date.fromisoformat (deadline_date))  # start time is iso string
        # DONE:CHECK FOR WORDCOUNT/CHAPTERCOUNT, ETC.
        #print ("Available days:" + str (days_available))
        time_required = wordcount / 250 + chaptercount * 1.5  # 90mins/chapter, and 250 words an hour.
        daily_sessions = round (
            time_required / days_available) if days_available > 0 else time_required  # time required is a plain number of hours
        #print ("Daily Sessions" + str (daily_sessions))
        frontloaded_days_int = round (days_available / 2) if days_available > 1 else 1  # number of days
        days_of_frontloaded_studying = datetime.timedelta (days=frontloaded_days_int)
        current_day = datetime.datetime.now ().date ()
        # print('Schedule was called')
        # day_counter=1 #Used as int counter for following for loop #TODO; manage placement (nested fors are weird)
        time_of_session = 9
        for i in range(1, frontloaded_days_int + 1):  # Everything within here repeats once a day
            # TODO: Format as Cronofy apt. JSON
            # TODO: Free-busy check
            # for session in range(0, min(round(1.5*daily_sessions), 4)):
            for session in range(5, round(min(2*2*daily_sessions+5,14)), 2):  # Creates a new session 30 mins later, this block  TODO: Possibly refine using hours and minutes
                # Changed from 9,18,2 to take into account timezones, if there are fewere sessions only schedules those
                # print("Calling write_session")
                self.write_session(datetime.time (hour=session), i, event)
                # print("Called write_session")
                # TODO: Timestring formatting
                # TODO: Timestring for param of write_session will be created based on
                #  current date+timedelta(n days, where n is an iterator in the for loop)+9hrs
                #print (i)
                # time_of_session += 3

            # day_counter+=1
        # deadline_date = datefromiso(event['deadline'])
        # time_of_session_notfrontloaded=9
        # normal_days=days_available-frontloaded_days_int
        for j in range (frontloaded_days_int, days_available):
            for session in range (5, min(3*daily_sessions+5,14), 3):  # Caps the number of daily sessions
                self.write_session (datetime.time (hour=session), j)

    def write_session(self, time,
                      displacement,memory_dict):  # Time refers to the  starting time (not date) of the session. Displacement refers to the
        free_time =crono_cal.read_free_busy (from_date=datetime.datetime.now (),
                                                   # to_date=datetime.date.fromisoformat('date_of_exam'), This is a method which does it for all days
                                                   to_date=datetime.datetime.now () + datetime.timedelta (
                                                       days=displacement), automatic_pagination=False)
        # Does it only for one day (since we're already iterating through days, this is more convenient)

        # print(free_time.json())
        '''free_time=free_time.json()['free_busy']
            free_times_filtered=[timeblock for timeblock in free_time if timeblock["free_busy_status"] == "free"]
            if free_times_filtered: #TODO: refine this test
                print('free time filtered exists')
                for timeframe in free_times_filtered:
                    if timeframe['start'] <= time <= timeframe['end'] :
                        random_id= self.randomiser()
                        self.create_session(session={
                            'event_id': '',
                            'name': '',
                            'subject': '',
                            'description': '',
                            'start_time': time,
                            'end_time':
                                (datetime.datetime.fromisoformat (time) + datetime.timedelta (minutes=90)).isoformat,
                            'type':'session'},
                            cronosession={
                                'event_id':'',
                                'sessionplan': "",
                                'description': "",
                                'start': time,
                                'end': (datetime.datetime.fromisoformat (time) + datetime.timedelta (minutes=90)).isoformat,
                                'reminders': [{"minutes": 10}]
                            })
                        # Returns the time 90 mins later, as an iso string
                        return
            else:'''
        # print('Free-busy is empty')
        precomputed_end = (datetime.time (hour=time.hour + 1, minute=time.minute + 30)).isoformat ()
        #print (precomputed_end)
        # DONE: At least this works as a time
        # random_id = self.randomiser()

        # session_summary = self.sessionplan.toPlainText() if self.sessionplan.toPlainText () != '' \
        #   else "Study Session " + self.subject_box.currentText ()
        session_summary = memory_dict['notes'] if memory_dict['notes'] != '' \
            else "Study Session " + memory_dict['subject']
        Constructed_Date = (datetime.datetime.now ().date () + datetime.timedelta (days=displacement)).isoformat ()
        eventID = randomiser_for_ids()
        # Constructs a date using time and displacement parameters

        session = {
            'event_id': eventID,
            'name': '',
            'subject': memory_dict['subject'],
            'description': 'Work On ' + "\'" + session_summary + "\'",
            'plan': '',
            'type': 'session',
            'start_time': Constructed_Date + 'T' + time.isoformat () + 'GST',
            'end_time': Constructed_Date + 'T' + precomputed_end + 'GST',  # Adds 90 minutes
            'deadline': None
            # TODO; Make sure that the time/date thing doesn't break
            #  (since it uses the same time parameter, it might create sessions at the same time)
            # time + datetime.timedelta (minutes=90)).isoformat,
        }

        cronosession = {
            'event_id': eventID,
            'summary': 'Work On ' + "\'" + session_summary + "\'",
            'description': "more whatnot",
            'start': Constructed_Date + 'T' + time.isoformat ()+'GST',
            'end': Constructed_Date + 'T' + precomputed_end+'GST',
            #'tzid':"Asia/Dubai"
        }
        #print ('Cronosession' + dumps (cronosession))
        crono_cal.upsert_event (cal_id, cronosession)
        # QtWidgets.QCalendarWidget.paintCell(session['date']) # FIXME
        # n = notify2.Notification(None, icon='') #FIXME
        # n.update (session['name'], session['description'])
        writetoJSON(session)
        notificationjob=scheduler.add_job(notification(session['subject'],session['description'],))


class Sessionform(QtWidgets.QMainWindow):
    def __init__(self, MainWindow, parent=None):
        super (QtWidgets.QMainWindow, self).__init__ (parent)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 472)
        self.MainWindow=MainWindow
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.subject_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.subject_box.setObjectName("subject_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.subject_box)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit)
        #self.dateTimeEdit.setMinimumSize(QtCore.QSize(130,20))
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.sessionplan = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        #self.sessionplan.setMaximumSize(QtCore.QSize(200, 100))
        self.sessionplan.setObjectName("sessionplan")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sessionplan)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.summary = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summary.sizePolicy().hasHeightForWidth())
        self.summary.setSizePolicy(sizePolicy)
        self.summary.setMaximumSize(QtCore.QSize(250, 25))
        self.summary.setObjectName("summary")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.summary)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 394, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        for i in range (0, len (listofsubjects) - 1): self.subject_box.addItem(listofsubjects[i])

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda : self.save_event())
        #self.stylehandler()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Subject"))
        self.label_4.setText(_translate("MainWindow", "Date"))
        self.label_3.setText(_translate("MainWindow", "Event"))
        self.label_5.setText(_translate("MainWindow", "Plan/Notes"))
        self.pushButton.setText(_translate("MainWindow", "Save Event"))
        self.dateTimeEdit.setDate (QtCore.QDate.currentDate ())

    def save_event(self):
        iso_date = self.dateTimeEdit.dateTime ().toPyDateTime ().isoformat()

        eventID = randomiser_for_ids ()
        memory_dict = {
            'event_id': eventID,
            'type': "Session",
            'name': self.summary.toPlainText(),
            'subject': self.subject_box.currentText(),
            'start_time': iso_date,
            'deadline': iso_date,
             'plan': self.sessionplan.toPlainText(),
            'description': self.sessionplan.toPlainText()
        }

        cronofy_dict = {
            'event_id': eventID,
            'summary': memory_dict['name'],
            'description': self.sessionplan.toPlainText(),
            'start': iso_date+'GST',
            'end': (datetime.datetime.fromisoformat (iso_date) + datetime.timedelta (minutes=90)).isoformat ()+'GST',
            # 1 minute later
        }

        writetoJSON(memory_dict)
        crono_cal.upsert_event (cal_id, cronofy_dict)
        self.close()


class FormWindow (QtWidgets.QMainWindow):

    def __init__(self, MainWindow, parent=None):
        super (QtWidgets.QMainWindow, self).__init__ (parent)
        MainWindow.setObjectName ("MainWindow")
        MainWindow.resize (355, 437)
        # MainWindow.setStyleSheet("background-color:black")
        self.MainWindow=MainWindow
        self.centralWidget = QtWidgets.QWidget (MainWindow)
        self.centralWidget.setObjectName ("centralWidget")
        self.formLayoutWidget = QtWidgets.QWidget (self.centralWidget)
        self.formLayoutWidget.setGeometry (QtCore.QRect (10, 10, 341, 361))
        self.formLayoutWidget.setObjectName ("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout (self.formLayoutWidget)
        self.formLayout.setContentsMargins (11, 11, 11, 11)
        self.formLayout.setSpacing (6)
        self.formLayout.setObjectName ("formLayout")
        self.label = QtWidgets.QLabel (self.formLayoutWidget)
        self.label.setObjectName ("label")
        self.formLayout.setWidget (1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.event_type_box = QtWidgets.QComboBox (self.formLayoutWidget)
        self.event_type_box.setObjectName ("event_type_box")
        self.event_type_box.addItem ("")
        self.event_type_box.addItem ("")
        self.event_type_box.addItem ("")
        self.event_type_box.addItem ("")
        self.formLayout.setWidget (1, QtWidgets.QFormLayout.FieldRole, self.event_type_box)
        self.label_2 = QtWidgets.QLabel (self.formLayoutWidget)
        self.label_2.setObjectName ("label_2")
        self.formLayout.setWidget (2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.subject_box = QtWidgets.QComboBox (self.formLayoutWidget)
        self.subject_box.setObjectName ("subject_box")
        for i in range (0, len (listofsubjects) - 1): self.subject_box.addItem (listofsubjects[i])
        self.formLayout.setWidget (2, QtWidgets.QFormLayout.FieldRole, self.subject_box)
        self.horizontalLayout = QtWidgets.QHBoxLayout ()
        self.horizontalLayout.setSpacing (6)
        self.horizontalLayout.setObjectName ("horizontalLayout")
        self.formLayout.setLayout (3, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel (self.formLayoutWidget)
        self.label_3.setObjectName ("label_3")
        self.formLayout.setWidget (7, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel (self.formLayoutWidget)
        self.label_4.setObjectName ("label_4")
        self.formLayout.setWidget (4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit (self.formLayoutWidget)
        self.dateTimeEdit.setObjectName ("dateTimeEdit")
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(100,20))
        self.formLayout.setWidget (4, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit)
        self.label_5 = QtWidgets.QLabel (self.formLayoutWidget)
        self.label_5.setObjectName ("label_5")
        self.formLayout.setWidget (8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.summary = QtWidgets.QPlainTextEdit (self.formLayoutWidget)
        self.summary.setMaximumSize (QtCore.QSize (200, 100))
        self.summary.setObjectName ("sessionplan")
        self.formLayout.setWidget (7, QtWidgets.QFormLayout.FieldRole, self.summary)
        self.plan = QtWidgets.QPlainTextEdit (self.formLayoutWidget)
        self.plan.setMaximumSize (QtCore.QSize (200, 100))
        self.plan.setObjectName ("summary")
        self.formLayout.setWidget (8, QtWidgets.QFormLayout.FieldRole, self.plan)
        self.label_6 = QtWidgets.QLabel (self.formLayoutWidget)
        self.label_6.setObjectName ("label_6")
        self.formLayout.setWidget (5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel (self.formLayoutWidget)
        self.label_7.setObjectName ("label_7")
        self.formLayout.setWidget (6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.word_count = QtWidgets.QSpinBox (self.formLayoutWidget)
        self.word_count.setMaximum (90000)
        self.word_count.setSingleStep (200)
        self.word_count.setProperty ("value", 0)
        self.word_count.setObjectName ("word_count")
        self.formLayout.setWidget (5, QtWidgets.QFormLayout.FieldRole, self.word_count)
        self.chapter_count = QtWidgets.QSpinBox (self.formLayoutWidget)
        self.chapter_count.setObjectName ("chapter_count")
        self.formLayout.setWidget (6, QtWidgets.QFormLayout.FieldRole, self.chapter_count)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout ()
        self.horizontalLayout_3.setSpacing (6)
        self.horizontalLayout_3.setObjectName ("horizontalLayout_3")
        self.formLayout.setLayout (11, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout ()
        self.horizontalLayout_4.setSpacing (6)
        self.horizontalLayout_4.setObjectName ("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem (40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem (spacerItem)
        self.save_button = QtWidgets.QPushButton (self.formLayoutWidget)
        self.save_button.setMaximumSize (QtCore.QSize (200, 16777215))
        self.save_button.setObjectName ("pushButton")
        self.horizontalLayout_4.addWidget (self.save_button)
        self.formLayout.setLayout (9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        MainWindow.setCentralWidget (self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar (MainWindow)
        self.menuBar.setGeometry (QtCore.QRect (0, 0, 355, 22))
        self.menuBar.setObjectName ("menuBar")
        MainWindow.setMenuBar (self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar (MainWindow)
        self.mainToolBar.setObjectName ("mainToolBar")
        MainWindow.addToolBar (QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar (MainWindow)
        self.statusBar.setObjectName ("statusBar")
        MainWindow.setStatusBar (self.statusBar)
        # self.dialog = Second()

        self.retranslateUi (MainWindow)
        #self.stylehandler()
        QtCore.QMetaObject.connectSlotsByName (MainWindow)
        self.save_button.clicked.connect (self.save_event)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle (_translate ("MainWindow", "MainWindow"))
        self.label.setText (_translate ("MainWindow", "Event type"))
        self.dateTimeEdit.setDate (QtCore.QDate.currentDate ())
        self.event_type_box.setItemText (0, _translate ("MainWindow", "Exam"))
        self.event_type_box.setItemText (1, _translate ("MainWindow", "Project"))
        self.event_type_box.setItemText (2, _translate ("MainWindow", "Deadline"))
        self.event_type_box.setItemText (3, _translate ("MainWindow", "Other"))
        self.label_2.setText (_translate ("MainWindow", "Subject"))
        self.label_3.setText (_translate ("MainWindow", "Summary/Notes"))
        self.label_4.setText (_translate ("MainWindow", "Deadline"))
        self.label_5.setText (_translate ("MainWindow", "Plan"))
        self.label_6.setText (_translate ("MainWindow", "Word count"))
        self.label_7.setText (_translate ("MainWindow", "Chapter count"))
        self.save_button.setText (_translate ("MainWindow", "Save Event"))

    # TODO: Define way of checking for existing events and delaying accordingly
    # https://docs.cronofy.com/developers/api/events/free-busy/
    # TODO; UI implementation of updating events
    """With paintcell method (happens on startup), 
    also include a clickable=true button somehow,
     which adds a specific method 
     (opens a form to update the time or delete the event)"""

    def save_event(self):
        iso_date = self.dateTimeEdit.dateTime ().toPyDateTime ().isoformat()
        #print (iso_date)
        eventID = randomiser_for_ids ()
        memory_dict = {
            'event_id': eventID,
            'type': self.event_type_box.currentText (),
            'subject': self.subject_box.currentText (),
            'deadline': iso_date,
            'wordcount': self.word_count.value (),
            'chaptercount': self.chapter_count.value (),
            'notes': self.summary.toPlainText (),
            'summary': self.plan.toPlainText (),
            'name': self.summary.toPlainText (),
            'description': self.summary.toPlainText()
            # TODO: Fix this, update form (just add another label, it'll be fine)
        }
        cronofy_dict = {
            'event_id': eventID,
            'summary': memory_dict['notes'],
            'description': "An important deadline",
            'start': iso_date+'GST',
            'end': (datetime.datetime.fromisoformat (iso_date) + datetime.timedelta (hours=2)).isoformat ()+'GST',
            # 1 minute later
        }
        # print ((datetime.datetime.fromisoformat (iso_date) + datetime.timedelta (hours=2)).isoformat ())
        # print(self.dateTimeEdit.dateTime())
        # print(dictionary)
        writetoJSON(memory_dict)
        crono_cal.upsert_event (cal_id, cronofy_dict)
        Ui_MainWindow.schedule(ui, memory_dict, self.word_count.value(), self.chapter_count.value())
        self.close()

    '''def create_session(self, session: dict, cronosession: dict):
            print('Cronosession'+dumps(cronosession))
            self.crono_cal.upsert_event ('cal_XCmB-arHdDNqarAX_GAJgjx5fiGXiC6G12LnAig',cronosession)
            # QtWidgets.QCalendarWidget.paintCell(session['date']) # FIXME
            #n = notify2.Notification(None, icon='') #FIXME
            #n.update (session['name'], session['description'])
            with open ('memory.json', mode='r+') as memory:
                s = memory.read ().replace (']', '')
                memory.seek (0)
                memory.truncate ()
                memory.write (s)
                # Leaves an unclosed parentheses

            with open ('memory.json', mode="a") as memory:
                memory.write (', \n')
                dump (session, memory, indent=3)
                memory.write (']')
    '''


class Calendar (QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__ (self, parent)
        self.setMinimumSize (QtCore.QSize (500, 500))
        self.setMaximumSize (QtCore.QSize (5000, 5000))
        self.setSelectionMode (False)
        self.currentPageChanged.connect (lambda: self.updateCells ())
        self.setStyleSheet ("background-color:white;\n color:black")


    def paintCell(self, painter, rect, date):
        QtWidgets.QCalendarWidget.paintCell (self, painter, rect, date)
        with open ('memory.json', mode='r') as memory:
            exams = [i for i in load (memory) if i['type'].lower () in ['deadline', 'exam', 'project', 'other']]
            x = date.toPyDate ().isoformat ()  # ISO format of a calendar date (this should run on every cell of the calendar)
            for exam in exams:
                if x == datefromiso (exam['deadline']):
                    # Finds the required colour based on the dictionary
                    for (key, value) in subjectgroups.items ():
                        if exam['subject'] in value:
                            painter.setBrush (QtGui.QColor (colourdictionary_light[key]))
                            painter.drawRect (rect)
                            painter.setBrush (QtGui.QColor ('#ffffff'))
                            painter.drawText (rect.center (), str (date.day ()))
                            painter.drawText (rect.bottomLeft (), exam['subject'])
                            break
    def screenshot(self):
        QtGui.QPixmap.grabWindow(app.desktop ().winId ()).save(datetime.datetime.now().isoformat(), 'jpg')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication (sys.argv)
    MainWindow = QtWidgets.QMainWindow ()
    ui = Ui_MainWindow (MainWindow)
    MainWindow.show ()
    sys.exit (app.exec_ ())


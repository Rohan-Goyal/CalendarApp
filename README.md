# CalendarApp

The app is designed to let you keep track of events and schedule periodic sessions for you to work/study, based on your calendar. Currently the google calendar integration doesn't work, because the app has not been verified by cronofy. So the only way to use that feature is to manually enter your client token and calendar ID to use them, using the discreetly marked button. Furthermore if you do that I make no guarantees regarding security of your information, so hack about at your own risk.

The way the app works is quite intuitive. Download the file appropriate to your OS, run it like you would any similar file (or via terminal if you want to see any print/debug statements I forgot to delete). The events view can be changed by clicking either 'today' or 'next 7 days' to show the upcoming sessions for that. Scheduling an exam or project automatically schedules sessions as well; this might slow down a bit when the app tries to connect to the network for cronofy, but in general it works quite well (at least when I tested it). Scheduling an event of any kind writes it both to memory and an external calendar (at least it should) and notifications are triggered to. However, they only work if you keep the app running in the background, so if you close it halfway through it might simply fail. This bug needs to be improved, I know, but it requires implementing a lot of architecture which I am extremely unfamiliar with, and probably worth an entire project in itself.
The app should work in all time zones (since it uses UTC and Pytz), but since testing only took place in GST/UAE, impossible to say for sure. If there are any major errors, please file a bug report.

## Instructions

### Initialisation

#### To run it as a plain app (in which case calendar integration won't work)

Download the appropriate file for your platform (.app for macOS, .exe for Windows, and the other one for Linux). If it is not available, assume that a bug has been discovered for that specific executable, and I am trying to fix it.
Move it to your applications directory or simply run it straight away, and let it run.

#### To run it as a Python Script

Download the Python Script, and run it in your Python Launcher. Make sure that you are using Python 3.x (written in 3.7).
The packages required in your environment are:
    1. PyQt5
    2. PyCronofy
    3. APScheduler
    3. Notify2 (only for Linux users)
    4. Applescript (Only for Mac users)
    5. Win10toast (Only for Windows users)

### General

Use the 'new event' form to schedule an exam,project, or deadline. Enter the word or chapter count for the work (whichever is valid), and based on that the app will automatically schedule a certain number of periodic sessions. To create a session to study a specific topic, simply click the new session button and fill out the form. The app schedules notifications as long as you keep it running in the background. If there are issues with memory or performance, consider it to be a bug and file a report.

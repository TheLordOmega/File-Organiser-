first python worked
then test main.py
then made small code to move txt files to folder and it worked
needed to fix that it creates the folder if it doesnt exist

what works: moving files based on suffix

we want it to be able to open file and read if keyword is there, and id based on priroties


ok now it can open md files and print the contents

we need it to try and predict from the name the subject and if it isnt 90% sure then it should read keywords in md files
 it recognised spc due to inside and moved and renamed file.


using pathlib library to move and read files55mOct 14, 2026
I got python set-up and working and then tested customtkinter's window if it was working
then i made a small program that moved txt files to a new folder based on the suffix.
This program was then generalised to work with any suffix.
The second thing i got working was opening markdown files (for example) and reading the contents and printing it. this took a few tries.
in the last 10 minutes i was able to make a rough draft for a progrma that combined both aspects, it read the md files and looked for keywords related to physics and then moved this to a new folder called physics and it also renamed the file to physics.md.
what works: moving files, reading md files
 what we need to improve on: be able to read any file (maybe even images?) and being able to decide between different options if 2 keywords for 2 different folders are there.

hour 2

was able to print whole directory tree

was able to implement code that takes a date and give all the files modified since that date
will now implement a save so that it only scans files modified since the last scan by having the date saved in a file

then join all the codes i have written so far

1h40-
now we have multiple small snippets of code that worked individually, we need to implement a path

we have unorganised files by type, date and content,
we want the program to organise in this way:

look at modified since last scan- done  and save date.
then have directory
then read files
decide the content theme
then move files to appropriate folder
sort them then by type
then by date
rename file based on that



week-end finish github working
emploi du temps




2h,

improving code, made it more efficient, just easier to follow


put all constants at the top
improved topics
made topics better

2h40:
start implementing ai for images and files harder



did 30 min of the GUI setup





made most of the ui but separatly:
made the framless code that makes the actual window looks smart (less.py)
made the directory selector (file.py)
made the tool.py
made ui.py for the buttons and other stuff

made draft  the multicore performance mult.py
then 
i have worked for 4h to do 1 thing:
optimize everything by making all the scripts more streamlined and connected this includes:

split Organiser.py into multiple specialized files that i can call as functions too,
i made: 
config.py : with everything setting related:   
- directory to use (current one)
- where the folder is named 
- history file and the save file code from before
- the blacklist of things not to move 
- topics available currently


cleanup.py: 
- remove all unnecessary spaces between files (due to conversion from pdf for example)
- yet to be implemented into the GUI

scanner.py:
- scans the directory, based on the history 
- make sure errors are well reported
- *theoratically should be made into a preview but has not yet been implemented or tested if possible.*
- connected to config as input and forwards to main.py

pdf.py:
- pdf extractor
- works but hasnt been implemented in terms of UI or forwarding completly
- and has the unnessary spaces (fixed with cleanup.py)

try.py:
- will be the place i feed the examples , including files for when the AI will be implemented 
- Haven't worked on the AI yet


main.py:
- will be the script that ties everything together, 
- is what connects everything to the UI

Ui.py:
- the biggest part of the project that took almost 5h 
- has a framless window
- multiple widgets using a menu bar that is elegant
- still doesn't have pill shape perfect 
- uses QT through PySide6.
- has mutiple buttons and i have drafts with left click and changes that will help with the implementation of more features
- images used for the minimize, maximize, close are including as svg from ZED code visualizer as they look good.


sources used this week:
https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/
https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html
https://doc.qt.io/archives/qt-5.15/qlabel.html#public-slots
https://doc.qt.io/qtforpython-6/overviews/qtwidgets-layout.html
https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGridLayout.html#PySide6.QtWidgets.QGridLayout
https://www.pythontutorial.net/pyqt/pyqt-qfiledialog/
https://www.pythonguis.com/tutorials/pyside6-creating-your-own-custom-widgets/
https://www.pythonguis.com/tutorials/pyside6-layouts/
https://realpython.com/python-pathlib/

also have a multithread draft that isnt implemented in oython files called mult.py:
https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/

A python file organiser that can organise a directory
see second part for Week2 


#Week1

text_files folder  was the directory used with inside of it some different types of files including some files to ignore by the code such as the history.md file that is used to track last saved  progress and the devlog drafts of this projects and my ideas as they come

class.py is the neural network script that is the most final till now (still doesn't work as i have not trained it yet and it isn't complete )
classifier.py is the first draft of how a neural network works and such

main.py will be the UI  script 
Organiser.py is the working file organiser/


features implemented
added a renaming, moving and opening md files based on content and title name and keywords
added a history file that lets us save the time and lets us continue where we left off so you dont need to reorganise the same things everytime 
features to be completed:
implementation of the neural network for better understanding of classifications
the basic understanding of how to train said neural network

features to be added :
improve the code
train the classifier on my training data
make a template maker into it
Make the UI
let me pick the directory through the GUI
BONUS : turn it into an app


sources used: 

https://realpython.com/python-pathlib/
https://pypdf.readthedocs.io/en/latest/user/extract-text.html?utm_source=chatgpt.com
https://scikit-learn.org/1.3/tutorial/text_analytics/working_with_text_data.html?utm_source=chatgpt.com
https://uw-madison-datascience.github.io/2022-10-26-machine-learning-novice-sklearn/06-neural-networks/index.html
https://techyorker.com/text-classification-explained-step-by-step-from-labeled-data-to-a-working-model/?utm_source=chatgpt.com
https://customtkinter.tomschimansky.com/tutorial/grid-system/



#Week2: 

made most of the ui but separatly:
made the framless code that makes the actual window looks smart (less.py)
made the directory selector (file.py)
made the tool.py
made ui.py for the buttons and other stuff

made draft the multicore performance mult.py
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

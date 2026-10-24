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


built a pdf extractor tool that extracts the text from pdf and saves it to a md file

i then made a script that remove all teh unnesary sapces from said markdown or any markdown in general

plans for next :
combine all these scripts into a single organise
and start the training data
make the space saving also work for making it a specific template

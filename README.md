Questions
=========


This repository consists of an app to upload and download files. The app was created using PyCharm as IDE and uses Postgres as its database. 
It also consists of python scripts for :
1) check for overlapping rectangles (namely, Question1)
2) Finding a word from a list of words (namely, Question2)

For running the project,
1) /register/ : is the url to open signup page, where a user can signup
2) /signin/ : url for logging in
3) After logging-in, the user will be directed to 'upload-download' template, where he/she can either upload a file or download files from a list of existing files.

For Question1, (ie. overlapping rectangles):
-> The user needs to create 2 instances of Rectangle class
-> Pass these 2 instances as arguments for the rectangle_overlap() function

For Question2, (ie. searching a word from a list of words):
-> The user needs to pass a list of words as first argument and a word that is to be searched as its second parameter

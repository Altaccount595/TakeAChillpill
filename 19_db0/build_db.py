#Sasha (Alex) Murokh, Jonathan Metzler, Naf Murtaza
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#for students
with open('students.csv', newline='') as file:
    reader = csv.DictReader(file) #reads file as dictionaries: with header row as keys
    dict = []
    for row in reader:
        dict+=[row]
    #print(dict) #list of dictionaries
    
c.execute("CREATE TABLE roster (name TEXT, age INTEGER, id INTEGER)") #creates table with column names + types
for item in dict:
    lst = list(item.values()) 
    lst[1] = int(lst[1]) #convert to ints
    lst[2] = int(lst[2])
    lst = str(lst)
    lst = '(' + lst[1:len(lst)-1] + ')' #format properly for sqlite to accept
    #print(lst)
    c.execute(f'INSERT INTO roster (name, age, id) VALUES {lst}') # inserts each row of values into respective headers
#==========================================================
#for courses
with open('courses.csv', newline='') as file:
    reader = csv.DictReader(file) #reads file as dictionaries: with header row as keys
    dict = []
    for row in reader:
        dict+=[row]
    #print(dict) #list of dictionaries

c.execute("CREATE TABLE courselist (code TEXT,mark INTEGER,id INTEGER)") #creates table with column names + types
for item in dict:
    lst = list(item.values()) 
    lst[1] = int(lst[1]) #convert to ints
    lst[2] = int(lst[2])
    lst = str(lst)
    lst = '(' + lst[1:len(lst)-1] + ')' #format properly for sqlite to accept
    #print(lst)
    c.execute(f'INSERT INTO courselist (code,mark,id) VALUES {lst}') # inserts each row of values into respective headers


#==========================================================

db.commit() #save changes
db.close()  #close database

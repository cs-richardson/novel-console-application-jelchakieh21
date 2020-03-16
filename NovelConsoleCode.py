
import sqlite3 as sq
from datetime import datetime, date

con = sq.connect("Novel Final.db")
c = con.cursor()

def get_author():
    res = c.execute("SELECT AuthorID, Name, DOB from Authors")
    data = c.fetchall() # Gets the author data from the table
    return data

def get_novels():
    res = c.execute("SELECT Name, Quantity, NovelID, AuthorID")
    data = c.fetchall() # Gets the novel data from the table
    return data

def add_author(authorid, name, dob):
    ins_str = 'INSERT INTO Authors (AuthorID, DOB, Name) Values (' + str(authorid) + ', ' + str(dob) + ', "' + str(name) + '");'
    print (ins_str)
    res = c.execute(ins_str) 
    con.commit()

def add_novels(name, quantity, novelid, authorid):
    ins_str = 'INSERT INTO Novels (Quantity, NovelID, AuthorID, Name) Values (' + str(quantity) + ', ' + str(novelid) + ', ' + str(authorid) + ',"' + str(name) + '");'
    print (ins_str)
    res = c.execute(ins_str)
    con.commit()

def render_author_report():
    author = get_author()
    tbl = "|---------------------------\n|"
    for row in author:
        for field in row:
            tbl += str(field)
            tbl += ", "
        tbl += "\n|"
    tbl += "---------------------------"

    print("Author results\n\n" + tbl)

#This asks for these parameters when entering a new author
def render_author_request():
    authorid = input("Enter authorID:\t")
    name = input("Enter name:\t")
    dob = input("Enter DOB:\t")
    try:
        add_author(authorid, name, dob)
    except:
        print("Error- Try again", "Possible errors:  \nthere is already a reservation for that combination, you chose an invalid boat or sailor\nthe date is in an invalid format, \nsomeone else is entering a reservation at the same time")
        return

#This asks for these parameters when entering a new novel
def render_novel_request():
    authorid = int(input("Enter AuthorID:\t"))
    name = input("Enter Name:\t")
    quantity = int(input("Enter Quantity:\t"))
    novelid = int(input("Enter NovelID:\t"))
    try:
        add_novels(name, quantity, novelid, authorid)
    except:
        print("Error- Try again", "Possible errors:  \nthere is already a reservation for that combination, you chose an invalid boat or sailor\nthe date is in an invalid format, \nsomeone else is entering a reservation at the same time")
        return

#These are the options that the user gets when running this program
def render_menu():
    print("0. Run Report")
    print("1. Enter Author")
    print("2. Enter Novel")
    print("3. Exit")
    choice = int(input("Choose an option:\t"))

#This runs certain previous funcitons everytime when a certain choice is selected.
    if choice == 0:
        render_author_report()
    elif choice == 1:
        render_author_request()
    elif choice == 2:
        render_novel_request()
    elif choice == 3:
        end_program()
        return False;

    return True;


def end_program():
    con.close()

#This repeats "welcome to our novel database!" everytime an action takes place within the program.
while(render_menu()):
    print("\n\nWelcome to our novel database!")


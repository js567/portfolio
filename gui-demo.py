"""
Demonstration GUI for Asterisk Test

This is an example of a GUI I made for a research group at Oregon State University that I work with. 
This interface was used to help perform tests of robotic grasping systems.

When the file is running, camera control buttons and file buttons will not have any functionality,
so don't worry if they are not working. This is so that the program will run well on any computer
without needing to run a connected camera or to write files to the system drive.

Make sure to install tkinter before running if you haven't already.

pip install python-tk (terminal)

The test window is currently scaled to run well on Windows 10 1080p 16x9. Changing some of these
factors (such as Ubuntu instead of Windows) can mess with the scaling, so if that is an
issue for you, you can manually adjust the window size by dragging the borders or adjust the 
window dimensions below (line 34).

Written by Jack Stevenson in 2020/2021, email
stevenj4@oregonstate.edu or jstevenson567@gmail.com for questions and to offer feedback
"""

from tkinter import *
from tkinter import messagebox

# Initialize window

window = Tk()
window.title('Asterisk Test Portal')

# If you are having scaling issues, feel free to change the window size below

window.geometry('470x600')

# TEST INPUTS SECTION
# Edit this section to add/remove users, hands, etc.

name_list = ["john", "josh", "sage", "garth", "test"]

hand_list = ["human", "basic",  "m2stiff", "m2active",
             "2v2", "3v3", "2v3", "barrett", "modelvf"]

dir_list = ["a", "b", "c", "d", "e", "f", "g", "h", "cw", "ccw"]

trial_list = ["1", "2", "3", "4", "5"]

type_list = ["none", "plus15", "minus15"]

name_list_sel = StringVar(value=name_list)
hand_list_sel = StringVar(value=hand_list)
dir_list_sel = StringVar(value=dir_list)
trial_list_sel = StringVar(value=trial_list)
type_list_sel = StringVar(value=type_list)

# FUNCTION SECTION
# Defines functions used in program

# Function for help button


def help_me():
    messagebox.showinfo("Asterisk Test Help", '''
Welcome to Asterisk Help

To perform a test:
1. Select correct name, hand, direction, trial, and trial type
2. Press 'Check Selection' 
3. Press 'Initialize Test' 
4. Ensure that the window says 'Ready to record'
5. Press 'Record' and 'Stop' to record trial
6. File location should be displayed on the window 
7. Use 'Quit' or exit out of window to close program

To seek help with the test or report a bug contact Jack Stevenson at stevenj4@oregonstate.edu or John Morrow IV at morrowjo@oregonstate.edu
    ''')

name = ''
hand = ''
dir = ''
trial = ''
type = ''

name_selection = StringVar()
hand_selection = StringVar()
dir_selection = StringVar()
trial_selection = StringVar()
type_selection = StringVar()


# Functions to get user inputs


def show_name(*args):
    name_sel = nb.curselection()
    name_index = int(name_sel[0])
    name = name_list[name_index]
    name_selection.set(name)


def show_hand(*args):
    hand_sel = hb.curselection()
    hand_index = int(hand_sel[0])
    hand = hand_list[hand_index]
    hand_selection.set(hand)


def show_dir(*args):
    dir_sel = db.curselection()
    dir_index = int(dir_sel[0])
    dir = dir_list[dir_index]
    dir_selection.set(dir)


def show_trial(*args):
    trial_sel = tb.curselection()
    trial_index = int(trial_sel[0])
    trial = trial_list[trial_index]
    trial_selection.set(trial)


def show_type(*args):
    type_sel = ttb.curselection()
    type_index = int(type_sel[0])
    type = type_list[type_index]
    type_selection.set(type)


file_path = StringVar()
file_name = StringVar()


# Function to create file path and name


def file_path_function(*args):
    name_sel = nb.curselection()
    hand_sel = hb.curselection()
    dir_sel = db.curselection()
    trial_sel = tb.curselection()
    type_sel = ttb.curselection()

    name_index = int(name_sel[0])
    hand_index = int(hand_sel[0])
    dir_index = int(dir_sel[0])
    trial_index = int(trial_sel[0])
    type_index = int(type_sel[0])

    name = name_list[name_index]
    hand = hand_list[hand_index]
    dir = dir_list[dir_index]
    trial = trial_list[trial_index]
    type = type_list[type_index]

    file_name.set(f"{name}_{hand}_{dir}_{type}_{trial}")
    file_path.set(f"data/{name}/{hand}/{dir}/{type}/{trial}/")

    
# Makes a confirmation window on quit command


def quit_confirm():
    quit_box = messagebox.askquestion('Quit Test', 'Are you sure you want to quit?')
    if quit_box == 'yes':
        window.destroy()
    else:
        messagebox.showinfo('Return', 'The window will remain open. Please return to the test window '
                                      'and continue performing a trial.')


# WIDGET SECTION
# GUI Widgets in order of appearance

# Help button

help_button = Button(window, text='Help', width=5, height=1, bg='Gray',
                     activebackground='Yellow', activeforeground='Black', command=help_me)
help_button.grid(column=0, row=0, pady=15)

# Upper label

upper_label = Label(window, text='Input Data for Next Test')
upper_label.grid(column=0, row=0, pady=10, columnspan=5)

# Label for name listbox

nb_label = Label(window, text='Name')
nb_label.grid(column=0, row=1, pady=10)

# Name listbox

nb = Listbox(window, listvariable=name_list_sel, height=10, width=10, exportselection=0)
nb.grid(column=0, row=2, padx=15, pady=0)

# Label for hand listbox

hb_label = Label(window, text='Hand')
hb_label.grid(column=1, row=1, pady=5)

# Hand listbox

hb = Listbox(window, listvariable=hand_list_sel, height=10, width=10, exportselection=0)
hb.grid(column=1, row=2, padx=15, pady=0)

# Label for direction listbox

db_label = Label(window, text='Direction')
db_label.grid(column=2, row=1, pady=5)

# Direction listbox

db = Listbox(window, listvariable=dir_list_sel, height=10, width=10, exportselection=0)
db.grid(column=2, row=2, padx=15, pady=0)

# Label for trial listbox

tb_label = Label(window, text='Trial Number')
tb_label.grid(column=3, row=1, pady=5)

# Trial listbox

tb = Listbox(window, listvariable=trial_list_sel, height=10, width=10, exportselection=0)
tb.grid(column=3, row=2, padx=15, pady=0)

# Label for type listbox

ttb_label = Label(window, text='Trial Type')
ttb_label.grid(column=4, row=1, pady=5)

# Type listbox

ttb = Listbox(window, listvariable=type_list_sel, height=10, width=10, exportselection=0)
ttb.grid(column=4, row=2, padx=15, pady=0)

# Selection labels

name_selection_label = Label(window, textvariable=name_selection, bg='White')
name_selection_label.grid(column=0, row=3, pady=10)

hand_selection_label = Label(window, textvariable=hand_selection, bg='White')
hand_selection_label.grid(column=1, row=3, pady=5)

dir_selection_label = Label(window, textvariable=dir_selection, bg='White')
dir_selection_label.grid(column=2, row=3, pady=5)

trial_selection_label = Label(window, textvariable=trial_selection, bg='White')
trial_selection_label.grid(column=3, row=3, pady=5)

type_selection_label = Label(window, textvariable=type_selection, bg='White')
type_selection_label.grid(column=4, row=3, pady=5)

# File location label

file_label = Label(window, text='File name and path will be shown below (make selections and generate file location)')
file_label.grid(column=0, row=4, pady=15, columnspan=5)

# File name, location

file_name_label = Label(window, textvariable=file_name, bg='White')
file_name_label.grid(column=0, row=5, columnspan=5)

file_location_label = Label(window, textvariable=file_path, bg='White')
file_location_label.grid(column=0, row=6, columnspan=5)

foot_label = Label(window, text='OSU Robotics & Human Control Systems 2021', fg="Gray45")
foot_label.grid(column=0, row=9, pady=15, columnspan=5)

# Confirm, run, quit buttons

run_button = Button(window, text='Initialize Test', width=21, height=2, bg='Gray',
                    activebackground='Green', activeforeground='White')
run_button.grid(column=2, row=7, pady=15, columnspan=2)

confirm_button = Button(window, text='Generate File Name/Path', width=21, height=2, bg='Gray',
                        activebackground='Blue', activeforeground='White', command=file_path_function)
confirm_button.grid(column=0, row=7, pady=5, columnspan=2)

quit_button = Button(window, text='Quit', width=7, height=2, bg='Gray',
                     activebackground='Red', activeforeground='White', command=quit_confirm)
quit_button.grid(column=4, row=7, pady=5)

# Camera buttons

record_button = Button(window, text='Start Recording', width=21, height=2, bg='Gray',
                       activebackground='Red', activeforeground='White')
record_button.grid(column=0, row=8, pady=5, columnspan=2)

stop_button = Button(window, text='Stop Recording', width=21, height=2, bg='Gray',
                     activebackground='Red', activeforeground='White')
stop_button.grid(column=2, row=8, pady=5, columnspan=2)

files_button = Button(window, text='View Files', width=7, height=2, bg='Gray',
                      activebackground='White', activeforeground='Black')
files_button.grid(column=4, row=8, pady=5)


# BINDINGS

nb.bind('<<ListboxSelect>>', show_name)
hb.bind('<<ListboxSelect>>', show_hand)
db.bind('<<ListboxSelect>>', show_dir)
tb.bind('<<ListboxSelect>>', show_trial)
ttb.bind('<<ListboxSelect>>', show_type)

window.mainloop()

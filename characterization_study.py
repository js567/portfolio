"""

Characterization Study Data Helper Code

Code to receive input for five different characterization tests and save the results into specific csv files
for data processing.

One main window has buttons to open additional test windows. Each test type is defined in a function below (tilt and
complex tests are together under complex.) Each function contains all window code and is called by a button on the main
window.

The csv files will be saved in the format name_identifier_test.csv where name is user name, identifier is metadata (to
be determined in the future,) and test is test type. The files are created in the same location where the code is run.

Currently, if two tests of the same type are run subsequently, the code should be closed and run fresh to prevent a
possible bug. Tests of different types can be run for a total of one each every time the code is run.
This should be addressed in the future.


Written by Jack Stevenson in 2021.

"""

from tkinter import *
import csv

# creates main window
master = Tk()
master.title('Characterization Test Portal')

# sets the geometry of main window
master.geometry('530x215')

# trial variables
flick_trial_number = 1
squeeze_trial_number = 1
tilt_trial_number = 1
convex_trial_number = 1

hands = [
    'Select Hand',
    'barrett'
]

names = [
    'Select Name',
    'john'
]

# pull window function
def pull_window():

    # create and format new window
    pullwindow = Toplevel(master)
    pullwindow.title("Pull Test")
    pullwindow.geometry("270x570")

    # window title
    pull_title = Label(pullwindow, text='Pull Test', font='10')
    pull_title.grid(column=0, row=0, pady=20, columnspan=2)

    pull_name = StringVar("")
    pull_ident = StringVar("")

    # variables to save test data
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()

    # function to save test data
    def pull_submit():

        hand_name = pull_hand_entry.get()
        user_name = pull_name_entry.get()

        force1 = var1.get()
        force2 = var2.get()
        force3 = var3.get()
        force4 = var4.get()
        force5 = var5.get()
        force6 = var6.get()
        force7 = var7.get()
        force8 = var8.get()
        force9 = var9.get()
        force10 = var10.get()

        # saves data to a csv file with format name_identifier_pull.csv
        with open(hand_name + '_' + user_name + '_' + 'pull.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Trial', 'Force'])
            filewriter.writerow(['1', force1])
            filewriter.writerow(['2', force2])
            filewriter.writerow(['3', force3])
            filewriter.writerow(['4', force4])
            filewriter.writerow(['5', force5])
            filewriter.writerow(['6', force6])
            filewriter.writerow(['7', force7])
            filewriter.writerow(['8', force8])
            filewriter.writerow(['9', force9])
            filewriter.writerow(['10', force10])

        # destroy window (since all trials are saved simultaneously)
        pullwindow.destroy()

    # widgets in pull window
    pull_name_label = Label(pullwindow, text="Hand")
    pull_name_label.grid(column=0, row=1)

    pull_hand_entry = StringVar(pullwindow)
    pull_hand_entry.set(hands[0])  # default value

    pull_hand_menu = OptionMenu(pullwindow, pull_hand_entry, *hands)
    pull_hand_menu.grid(column=0, row=2)
    pull_hand_menu["borderwidth"] = 0
    pull_hand_menu["background"] = "Gray75"
    pull_hand_menu["activeforeground"] = "White"
    pull_hand_menu["activebackground"] = "Orange"
    pull_hand_menu["padx"]=20
    pull_hand_menu["width"] = 8

    pull_ident_label = Label(pullwindow, text="User Name")
    pull_ident_label.grid(column=1, row=1)

    pull_name_entry = StringVar(pullwindow)
    pull_name_entry.set(names[0])  # default value

    pull_name_menu = OptionMenu(pullwindow, pull_name_entry, *names)
    pull_name_menu.grid(column=1, row=2)
    pull_name_menu["borderwidth"] = 0
    pull_name_menu["background"] = "Gray75"
    pull_name_menu["activeforeground"] = "White"
    pull_name_menu["activebackground"] = "Orange"
    pull_name_menu["padx"] = 20
    pull_name_menu["width"] = 8

    trial_label = Label(pullwindow, text="Trial")
    trial_label.grid(column=0, row=3, padx=15, pady=10)

    label1 = Label(pullwindow, text='1')
    label2 = Label(pullwindow, text='2')
    label3 = Label(pullwindow, text='3')
    label4 = Label(pullwindow, text='4')
    label5 = Label(pullwindow, text='5')
    label6 = Label(pullwindow, text='6')
    label7 = Label(pullwindow, text='7')
    label8 = Label(pullwindow, text='8')
    label9 = Label(pullwindow, text='9')
    label10 = Label(pullwindow, text='10')

    label1.grid(column=0, row=4)
    label2.grid(column=0, row=5)
    label3.grid(column=0, row=6)
    label4.grid(column=0, row=7)
    label5.grid(column=0, row=8)
    label6.grid(column=0, row=9)
    label7.grid(column=0, row=10)
    label8.grid(column=0, row=11)
    label9.grid(column=0, row=12)
    label10.grid(column=0, row=13)

    info_label = Label(pullwindow, text='Enter force below:')
    info_label.grid(column=1, row=3, pady=0)

    entry1 = Entry(pullwindow, textvariable=var1, justify=CENTER, borderwidth=0, width=10,
                        font=('calibre', 10, 'normal'))
    entry2 = Entry(pullwindow, textvariable=var2, justify=CENTER, borderwidth=0, width=10,
                       font=('calibre', 10, 'normal'))
    entry3 = Entry(pullwindow, textvariable=var3, justify=CENTER, borderwidth=0, width=10,
                   font=('calibre', 10, 'normal'))
    entry4 = Entry(pullwindow, textvariable=var4, justify=CENTER, borderwidth=0, width=10,
                   font=('calibre', 10, 'normal'))
    entry5 = Entry(pullwindow, textvariable=var5, justify=CENTER, borderwidth=0, width=10,
                   font=('calibre', 10, 'normal'))
    entry6 = Entry(pullwindow, textvariable=var6, justify=CENTER, borderwidth=0, width=10,
                   font=('calibre', 10, 'normal'))
    entry7 = Entry(pullwindow, textvariable=var7, justify=CENTER, borderwidth=0, width=10,
                   font=('calibre', 10, 'normal'))
    entry8 = Entry(pullwindow, textvariable=var8, justify=CENTER, borderwidth=0, width=10,
                   font=('calibre', 10, 'normal'))
    entry9 = Entry(pullwindow, textvariable=var9, justify=CENTER, borderwidth=0, width=10,
                   font=('calibre', 10, 'normal'))
    entry10 = Entry(pullwindow, textvariable=var10, justify=CENTER, borderwidth=0, width=10,
                   font=('calibre', 10, 'normal'))

    entry1.grid(row=4, column=1, padx=10, pady=5)
    entry2.grid(row=5, column=1, padx=10, pady=5)
    entry3.grid(row=6, column=1, padx=10, pady=5)
    entry4.grid(row=7, column=1, padx=10, pady=5)
    entry5.grid(row=8, column=1, padx=10, pady=5)
    entry6.grid(row=9, column=1, padx=10, pady=5)
    entry7.grid(row=10, column=1, padx=10, pady=5)
    entry8.grid(row=11, column=1, padx=10, pady=5)
    entry9.grid(row=12, column=1, padx=10, pady=5)
    entry10.grid(row=13, column=1, padx=10, pady=5)

    sub_btn = Button(pullwindow, text="Submit Data", width=20, height=2, background='Gray75',
                     activebackground='Orange', activeforeground='White', borderwidth=0, command=pull_submit)
    sub_btn.grid(row=14, column=0, pady=20, columnspan=2)

# flick window function
def flick_window():

    # string variables to save test info
    #flick_name_var = StringVar("")
    #flick_test_var = StringVar("")
    flick_orient_var = StringVar("")

    flick_orient_var.set('null')

    # setup and format flick window
    flickwindow = Toplevel(master)
    flickwindow.title("Flick Test")
    flickwindow.geometry("435x505")

    flick_title = Label(flickwindow, text='Flick Test', font='10')
    flick_title.grid(column=0, row=0, pady=10, columnspan=3)

    flick_info = Label(flickwindow, text='Enter Flick Test data and press submit to record')
    flick_info.grid(column=0, row=1, pady=6, columnspan=3)

    # function to save flick data
    def flick_submit():
        if a_test.get() != 'null' and b_test.get() != 'null' and c_test.get() != 'null' and d_test.get() != 'null' \
                and e_test.get() != 'null' and f_test.get() != 'null' and g_test.get() != 'null' \
                    and h_test.get() != 'null' and flick_hand_entry.get() != 'Select Hand' and flick_name_entry != 'Select Name' \
                        and flick_orient_var.get() != 'null':

            global flick_trial_number

            hand = flick_hand_entry.get()
            name = flick_name_entry.get()
            flick_orient = flick_orient_var.get()

            outa = a_test.get()
            outb = b_test.get()
            outc = c_test.get()
            outd = d_test.get()
            oute = e_test.get()
            outf = f_test.get()
            outg = g_test.get()
            outh = h_test.get()

            # create reference line on csv file in format name_identifier_flick.csv
            if flick_trial_number == 1:
                with open(str(hand) + '_' + str(name) + '_' + str(flick_orient) + '_' + 'flick.csv', 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(['Trial', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

            # add a new line for each trial with data
            with open(str(hand) + '_' + str(name) + '_' + str(flick_orient) + '_' + 'flick.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([str(flick_trial_number), outa, outb, outc, outd, oute, outf, outg, outh])
                csvfile.close()

            # increase trial number
            flick_trial_number += 1

            # set label to display number of completed trials
            trial_label.configure(text="Completed trials: " + str(flick_trial_number - 1))

            a_test.set('null')
            b_test.set('null')
            c_test.set('null')
            d_test.set('null')
            e_test.set('null')
            f_test.set('null')
            g_test.set('null')
            h_test.set('null')

        else:
            errorwindow = Toplevel(flickwindow)
            errorwindow.title("Error")
            errorwindow.geometry("300x130")

            def return_to_test():
                errorwindow.destroy()

            error_label = Label(errorwindow, text='''
INSUFFIECIENT DATA ENTERED
Please check answers and resubmit''')
            error_label.grid(column=0, row=0, padx=30, pady=10)

            error_button = Button(errorwindow, text='Return to Test', borderwidth=0, bg='Gray75', command=return_to_test)
            error_button.grid(column=0, row=1)


    # function to destroy flick window
    def flick_close():

        flick_trial_number = 1

        flickwindow.destroy()

    # flick window widgets

    flick_hand_entry = StringVar(flickwindow)
    flick_hand_entry.set(hands[0])  # default value

    flick_hand_menu = OptionMenu(flickwindow, flick_hand_entry, *hands)
    flick_hand_menu.grid(column=0, row=3)
    flick_hand_menu["borderwidth"] = 0
    flick_hand_menu["background"] = "Gray75"
    flick_hand_menu["activeforeground"] = "White"
    flick_hand_menu["activebackground"] = "Orange"
    flick_hand_menu["padx"] = 20
    flick_hand_menu["width"] = 8

    flick_name_entry = StringVar(flickwindow)
    flick_name_entry.set(names[0])  # default value

    flick_name_menu = OptionMenu(flickwindow, flick_name_entry, *names)
    flick_name_menu.grid(column=0, row=5)
    flick_name_menu["borderwidth"] = 0
    flick_name_menu["background"] = "Gray75"
    flick_name_menu["activeforeground"] = "White"
    flick_name_menu["activebackground"] = "Orange"
    flick_name_menu["padx"] = 20
    flick_name_menu["width"] = 8

    flick_name_label = Label(flickwindow, text='Hand')
    #flick_name_entry = Entry(flickwindow, textvariable=flick_name_var, justify=CENTER, borderwidth=0,
    #                   font=('calibre', 10, 'normal'))
    flick_label = Label(flickwindow, text='Name')
    #flick_entry = Entry(flickwindow, textvariable=flick_test_var, justify=CENTER, borderwidth=0,
    #                    font=('calibre', 10, 'normal'))
    orientation_label = Label(flickwindow, text="Orientation")
    hor_radio = Radiobutton(flickwindow, text='horizontal', variable=flick_orient_var, value="horizontal",
                            borderwidth=0, activeforeground='White', activebackground="orange")
    vert_radio = Radiobutton(flickwindow,  text='vertical', variable=flick_orient_var, value="vertical",
                             borderwidth=0, activeforeground='White', activebackground="orange")
    trial_label = Label(flickwindow, text="Completed trials: " + str(flick_trial_number - 1), bg='White')
    sub_btn = Button(flickwindow, text="Submit Trial", width=20, height=1, background='Gray75',
                     activebackground='Green', activeforeground='White', borderwidth=0, command=flick_submit)
    end_btn = Button(flickwindow, text="Finish Test", width=20, height=1, background='Gray75',
                     activebackground='Red', activeforeground='White', borderwidth=0, command=flick_close)

    flick_name_label.grid(column=0, row=2, pady=0)
    #flick_name_entry.grid(row=3, column=0, padx=20, ipadx=20, ipady=2, pady=10)
    flick_label.grid(column=0, row=4, pady=0)
    #flick_entry.grid(row=5, column=0, padx=20, ipadx=20, ipady=2, pady=10)
    orientation_label.grid(column=0, row=6)
    hor_radio.grid(column=0, row=7)
    vert_radio.grid(column=0, row=8)
    trial_label.grid(column=0, row=9)
    sub_btn.grid(row=10, column=0, pady=0, padx=30)
    end_btn.grid(row=11, column=0, pady=0)

    dir_label = Label(flickwindow, text='Direction')
    dir_label.grid(column=1, row=2, pady=5)

    a = Label(flickwindow, text="a")
    b = Label(flickwindow, text="b")
    c = Label(flickwindow, text="c")
    d = Label(flickwindow, text="d")
    e = Label(flickwindow, text="e")
    f = Label(flickwindow, text="f")
    g = Label(flickwindow, text="g")
    h = Label(flickwindow, text="h")

    a.grid(column=1, row=3, pady=10)
    b.grid(column=1, row=4, pady=10)
    c.grid(column=1, row=5, pady=10)
    d.grid(column=1, row=6, pady=10)
    e.grid(column=1, row=7, pady=10)
    f.grid(column=1, row=8, pady=10)
    g.grid(column=1, row=9, pady=10)
    h.grid(column=1, row=10, pady=10)

    sb_label = Label(flickwindow, text='Outcome')
    sb_label.grid(column=2, row=2, pady=5)

    # set of outcomes that can be selected on menus
    outcomes = [
        "null",
        "success",
        "partial",
        "failure"
    ]

    a_test = StringVar(flickwindow)
    a_test.set(outcomes[0])  # default value

    a_menu = OptionMenu(flickwindow, a_test, *outcomes)
    a_menu.grid(column=2, row=3)
    a_menu["borderwidth"] = 0
    a_menu["background"] = "Gray75"
    a_menu["activeforeground"] = "White"
    a_menu["activebackground"] = "Orange"
    a_menu["width"]=8

    b_test = StringVar(flickwindow)
    b_test.set(outcomes[0])  # default value

    b_menu = OptionMenu(flickwindow, b_test, *outcomes)
    b_menu.grid(column=2, row=4)
    b_menu["borderwidth"] = 0
    b_menu["background"] = "Gray75"
    b_menu["activeforeground"] = "White"
    b_menu["activebackground"] = "Orange"
    b_menu["width"]=8

    c_test = StringVar(flickwindow)
    c_test.set(outcomes[0])  # default value

    c_menu = OptionMenu(flickwindow, c_test, *outcomes)
    c_menu.grid(column=2, row=5)
    c_menu["borderwidth"] = 0
    c_menu["background"] = "Gray75"
    c_menu["activeforeground"] = "White"
    c_menu["activebackground"] = "Orange"
    c_menu["width"]=8

    d_test = StringVar(flickwindow)
    d_test.set(outcomes[0])  # default value

    d_menu = OptionMenu(flickwindow, d_test, *outcomes)
    d_menu.grid(column=2, row=6)
    d_menu["borderwidth"] = 0
    d_menu["background"] = "Gray75"
    d_menu["activeforeground"] = "White"
    d_menu["activebackground"] = "Orange"
    d_menu["width"]=8

    e_test = StringVar(flickwindow)
    e_test.set(outcomes[0])  # default value

    e_menu = OptionMenu(flickwindow, e_test, *outcomes)
    e_menu.grid(column=2, row=7)
    e_menu["borderwidth"] = 0
    e_menu["background"] = "Gray75"
    e_menu["activeforeground"] = "White"
    e_menu["activebackground"] = "Orange"
    e_menu["width"]=8

    f_test = StringVar(flickwindow)
    f_test.set(outcomes[0])  # default value

    f_menu = OptionMenu(flickwindow, f_test, *outcomes)
    f_menu.grid(column=2, row=8)
    f_menu["borderwidth"] = 0
    f_menu["background"] = "Gray75"
    f_menu["activeforeground"] = "White"
    f_menu["activebackground"] = "Orange"
    f_menu["width"]=8

    g_test = StringVar(flickwindow)
    g_test.set(outcomes[0])  # default value

    g_menu = OptionMenu(flickwindow, g_test, *outcomes)
    g_menu.grid(column=2, row=9)
    g_menu["borderwidth"] = 0
    g_menu["background"] = "Gray75"
    g_menu["activeforeground"] = "White"
    g_menu["activebackground"] = "Orange"
    g_menu["width"]=8

    h_test = StringVar(flickwindow)
    h_test.set(outcomes[0])  # default value

    h_menu = OptionMenu(flickwindow, h_test, *outcomes)
    h_menu.grid(column=2, row=10)
    h_menu["borderwidth"] = 0
    h_menu["background"] = "Gray75"
    h_menu["activeforeground"] = "White"
    h_menu["activebackground"] = "Orange"
    h_menu["width"]=8

# squeeze window function
def squeeze_window():

    # string variables to store test data
    squeeze_name_var = StringVar("")
    squeeze_test_var = StringVar("")

    # setup and format squeeze window
    squeezewindow = Toplevel(master)
    squeezewindow.title("Squeeze Test")
    squeezewindow.geometry("420x460")

    squeeze_title = Label(squeezewindow, text='Squeeze Test', font='10')
    squeeze_title.grid(column=0, row=0, pady=10, columnspan=3)

    squeeze_info = Label(squeezewindow, text='Enter Squeeze Test data and press submit to record')
    squeeze_info.grid(column=0, row=1, pady=6, columnspan=3)

    # function to submit squeeze data
    def squeeze_submit():
        if a_var.get() != 0 and b_var.get() != 0 and c_var.get() != 0 and d_var.get() != 0 and e_var.get() != 0 \
                and f_var.get() != 0 and g_var.get() != 0 and h_var.get() != 0 and squeeze_hand.get() \
                != 'Select Hand' and squeeze_name != 'Select Name':

            global squeeze_trial_number

            hand = squeeze_hand.get()
            name = squeeze_name.get()

            out_a = a_var.get()
            out_b = b_var.get()
            out_c = c_var.get()
            out_d = d_var.get()
            out_e = e_var.get()
            out_f = f_var.get()
            out_g = g_var.get()
            out_h = h_var.get()

            # create reference line in csv file with format name_identifier_squeeze.csv
            if squeeze_trial_number == 1:
                with open(str(hand) + '_' + str(name) + '_' + 'squeeze.csv', 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(['Trial', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

            # add new line for each trial with data
            with open(str(hand) + '_' + str(name) + '_' + 'squeeze.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([str(squeeze_trial_number), out_a, out_b, out_c, out_d, out_e, out_f,
                                     out_g, out_h])
                csvfile.close()

            # increase trial number per trial
            squeeze_trial_number += 1

            # set trial label to accurate trial number
            squeeze_trial_label.configure(text="Completed trials: " + str(squeeze_trial_number - 1))

        else:
            errorwindow = Toplevel(squeezewindow)
            errorwindow.title("Error")
            errorwindow.geometry("300x130")

            def return_to_test():
                errorwindow.destroy()

            error_label = Label(errorwindow, text='''
INSUFFIECIENT DATA ENTERED
Please check answers and resubmit''')
            error_label.grid(column=0, row=0, padx=30, pady=10)

            error_button = Button(errorwindow, text='Return to Test', borderwidth=0, bg='Gray75',
                                  command=return_to_test)
            error_button.grid(column=0, row=1)

        # function to destroy squeeze window
    def squeeze_close():

        squeeze_trial_number = 1

        squeezewindow.destroy()

    # squeeze window widgets
    squeeze_name_label = Label(squeezewindow, text='Hand')
    squeeze_name_entry = Entry(squeezewindow, textvariable=squeeze_name_var, justify=CENTER, borderwidth=0,
                       font=('calibre', 10, 'normal'))
    squeeze_label = Label(squeezewindow, text='Name')
    squeeze_entry = Entry(squeezewindow, textvariable=squeeze_test_var, justify=CENTER, borderwidth=0,
                        font=('calibre', 10, 'normal'))
    squeeze_trial_label = Label(squeezewindow, text="Completed trials: " + str(squeeze_trial_number - 1), bg='White')
    sub_btn = Button(squeezewindow, text="Submit Trial", width=20, height=1, background='Gray75',
                     activebackground='Green', activeforeground='White', borderwidth=0, command=squeeze_submit)
    end_btn = Button(squeezewindow, text="Finish Test", width=20, height=1, background='Gray75',
                     activebackground='Red', activeforeground='White', borderwidth=0, command=squeeze_close)

    squeeze_hand = StringVar(squeezewindow)
    squeeze_hand.set(hands[0])  # default value

    squeeze_hand_menu = OptionMenu(squeezewindow, squeeze_hand, *hands)
    squeeze_hand_menu.grid(column=0, row=3)
    squeeze_hand_menu["borderwidth"] = 0
    squeeze_hand_menu["background"] = "Gray75"
    squeeze_hand_menu["activeforeground"] = "White"
    squeeze_hand_menu["activebackground"] = "Orange"
    squeeze_hand_menu["padx"] = 20
    squeeze_hand_menu["width"] = 8

    squeeze_name = StringVar(squeezewindow)
    squeeze_name.set(names[0])  # default value

    squeeze_name_menu = OptionMenu(squeezewindow, squeeze_name, *names)
    squeeze_name_menu.grid(column=0, row=5)
    squeeze_name_menu["borderwidth"] = 0
    squeeze_name_menu["background"] = "Gray75"
    squeeze_name_menu["activeforeground"] = "White"
    squeeze_name_menu["activebackground"] = "Orange"
    squeeze_name_menu["padx"] = 20
    squeeze_name_menu["width"] = 8

    squeeze_name_label.grid(column=0, row=2, pady=0)
    #squeeze_name_entry.grid(row=3, column=0, padx=20, ipadx=20, ipady=2, pady=10)
    squeeze_label.grid(column=0, row=4, pady=0)
    #squeeze_entry.grid(row=5, column=0, padx=20, ipadx=20, ipady=2, pady=10)
    squeeze_trial_label.grid(column=0, row=8)
    sub_btn.grid(row=9, column=0, pady=0, padx=25)
    end_btn.grid(row=10, column=0, pady=10)

    dir_label = Label(squeezewindow, text='Direction')
    dir_label.grid(column=1, row=2, pady=5)

    a = Label(squeezewindow, text="a")
    b = Label(squeezewindow, text="b")
    c = Label(squeezewindow, text="c")
    d = Label(squeezewindow, text="d")
    e = Label(squeezewindow, text="e")
    f = Label(squeezewindow, text="f")
    g = Label(squeezewindow, text="g")
    h = Label(squeezewindow, text="h")

    a.grid(column=1, row=3, pady=10)
    b.grid(column=1, row=4, pady=10)
    c.grid(column=1, row=5, pady=10)
    d.grid(column=1, row=6, pady=10)
    e.grid(column=1, row=7, pady=10)
    f.grid(column=1, row=8, pady=10)
    g.grid(column=1, row=9, pady=10)
    h.grid(column=1, row=10, pady=10)

    sb_label = Label(squeezewindow, text='Pull length')
    sb_label.grid(column=2, row=2, pady=5)

    a_var = StringVar(squeezewindow)
    a_var.set(0)
    a_entry = Entry(squeezewindow, textvariable=a_var, justify=CENTER, borderwidth=0, width=12)
    a_entry.grid(column=2, row=3)

    b_var = StringVar(squeezewindow)
    b_var.set(0)
    b_entry = Entry(squeezewindow, textvariable=b_var, justify=CENTER, borderwidth=0, width=12)
    b_entry.grid(column=2, row=4)

    c_var = StringVar(squeezewindow)
    c_var.set(0)
    c_entry = Entry(squeezewindow, textvariable=c_var, justify=CENTER, borderwidth=0, width=12)
    c_entry.grid(column=2, row=5)

    d_var = StringVar(squeezewindow)
    d_var.set(0)
    d_entry = Entry(squeezewindow, textvariable=d_var, justify=CENTER, borderwidth=0, width=12)
    d_entry.grid(column=2, row=6)

    e_var = StringVar(squeezewindow)
    e_var.set(0)
    e_entry = Entry(squeezewindow, textvariable=e_var, justify=CENTER, borderwidth=0, width=12)
    e_entry.grid(column=2, row=7)

    f_var = StringVar(squeezewindow)
    f_var.set(0)
    f_entry = Entry(squeezewindow, textvariable=f_var, justify=CENTER, borderwidth=0, width=12)
    f_entry.grid(column=2, row=8)

    g_var = StringVar(squeezewindow)
    g_var.set(0)
    g_entry = Entry(squeezewindow, textvariable=g_var, justify=CENTER, borderwidth=0, width=12)
    g_entry.grid(column=2, row=9)

    h_var = StringVar(squeezewindow)
    h_var.set(0)
    h_entry = Entry(squeezewindow, textvariable=h_var, justify=CENTER, borderwidth=0, width=12)
    h_entry.grid(column=2, row=10)

# function to create tilt window
def tilt_window():

    tilt_name_var = StringVar("")
    tilt_test_var = StringVar("")
    tilt_time_var = StringVar("")

    tilt_time_var.set(0)

    # create and format tilt window
    tiltwindow = Toplevel(master)
    tiltwindow.title("Spray Test")
    tiltwindow.geometry("245x480")

    tilt_title = Label(tiltwindow, text='Spray Test', font='10')
    tilt_title.grid(column=0, row=0, pady=10)

    tilt_info = Label(tiltwindow, text='''Record time with stopwatch
    Enter and submit data''', padx=30)
    tilt_info.grid(column=0, row=1, pady=5)

    # function to submit tilt data
    def tilt_submit():

        if tilt_time_var.get !=0 and tilt_hand.get() != "Select Hand" and tilt_name.get() != 'Select Name':
            global tilt_trial_number

            name = tilt_name_var.get()
            identifier = tilt_test_var.get()
            time = tilt_time_var.get()

            # create reference row in csv file name_identifier_tilt.csv
            if tilt_trial_number == 1:
                with open(str(name) + '_' + str(identifier) + '_' + 'spray.csv', 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(['Trial', 'Time'])

            # add a new row to csv file for each trial
            with open(str(name) + '_' + str(identifier) + '_' + 'spray.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([str(tilt_trial_number), time])
                csvfile.close()

            # increase trial number for each trial
            tilt_trial_number += 1

            # set trial label to new trial number
            tilt_trial_label.configure(text="Completed trials: " + str(tilt_trial_number - 1))

        else:
            errorwindow = Toplevel(tiltwindow)
            errorwindow.title("Error")
            errorwindow.geometry("300x130")

            def return_to_test():
                errorwindow.destroy()

            error_label = Label(errorwindow, text='''
INSUFFIECIENT DATA ENTERED
Please check answers and resubmit''')
            error_label.grid(column=0, row=0, padx=30, pady=10)

            error_button = Button(errorwindow, text='Return to Test', borderwidth=0, bg='Gray75',
                                  command=return_to_test)
            error_button.grid(column=0, row=1)

    # function to destroy tilt window
    def tilt_close():

        tiltwindow.destroy()
        tilt_trial_number = 1

    tilt_hand = StringVar(tiltwindow)
    tilt_hand.set(hands[0])  # default value

    tilt_hand_menu = OptionMenu(tiltwindow, tilt_hand, *hands)
    tilt_hand_menu.grid(column=0, row=3)
    tilt_hand_menu["borderwidth"] = 0
    tilt_hand_menu["background"] = "Gray75"
    tilt_hand_menu["activeforeground"] = "White"
    tilt_hand_menu["activebackground"] = "Orange"
    tilt_hand_menu["padx"] = 20
    tilt_hand_menu["width"] = 8

    tilt_name = StringVar(tiltwindow)
    tilt_name.set(names[0])  # default value

    tilt_name_menu = OptionMenu(tiltwindow, tilt_name, *names)
    tilt_name_menu.grid(column=0, row=5)
    tilt_name_menu["borderwidth"] = 0
    tilt_name_menu["background"] = "Gray75"
    tilt_name_menu["activeforeground"] = "White"
    tilt_name_menu["activebackground"] = "Orange"
    tilt_name_menu["padx"] = 20
    tilt_name_menu["width"] = 8

    # tilt window widgets
    tilt_name_label = Label(tiltwindow, text='Hand')
    tilt_name_entry = Entry(tiltwindow, textvariable=tilt_name_var, justify=CENTER, borderwidth=0,
                               font=('calibre', 10, 'normal'))
    tilt_label = Label(tiltwindow, text='Name')
    tilt_entry = Entry(tiltwindow, textvariable=tilt_test_var, justify=CENTER, borderwidth=0,
                          font=('calibre', 10, 'normal'))
    tilt_time_label = Label(tiltwindow, text='Enter elapsed time:')
    tilt_time_entry = Entry(tiltwindow, textvariable=tilt_time_var, justify=CENTER, borderwidth=0, width=10,
                       font=('calibre', 10, 'normal'))
    tilt_trial_label = Label(tiltwindow, text="Completed trials: " + str(tilt_trial_number - 1), bg='White', pady=5)
    # call tilt submit function
    sub_btn = Button(tiltwindow, text="Submit Trial", width=20, height=1, background='Gray75',
                     activebackground='Green', activeforeground='White', borderwidth=0, command=tilt_submit)
    # call tilt close function
    end_btn = Button(tiltwindow, text="Finish Test", width=20, height=1, background='Gray75',
                     activebackground='Red', activeforeground='White', borderwidth=0, command=tilt_close)

    tilt_name_label.grid(column=0, row=2, pady=10)
    #tilt_name_entry.grid(row=3, column=0, padx=20, ipadx=20, ipady=2, pady=10)
    tilt_label.grid(column=0, row=4, pady=10)
    #tilt_entry.grid(row=5, column=0, padx=20, ipadx=20, ipady=2, pady=10)
    tilt_time_label.grid(column=0, row=6, pady=10)
    tilt_time_entry.grid(row=7, column=0, padx=20, ipadx=20, ipady=2, pady=0)
    tilt_trial_label.grid(column=0, row=10, pady=25)
    sub_btn.grid(row=11, column=0, pady=0)
    end_btn.grid(row=12, column=0, pady=15)

# function to create convex window
def convex_window():

    # string variables to save test data
    convex_name_var = StringVar("")
    convex_test_var = StringVar("")
    convex_time_var = StringVar("")
    convex_pen_var = StringVar("")
    convex_time_var_bowl = StringVar("")
    convex_pen_var_bowl = StringVar("")

    convex_time_var.set(0)
    convex_pen_var.set(0)
    convex_time_var_bowl.set(0)
    convex_pen_var_bowl.set(0)

    # create and format convex window
    convexwindow = Toplevel(master)
    convexwindow.title("Pen Test")
    convexwindow.geometry("270x515")

    convex_title = Label(convexwindow, text='Pen Test', font='10')
    convex_title.grid(column=0, row=0, pady=10, columnspan=2)

    convex_info = Label(convexwindow, text='''Start a stopwatch and record end time
Enter data and press submit to record''')
    convex_info.grid(column=0, row=1, pady=5, columnspan=2)

    def convex_submit():

        if convex_name.get() != 'Select Name' and convex_hand.get() != 'Select Hand' and convex_time_var.get() != 0 \
                and convex_pen_entry.get() != 0 and convex_time_var_bowl.get() !=0 and convex_pen_var_bowl.get() != 0:

            global convex_trial_number

            hand = convex_hand.get()
            name = convex_name.get()
            paper_time = convex_time_var.get()
            paper_drops = convex_pen_var.get()
            bowl_time = convex_time_var.get()
            bowl_drops = convex_pen_var.get()

            # add reference row to csv file name_identifier_convex.csv
            if convex_trial_number == 1:
                with open(str(hand) + '_' + str(name) + '_' + 'pen.csv', 'a') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(['Trial', 'Paper Time', 'Paper Drops', 'Bowl Time', 'Bowl Drops'])

            # add new data rows to csv file for each trial
            with open(str(hand) + '_' + str(name) + '_' + 'pen.csv', 'a') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([str(convex_trial_number), paper_time, paper_drops, bowl_time, bowl_drops])
                csvfile.close()

            # set new trial number
            convex_trial_number += 1

            # set trial label to new value
            convex_trial_label.configure(text="Completed trials: " + str(convex_trial_number - 1))

        else:
            errorwindow = Toplevel(convexwindow)
            errorwindow.title("Error")
            errorwindow.geometry("300x130")

            def return_to_test():
                errorwindow.destroy()

            error_label = Label(errorwindow, text='''
INSUFFIECIENT DATA ENTERED
Please check answers and resubmit''')
            error_label.grid(column=0, row=0, padx=30, pady=10)

            error_button = Button(errorwindow, text='Return to Test', borderwidth=0, bg='Gray75',
                                  command=return_to_test)
            error_button.grid(column=0, row=1)

    # function to destroy convex window
    def tilt_close():

        convexwindow.destroy()
        tilt_trial_number = 1

    # convex window widgets

    convex_hand = StringVar(convexwindow)
    convex_hand.set(hands[0])  # default value

    convex_hand_menu = OptionMenu(convexwindow, convex_hand, *hands)
    convex_hand_menu.grid(column=0, row=3)
    convex_hand_menu["borderwidth"] = 0
    convex_hand_menu["background"] = "Gray75"
    convex_hand_menu["activeforeground"] = "White"
    convex_hand_menu["activebackground"] = "Orange"
    convex_hand_menu["padx"] = 20
    convex_hand_menu["width"] = 8

    convex_name = StringVar(convexwindow)
    convex_name.set(names[0])  # default value

    convex_name_menu = OptionMenu(convexwindow, convex_name, *names)
    convex_name_menu.grid(column=1, row=3)
    convex_name_menu["borderwidth"] = 0
    convex_name_menu["background"] = "Gray75"
    convex_name_menu["activeforeground"] = "White"
    convex_name_menu["activebackground"] = "Orange"
    convex_name_menu["padx"] = 20
    convex_name_menu["width"] = 8

    convex_name_label = Label(convexwindow, text='Hand')
    convex_name_entry = Entry(convexwindow, textvariable=convex_name_var, justify=CENTER, borderwidth=0,
                               font=('calibre', 10, 'normal'))
    convex_label = Label(convexwindow, text='Name')
    convex_entry = Entry(convexwindow, textvariable=convex_test_var, justify=CENTER, borderwidth=0,
                          font=('calibre', 10, 'normal'))
    left_label = Label(convexwindow, text='FLAT PAPER')
    right_label = Label(convexwindow, text='BOWL')
    convex_time_label = Label(convexwindow, text='Flat Paper Time')
    convex_time_entry = Entry(convexwindow, textvariable=convex_time_var, justify=CENTER, borderwidth=0, width=12,
                       font=('calibre', 10, 'normal'))
    convex_pen_label = Label(convexwindow, text='Flat Paper Drops')
    convex_pen_entry = Entry(convexwindow, textvariable=convex_pen_var, justify=CENTER, borderwidth=0, width=12,
                              font=('calibre', 10, 'normal'))
    convex_time_label_bowl = Label(convexwindow, text='Bowl Time')
    convex_time_entry_bowl = Entry(convexwindow, textvariable=convex_time_var_bowl, justify=CENTER, borderwidth=0, width=12,
                              font=('calibre', 10, 'normal'))
    convex_pen_label_bowl = Label(convexwindow, text='Bowl Drops')
    convex_pen_entry_bowl = Entry(convexwindow, textvariable=convex_pen_var_bowl, justify=CENTER, borderwidth=0, width=12,
                             font=('calibre', 10, 'normal'))
    convex_trial_label = Label(convexwindow, text="Completed trials: " + str(convex_trial_number - 1), bg='White')
    # call convex submit function
    sub_btn = Button(convexwindow, text="Submit Trial", width=20, height=1, background='Gray75',
                     activebackground='Green', activeforeground='White', borderwidth=0, command=convex_submit)
    # call convex close function
    end_btn = Button(convexwindow, text="Finish Test", width=20, height=1, background='Gray75',
                     activebackground='Red', activeforeground='White', borderwidth=0, command=tilt_close)

    convex_name_label.grid(column=0, row=2, pady=10)
    #convex_name_entry.grid(row=3, column=0, pady=10)
    convex_label.grid(column=1, row=2, pady=0)
    #convex_entry.grid(row=5, column=0, pady=10)
    left_label.grid(column=0, row=5, pady=10)
    right_label.grid(column=1, row=5)
    convex_time_label.grid(column=0, row=6, pady=0)
    convex_time_entry.grid(row=7, column=0, pady=10)
    convex_pen_label.grid(column=0, row=8, pady=0)
    convex_pen_entry.grid(row=9, column=0, pady=10)
    convex_time_label_bowl.grid(column=1, row=6, pady=0)
    convex_time_entry_bowl.grid(row=7, column=1, pady=10)
    convex_pen_label_bowl.grid(column=1, row=8, pady=0)
    convex_pen_entry_bowl.grid(row=9, column=1, pady=10)
    convex_trial_label.grid(column=0, row=10, columnspan=2, pady=25)
    sub_btn.grid(row=11, column=0, pady=0, columnspan=2)
    end_btn.grid(row=12, column=0, pady=15, columnspan=2)

# main window widgets and setup

upper_label = Label(master, text='Characterization Test Portal', font='10')
upper_label.grid(column=0, row=0, pady=20, columnspan=10)

info_label = Label(master, text='Make a test selection below:', foreground="Gray40")
info_label.grid(column=0, row=2, pady=0, columnspan=10)

foot_label = Label(master, text='OSU Robotics & Human Control Systems 2021', foreground="Gray40")
foot_label.grid(column=0, row=7, pady=0, columnspan=10)

# call pull function
pull_button = Button(master, text="Pull Test", width=10, height=2, background='Gray75',
             activebackground='Orange', activeforeground='White', borderwidth=0, command=pull_window)
pull_button.grid(column=0, row=3, columnspan=2, pady=20)

# call flick function
flick_button = Button(master, text="Flick Test", width=10, height=2, background='Gray75',
             activebackground='Orange', activeforeground='White', borderwidth=0, command=flick_window)
flick_button.grid(column=2, row=3, columnspan=2, pady=20)

# call squeeze function
squeeze_button = Button(master, text="Squeeze Test", width=10, height=2, background='Gray75',
             activebackground='Orange', activeforeground='White', borderwidth=0, command=squeeze_window)
squeeze_button.grid(column=4, row=3, columnspan=2, pady=20)

# call complex function
complex_button = Button(master, text="Spray Test", width=10, height=2, background='Gray75',
             activebackground='Orange', activeforeground='White', borderwidth=0, command=tilt_window)
complex_button.grid(column=6, row=3, columnspan=2, pady=20)

complex_button = Button(master, text="Pen Test", width=10, height=2, background='Gray75',
             activebackground='Orange', activeforeground='White', borderwidth=0, command=convex_window)
complex_button.grid(column=8, row=3, columnspan=2, pady=20)


# mainloop to run main window
mainloop()

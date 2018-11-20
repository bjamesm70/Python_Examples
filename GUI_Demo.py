# GUI_Demo.py

# Lesson 90: Advanced GUI Example

# - A note about 'weight' with tkinter/grid use from:
# (http://effbot.org/tkinterbook/grid.htm)
#
# weight=
# A relative weight used to distribute additional space between columns. A
# column with the weight 2 will grow twice as fast as a column with weight
# 1. The default is 0, which means that the column will not grow at all.
#
# From me:
# So, it affects how extra space is distributed not the standard size of
# the row/column.  This can come into affect when the window resizes.

# - To keep a row close to its neighbor, give them both a low row weight.


# - Jim
# (Contact Info)

import tkinter    # Toolkit Interface
import os         # To work with the OS.

# Our main GUI window:
main_window = tkinter.Tk()

main_window.title("Grid Demo")
main_window.geometry('640x480-8-200')

# Add some padding around the left, and right side of the window:
main_window['padx'] = 8

# Add a text label, and set its width equal to the 1st 3 columns.
label = tkinter.Label(main_window, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# Set up some column widths:
# Column 1 = scroll bar column.
# Set its weight low so that it does not expand, or contract much.
main_window.columnconfigure(0, weight=1000)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1000)
main_window.columnconfigure(3, weight=600)
main_window.columnconfigure(4, weight=1000)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

################################################################
# Create a list box that spans 2 rows, and fills its grid area #
################################################################

# (sticky -> north, south, east, and west):
file_list = tkinter.Listbox(main_window)
file_list.grid(row=1, column=0, sticky='nsew', rowspan=2)
file_list.config(border=2, relief='sunken')

# Get the files/dirs in "/usr/bin" to file our list box.
# (For Windows, use: '/Windows/System32')
for item in os.listdir('/usr/bin'):
    # Add the file/dir to the end of the list box.
    file_list.insert(tkinter.END, item)

####################################
# Add a scroll bar to the list box #
####################################

# "command=file_list.yview" is required to be able to move the
# scroll bar.  It will cause the list box to scroll also.  However,
# you also need to add in the "file_list['yscrollcommand'] = file_list_scroll.set"
# for that to work.
file_list_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL, command=file_list.yview)
file_list_scroll.grid(row=1, column=1, sticky='nsw', rowspan=2)

# The list box has a property called "yscrollcommand".
# Use it to tie the scroll bar with the list box.
# This will reposition the scroll bar if you move through the list,
# reposition the list if you move through the scroll bar.
# Note: see above about: "command=file_list.yview"
file_list['yscrollcommand'] = file_list_scroll.set

########################################
# Create a frame for the radio buttons #
########################################

options_frame = tkinter.LabelFrame(main_window, text="File Details")

# Place it:
# sticky --> 'ne' --> position in the northeast corner of that grid square.
options_frame.grid(row=1, column=2, sticky='ne')

#########################
# Add the radio buttons #
#########################

radio_button_value = tkinter.IntVar()
radio_button_value.set(3)    # Default to the 3rd radio button which we are about to add.

# The buttons: (They are put in 'options_frame'.)
radio1 = tkinter.Radiobutton(options_frame, text="Filename", value=1, variable=radio_button_value)
radio2 = tkinter.Radiobutton(options_frame, text="Path", value=2, variable=radio_button_value)
radio3 = tkinter.Radiobutton(options_frame, text="Timestamp", value=3, variable=radio_button_value)

# Assign them locations:
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Show the result of the radio button/list box choices:
# (Just a label for the result:
result_label = tkinter.Label(main_window, text="Result")
result_label.grid(row=2, column=2, sticky='nw')

#####################
# Add a results box #
#####################

# The result:
result = tkinter.Entry(main_window)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners.
# Note: a frame has no size if you don't put anything in it!
time_frame = tkinter.LabelFrame(main_window, text="Time")
time_frame.grid(row=3, column=0, sticky='new')

######################
# Add a time chooser #
######################

# The time spinners:
hour_spinner   = tkinter.Spinbox(time_frame, width=2, values=tuple(range(0, 24)))
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)

# Add some internal padding to the left/right borders of the frame.
# (and a small amount of y padding)
time_frame['padx'] = 36
time_frame['pady'] = 2

# Add the time spinners w/ ":" separators.
hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=":").grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=":").grid(row=0, column=3)
second_spinner.grid(row=0, column=4)


######################
# Add a date chooser #
######################

# The date frame:
date_frame = tkinter.Frame(main_window)
date_frame.grid(row=4, column=0, sticky='new')

# Some labels to show w/i the frame:
day_label   = tkinter.Label(date_frame, text="Day")
month_label = tkinter.Label(date_frame, text="Month")
year_label  = tkinter.Label(date_frame, text="Year")

day_label.grid(row=0, column=0, sticky='w')
month_label.grid(row=0, column=1, sticky='w')
year_label.grid(row=0, column=2, sticky='w')

# Create the date spinners:
month_tuple = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

day_spinner   = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
month_spinner = tkinter.Spinbox(date_frame, width=5, values=month_tuple)
year_spinner  = tkinter.Spinbox(date_frame, width=5, from_=2000, to=2099)

day_spinner.grid(row=1, column=0)
month_spinner.grid(row=1, column=1)
year_spinner.grid(row=1, column=2)

############################
# Add OK, & Cancel Buttons #
############################

# Close the app when the "cancel" button is pressed: command=main_window.quit
# or command=main_window.destroy.
# Note: no parens!
ok_button     = tkinter.Button(main_window, text="OK")
#cancel_button = tkinter.Button(main_window, text="Cancel", command=main_window.quit)
cancel_button = tkinter.Button(main_window, text="Cancel", command=main_window.destroy)

ok_button.grid(row=4, column=3, sticky='e')
cancel_button.grid(row=4, column=4, sticky='w')

# Display the window in the FG of the program.
main_window.mainloop()

# Set for confirmation, print the radio button selected.
print(radio_button_value.get())
# Jukebox_Ver1.py

# Lesson 176: Simple Database Browser

# This program makes a simple GUI window that
# allows you to select artists, their albums,
# and the songs.  It is a fake interface to
# a jukebox.

# This version uses 2 functions (get_albums, and
# get_songs) that are very similar, and will be merged into
# common code in the future.

# Note: There is a change to the way python 3.7 (for mac) handles the bind/select:
# code: albums_list.bind('<<ListboxSelect>>', get_songs)
# and:  albums_list.bind('<<ListboxSelect>>', get_songs)
# When you select a value in another scroll box, it causes any other scroll
# box's selected value to become unselected, and to
# generate an event that calls your function associated
# with that other scroll box.  The event passed has
# a value of nothing selected.  As a result, "curselection()",
# w/i the function, returns empty.
# You need to code around that.
# It was not like that in previous versions of python.

# - Jim
# (contact info)

import sqlite3
import tkinter    # python 3 naming of library.


###########
# Classes #
###########


class ScrollBox(tkinter.Listbox):
    # Inherits from tkinter.Listbox
    
    # This class will combine a listbox, & a scroll bar.
    # They will share the same location on the grid
    # with the the scroll bar being on the right, and
    # the list box being on the left.
    
    def __init__(self, window, **kwargs):
    
        # Call the parent's init function 1st:
        super().__init__(window, **kwargs)
        
        # Add in the scroll bar below:
        
        # This class will have a list box, and a scroll bar.  So, the "self.yview"
        # will refer to the list box's yview.
        # (This says that when you move the scroll bar, also run the file_list's "yview" function.)
        
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)
        
    # Overriding from Listbox:
    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # Regarding the "grid" function:
        # From: https://www.tutorialspoint.com/python/tk_grid.htm
        # This geometry manager organizes widgets in a table-like structure in the parent widget.
        
        # 1st call the parent class' function to place the list box in the window's grid.
        # Place the list box in whatever row, and column the user specifies.
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
    
        # Now add our scrollbar (which was created in the init function) to the same
        # location on the window's grid.
        # Put the scroll bar in the same grid as the list box.  However, stick to the east side.
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        # Link the list back to the scroll bar:  When the list box contents adjust
        # (due to the person using the arrow keys to move w/i it, or the contents
        # updating), update the scroll bar.
        # Note: Adjusting the list box due to the scroll bar moving is handled
        # in the init function with: command=self.yview)
        self['yscrollcommand'] = self.scrollbar.set


#########################
# End Class Definitions #
#########################


########################
# Function Definitions #
########################

def get_albums(event):
    # This function will populate the "albums"
    # scroll box with the albums by the artist/band
    # selected int the "artists" scroll box.

    # The 'widget' variable that holds the tkinter object/widget
    # that is associated with the action; in our case, the
    # "artists" scroll box.
    list_box = event.widget

    # From the 'artist' list box, get the presently selected artist/band.
    # Notes:
    # 1) list_box.curselection() --> will return a list of POSITIONS of all the selected items.
    # 2) As it's possible to select more than 1 item from list box by
    # holding down the shift, or other keys, we use [0] to grab the 1st
    # band/artist from the list.
    # 3) list_box.get(index) --> Once we have the index, get the value at that location.
    # 4) you need the "," after 'list_box(index)' to return a tuple.
    # The SELECT query needs a tuple.
    
    # Note: There is a change to the way python 3.7 (for mac)
    # handles the bind/select.  When you select
    # a value in another scroll box, it causes this scroll
    # box's selected value to become unselected, and to
    # generate an event that calls this function, and has
    # no value selected.  As a result, "curselection()"
    # returns empty.
    
    # So, we need to test for the unselected condition,
    # and not run the function if so.

    if len(list_box.curselection()) == 0:
        # This list box was just unselected,
        # and not has nothing selected.  As
        # result, we should not be running this
        # function.  Only run it if we selected
        # an item from the list.
        return
        
    # If you are here, then the function was NOT
    # called due to an unselect event happening.
    artist_index = list_box.curselection()[0]
    artist_name = list_box.get(artist_index),
    
    # Get the artist id number as the artist ID number is used in the
    # 'albums' table.
    # fetchone(): If the name returns multiple values, grab just the 1st.
    # fetchone(): returns a tuple.
    artist_id = db_conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
    
    # Get the albums for this artist, and add them to a temp list:
    temp_album_list = []
    
    for row in db_conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ?"
                               "ORDER BY albums.name", artist_id):
        
        # You need 'row[0]' because apparently the "execute" returns a list of 1 item.
        # You want the '0th', and only item in the list.
        temp_album_list.append(row[0])
    
    # "album_lv" is the variable tied to the album scroll box.
    # Any update to the variable is automatically reflected in the scroll box.
    # ".set()" requires a tuple.
    album_lv.set(tuple(temp_album_list))
    
    # Now that we have reset the album list, clear out the songs list
    # b/c it was reflective of the past album choice.
    song_lv.set(("Choose an album",))


def get_songs(event):
    # When an album is selected from the "Albums" list box,
    # populate the "Songs" list box with the songs for that
    # album.
    
    # See notes in "get_albums" for explanation of code that
    # is shared b/t the two.
    
    # The 'widget' variable that holds the tkinter object/widget
    # that is associated with the action; in our case, the
    # "albums" scroll box.
    list_box = event.widget
    
    # From the 'album' list box, get the presently selected album.
    # Notes:
    # 1) list_box.curselection() --> will return a list of POSITIONS of all the selected items.
    # 2) As it's possible to select more than 1 item from list box by
    # holding down the shift, or other keys, we use [0] to grab the 1st
    # album from the list.
    # 3) list_box.get(index) --> Once we have the index, get the value at that location.
    # 4) you need the "," after 'list_box(index)' to return a tuple.
    # The SELECT query needs a tuple.

    # Note: There is a change to the way python 3.7 (for mac)
    # handles the bind/select.  When you select
    # a value in another scroll box, it causes this scroll
    # box's selected value to become unselected, and to
    # generate an event that calls this function, and has
    # no value selected.  As a result, "curselection()"
    # returns empty.

    # So, we need to test for the unselected condition,
    # and not run the function if so.

    if len(list_box.curselection()) == 0:
        # This list box was just unselected,
        # and not has nothing selected.  As
        # result, we should not be running this
        # function.  Only run it if we selected
        # an item from the list.
        return
    
    # If you are here, then the function was NOT
    # called due to an unselect event happening.
    song_index = int(list_box.curselection()[0])
    album_name = list_box.get(song_index),

    # Get the album id number as the album ID number is used in the
    # 'songs' table.
    # fetchone(): If the name returns multiple values, grab just the 1st.
    # fetchone(): returns a tuple.
    album_id = db_conn.execute("SELECT albums._id FROM albums WHERE albums.name = ?", album_name).fetchone()
    
    temp_song_list = []
    
    for x in db_conn.execute("SELECT songs.title FROM songs WHERE songs.album = ?"
                             "ORDER BY songs.track", album_id):
        temp_song_list.append(x[0])
    
    # "song_lv" is the variable tied to the songs scroll box.
    # Any update to the variable is automatically reflected in the scroll box.
    # ".set()" requires a tuple.
    song_lv.set(tuple(temp_song_list))
    
    
############################
# End Function Definitions #
############################


db_conn = sqlite3.connect("music.sqlite")

# Create the GUI window.
main_winodw = tkinter.Tk()
main_winodw.title('Music DB Browser')
main_winodw.geometry('1024x768')

# Set up the columns:

# - A note about 'weight' with tkinter/grid use from:
# (http://effbot.org/tkinterbook/grid.htm)
#
# weight=
# A relative weight used to distribute additional space between columns. A
# column with the weight 2 will grow twice as fast as a column with weight
# 1. The default is 0, which means that the column will not grow at all.

main_winodw.columnconfigure(0, weight=2)
main_winodw.columnconfigure(1, weight=2)
main_winodw.columnconfigure(2, weight=2)
main_winodw.columnconfigure(3, weight=1)    # Spacer column on right.

main_winodw.rowconfigure(0, weight=1)
main_winodw.rowconfigure(1, weight=5)
main_winodw.rowconfigure(2, weight=5)
main_winodw.rowconfigure(3, weight=1)

##########
# Labels #
##########

artists_label = tkinter.Label(main_winodw, text="Artists")
artists_label.grid(row=0, column=0)

albums_label = tkinter.Label(main_winodw, text="Albums")
albums_label.grid(row=0, column=1)

songs_label = tkinter.Label(main_winodw, text="Songs")
songs_label.grid(row=0, column=2)

###################
# Artist List Box #
###################

artists_list = ScrollBox(main_winodw)
# padx --> 30 pixels on the left, 0, on the right)
artists_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artists_list.config(border=2, relief='sunken')

# Populate the list box with the all the artist:
for artist in db_conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    # For each artist (in alphabetical order), add the artist to
    # the end of the list.  This will keep it in alphabetical order.
    # It looks like the "insert" function takes in a location in the
    # list box (in this case the end of the box), a list to add.
    # Apparently, the select statement returns a tuple of 1 element.
    # (Note: the code works fine as "artist" not "artist[0]".  But,
    # this the way the teacher wants it done.)
    # artists_list.insert(location to insert, what to insert)
    artists_list.insert(tkinter.END, artist[0])

# Now that the scroll box is populated, make it so
# that, when you select an entry, it will call a function
# that will will write.  The function, when executed, will
# cause the "Albums" scroll box to update with the albums
# by that artist/band.
# Note: Apparently, the 'bind' function will pass, as a parameter,
# to the function to call the event/action that was triggered.
# 01:31
artists_list.bind('<<ListboxSelect>>', get_albums)

###################
# Albums List Box #
###################

album_lv = tkinter.Variable(main_winodw)
album_lv.set(("Choose an artist",))
albums_list = ScrollBox(main_winodw, listvariable=album_lv)
albums_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albums_list.config(border=2, relief='sunken')

# The scroll box will be populated when an album is selected
# from the "albums" scroll box.  The follow will tie selecting
# an album to calling a function to populate the "songs" list box.
# Note: Apparently, the 'bind' function will pass, as a parameter,
# to the function to call the event/action that was triggered.
# 01:31
albums_list.bind('<<ListboxSelect>>', get_songs)


#################
# Song List Box #
#################

song_lv = tkinter.Variable(main_winodw)
song_lv.set(("Choose a song",))
songs_list = ScrollBox(main_winodw, listvariable=song_lv)
songs_list.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songs_list.config(border=2, relief='sunken')


#############
# Main Loop #
#############
test_list = range(0, 100)
album_lv.set(tuple(test_list))

main_winodw.mainloop()

print("Closing database connection.")
db_conn.close()

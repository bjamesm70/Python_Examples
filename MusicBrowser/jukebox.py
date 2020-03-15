# jukebox.py

# A GUI interface that shows you artists, their albums,
# and the songs in those albums.

# Lecture: 221. Simple Database Browser

# I left is debug print statements.

# - Jim

import sqlite3
import tkinter

# Connect to the DB:
music_db_conn = sqlite3.connect("./music.sqlite")

# Which artist is presently selected?
# I'm not a fan of global variables.
# However, some artists may have albums of the same name.
# So, we need to know the artist's name in order to get the
# right album to display the songs.
# There's no way to pass the artist info to the function that
# pulls the songs from an album (at least there is no way
# that I know of w/ my current python skill.)
artist_id: None = None

# We are creating own class for the listbox + scrolling:


class Scrollbox(tkinter.Listbox):
    
    # This class has a listbox + a scrollbar.
    # It's parent's class is a listbox.  We add
    # in a scrollbar.
    
    def __init__(self, window, **kwargs):
        # Create the list box.
        super().__init__(window, **kwargs)
    
        # Add the scroll bar, and associate its movement to the list box.
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)
        
        # Associate movement w/i the list box with the scroll bar's location.
        self["yscrollcommand"] = self.scrollbar.set

    # Overwriting the parent's (Listbox)  "grid" function.
    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
        # Put the listbox on the left, and the scrollbar on the right.
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)


# End of classes

# Start of functions:

def get_albums(event):
    
    # global artist_id: We need to share this info so that we can
    # select the correct album.  Some album names are common like
    # "Greatest Hits".
    global artist_id
    
    # Get the artist name from the selection.
    list_box = event.widget
    # "list_box" is the list box had is calling
    # this function.  It has a function called
    # "curselection()".  It returns a tuple of
    # the currently selected items - their indexes.  (You can
    # have more than 1 selection.)  So, we are
    # just going to take item [0] in the tuple
    # b/c mostly likely we only selected 1 item.
    # curselection --> I guess it stands for "current selection".
    
    # The new version of tkinter has the "binding()" function
    # send an event, to the bound function, when you select a
    # different list box (call it ListBoxB).  Let's call this a
    # "deselect" of your original list box.  So, ListBoxA will send
    # a "ListboxSelect" event to its attached function.  And,
    # "curselection" will contain an empty tuple b/c no items,
    # in ListBoxA, are activitely/currently selected.  You need
    # to deal with that:  (Really dumb design in my opinion!
    # However, m/b I'll learn it's usefulness in time.)  You,
    # now, need to test for that!

    print("curselection is '{}'.".format(list_box.curselection()))
    if not list_box.curselection():
        # We have a deselection.
        # False call.
        # Do nothing.  Return.
        print("it's null")
        return
    
    # If you are here, then you have a value from "curselection()".
    # This time, the function was not called as a result of a deselection!
    
    # Get the albums for the artist, and populate the list box:
    index = list_box.curselection()[0]
    print("index is: '{}', type: '{}'.".format(index, type(index)))
    
    # This will be the actual value at that index aka the
    # value that was populated into it: the name of the band (as a string).
    
    # Either form below is fine.
    # selected_artist_name = tuple([list_box.get(album_index)])
    selected_artist_name = list_box.get(index)
    print("selected_artist_name is: '{}', type: '{}'.".format(selected_artist_name, type(selected_artist_name)))

    # We want the id number associated w/ the artist name.
    # This way we can use it to find the artist's albums in the album table.
    # The ".execute" statement returns an iterable.
    # We want grab the 1 result from it --> .fetchone()
    # Note: The replacement field list needs to be a tuple.
    # Also, is you just do tuple(some_string), the tuple will make each
    # character 1 element in the tuple.  Hence, we need to declare the
    # contents of "selected_artist_name" as 1 item in the tuple via [...].
    artist_id = music_db_conn.execute("SELECT artists._id FROM artists WHERE artists.name=?",
                                      tuple([selected_artist_name])).fetchone()
    
    print("Artist ID is: ", artist_id)
    
    # Get the artist's albums from the DB:
    albums_for_artist = []
    
    # The "?" replacement expects a tuple.  "artist_id" is a tuple b/c that is
    # what ".execute" returns.
    for row in music_db_conn.execute("SELECT albums.name FROM albums WHERE "
                                     "albums.artist = ? ORDER BY albums.name",  artist_id):
        # Remember ".execute" returns a tuple even when
        # you only get 1 item per row returned.  So, you
        # specifically have to get access the item via row[0].
        print(row[0])
        albums_for_artist.append(row[0])
    
    # Display the albums in the album scroll box:
    # (The "album_label_var" holds what is displayed
    # in the list box.
    album_label_var.set(tuple(albums_for_artist))
    
    # Reset the songs list as we are now onto a new artist.
    song_label_var.set(("Choose an album",))
    
    print("-----------------------------")


def get_songs(song_event):
    print("In 'get_songs'.")
    # What list box called this function?
    list_box = song_event.widget
    
    # The new version of tkinter has the "binding()" function
    # send an event, to the bound function, when you select a
    # different list box (call it ListBoxB).  Let's call this a
    # "deselect" of your original list box.  So, ListBoxA will send
    # a "ListboxSelect" event to its attached function.  And,
    # "curselection" will contain an empty tuple b/c no items,
    # in ListBoxA, are activitely/currently selected.  You need
    # to deal with that:  (Really dumb design in my opinion!
    # However, m/b I'll learn it's usefulness in time.)  You,
    # now, need to test for that!

    print("curselection is '{}'.".format(list_box.curselection()))
    if not list_box.curselection():
        # We have a deselection.
        # False call.
        # Do nothing.  Return.
        print("it's null")
        return
    
    # Get the item selected:
    # Note: > 1 item can be selected.  We are only
    # taking the 1st.
    # "curselection" = current selection
    # We are getting the index number not the album title.
    index = list_box.curselection()[0]
    print("index is: '{}', type: '{}'.".format(index, type(index)))

    # Get the album name.
    album_name = list_box.get(index)

    print(album_name, type(album_name))

    # Get the album id from the DB.
    # .execute creates an iterable.  Assume 1 entry selected (or if > 1, just
    # grab the 1st).  Use "fetchone()" to get 1 row.
    # .execute returns a tuple for each row.
    print("album name is: '{}'.  artist_id is '{}'.  artist_id type is: '{}'."
          .format(album_name, artist_id, type(artist_id)))
    
    # Note: artist_id is a tuple (w/ 1 entry).  It needs to be a single entry.
    # As a result, using: artist_id[0]
    album_id = music_db_conn.execute("SELECT _id FROM albums WHERE albums.name=? "
                                     "AND albums.artist=?", (album_name, artist_id[0])).fetchone()
    
    # sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"

    # Get the songs for this album:
    songs_for_album = []

    for row in music_db_conn.execute("SELECT songs.title FROM songs WHERE "
                                     "songs.album  = ? ORDER BY songs.track",  album_id):
        # .execute returns a tuple (of 1 element in this case).
        # Grab element 0
        songs_for_album.append(row[0])

        print(row)
    
    song_label_var.set(tuple(songs_for_album))
    print("*********************************")


# ===== Main Window =====
# Create the main GUI window:
main_window = tkinter.Tk()
main_window.title("Music DB Browser")
main_window.geometry('1024x768')

# Add the 4 columns.  Let 3 will have data.
# The last column, the one on the right will hold no data.
# It's just to put some space b/t the 3rd column, and the right
# side of the GUI.
main_window.columnconfigure(0, weight=2)    # Artists
main_window.columnconfigure(1, weight=2)    # Records
main_window.columnconfigure(2, weight=3)    # Songs
main_window.columnconfigure(3, weight=1)    # Just a spacer

# Add teh 4 rows.
main_window.rowconfigure(0, weight=1)    # For Column Headings
main_window.rowconfigure(1, weight=5)    # Artists, Records, & Songs
main_window.rowconfigure(2, weight=5)    # Artists cont.
main_window.rowconfigure(3, weight=1)    # Just a spacer

# Headings for the columns:
# (The teacher didn't see a need for assigning these to variables.
# I guess they won't change.)
tkinter.Label(main_window, text="Artists").grid(row=0, column=0)
tkinter.Label(main_window, text="Albums").grid(row=0, column=1)
tkinter.Label(main_window, text="Songs").grid(row=0, column=2)

# =====  Artists Scrollbox =====
# Remember: the artist listbox spans to 2 rows.
artist_listbox = Scrollbox(main_window)
# padx=(30, 0) --> Pad the left side by 30 pixels.
artist_listbox.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artist_listbox.config(border=2, relief="sunken")

# Populate the list:
# (Put them in alphabetically.)
for artist_name in music_db_conn.execute("SELECT artists.name FROM artists ORDER BY  artists.name"):
    # You are iterating through a sorted list of the artists.
    # Add each 1 to the end of the list.
    # Note: The execute statement returns tuples!
    # So, you need to do artist_name[0].  Otherwise,
    # a tuple is put into the list box.
    artist_listbox.insert(tkinter.END, artist_name[0])

# When an artist is selected, call the "get_albums" function
# which will populate the Albums Scroll Box w/ their albums:
# Notes:
# 1) 'get_albums' is it's own function, and not part of the
# "Scrollbox" class.
# 2)  The "binding" will pass the event: "ListboxSelect" to
# the function.  It will pass the list box that triggered the
# function call.  (At that point (when the function is called),
# the list box will have a function called "curselection()"
# which will return a list of the currently selected items.
# (More than 1 item can be selected.)
# 3) curselection -> returns a list of the indexes!
# 4) IMPORTANT: new version of tkinter will cause:
# Unfortunately, the function "get_albums" will also get
# called on a deselect of this list box.  (When you
# select an element in another list box.)  And, we need to
# handle that in "get_songs".
artist_listbox.bind("<<ListboxSelect>>", get_albums)

# ===== Albums Scrollbox =====
# Initial text to display at the top of the scroll box.
# Later, it will hold/display a list of albums for the selected artist.
album_label_var = tkinter.Variable(main_window)
album_label_var.set(("Choose an artist",))

album_listbox = Scrollbox(main_window, listvariable=album_label_var)
album_listbox.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
album_listbox.config(border=2, relief="sunken")

# Whenever an album is selected, call the "get_songs" function.
# Unfortunately, it will also get called on a deselect of this list box.
# (When you select an element in another list box.)
# And, we need to handle that in "get_songs".
album_listbox.bind("<<ListboxSelect>>", get_songs)

# ===== Song Scrollbox =====
# Initial text to display at the top of the scroll box.
# Later, it will hold/display a list of songs for the selected album.
song_label_var = tkinter.Variable(main_window)
song_label_var.set(("Choose an album",))

song_listbox = Scrollbox(main_window, listvariable=song_label_var)
song_listbox.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
song_listbox.config(border=2, relief="sunken")

# ====== Main Loop =====
# Run the GUI:
main_window.mainloop()

# Done w/ the GUI.  Close the DB connection:
print("Closing the DB connection.")
music_db_conn.close()

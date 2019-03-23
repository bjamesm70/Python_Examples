# Jukebox_Ver2.py

# Lesson 176: Simple Database Browser

# This program makes a simple GUI window that
# allows you to select artists, their albums,
# and the songs.  It is a fake interface to
# a jukebox.

# This version creates a class to handle the
# population of the tables.

# Note: There is a change to the way python 3.7 (for mac) handles the bind/select:
# code: elf.bind('<<ListboxSelect>>', self.on_select)
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


class DataListBox(ScrollBox):
    # Subclassing our ScrollBox to add in
    # auto populate of scroll boxes.
    
    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # window = The TKInter window that our app is running in.
        # connection = the connection to the DB.
        # table = which table to work with in the DB.
        # field = which column in the table to look in.
        # sort_order = a list of how do we want the output displayed in the scroll box?
        
        # init method creates the list box, and the sqlite query.

        super().__init__(window, **kwargs)
        
        self.linked_box = None
        self.link_field = None
        self.link_value = None    # Holds the vale that was selected.
        
        # Remember a 'cursor' object allows you to execute statements in the DB
        # which then return an iterator (a pointer to a stream of data).
        # You can iterate forward through the data, and that's it.
        self.cursor = connection.cursor()
        
        self.table = table
        self.field = field

        # Now that the scroll box is created, make it so
        # that, when you select an entry in it, we will call a function
        # that  will cause the "linked_box" to update with the data
        # from column "link_field" for the value selected in our list box.
        # For example, if you select "Aerosmith" from the "Artists" list box,
        # then the "Albums" list box should be populated with the available
        # from Aerosmith.
        # Note: Apparently, the 'bind' function will pass, as a parameter,
        # to the function to call the event/action that was triggered.
        self.bind('<<ListboxSelect>>', self.on_select)
        
        # Query to execute:
        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        
        # If there is an order by, then add it to the select statement.
        # Otherwise, sort by the field you are requesting data for.
        
        # ','.join(sort_order) --> Creates a comma separate list of "sort_order".
        
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        
        else:
            self.sql_sort = " ORDER BY " + self.field
            
    def clear(self):
        
        # Clears a scroll box
        
        # http://effbot.org/tkinterbook/listbox.htm
        # delete's format is:
        # delete(first, last=None)
        # - Deletes one or more items.
        # - Use delete(0, END) to delete all items in the list.
        self.delete(0, tkinter.END)
        
    def link(self, widget, link_field):
        # This function ties to 'widgets' (data list boxes)
        # together.
        # A 'widget' will be another 'DataListBox'.
    
        self.linked_box = widget  # Example "artiists" is tied to "albums".
        
        # Every "DataListBox" has a "link_field".
        # The passed widget of type "DataListBox".
        # The "link_field" will be what we column gets looked through to use
        # populate the widget's list box.
        widget.link_field = link_field
        
    def requery(self, link_value=None):
        
        # Function to run the query.
        
        # Store the ID so that we know the "master" record
        # we populated from.
        self.link_value = link_value
        
        # If a value was passed in, make the query specific to that
        # value.
        if link_value and self.link_field:
            
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            
            # print(sql)    # TODO: For testing.  Remove once coding is completed.
            
            self.cursor.execute(sql, (link_value,))
        
        else:
            # For debugging during writing the code.
            # print(self.sql_select + self.sql_sort)  # TODO: Delete after testing.
            
            # Get the new data.
            self.cursor.execute(self.sql_select + self.sql_sort)
        
        # Remove the old data from the list box.
        self.clear()
        
        # Put the new data in the list box.
        # Note the stream contains tuples!
        for value in self.cursor:
            # Format: objName.insert(location, itemToAdd)
            # So, keep appending to the end.
            # 'value' is a tuple.
            self.insert(tkinter.END, value[0])
        
        # For the case where we click on an artist,
        # the 'albums' list box will populate.  We want
        # the 'songs' list to clear b/c we have not yet
        # selected an album.
        # The code below will do those b/c the "linked_box"
        # (for the "albums" list) is the "songs" list.
        if self.linked_box:
            self.linked_box.clear()
            
    def on_select(self, event):
        # This function looks at what was selected in its widget box, and
        # populates another list box (like "albums", or "songs") with data
        # related to the choice.  For example, if "Aerosmith" is selected from
        # the "artists" list, then the available Aerosmith albums would be populated
        # into the "albums" list box.  If an album is selected from the "albums"
        # list box, then all the songs from the album would be put into the "songs"
        # list box.

        # If the user did not provide a list box to populate,
        # then there is no point in running the code:
        if not self.linked_box:
            # No linked box.
            return
        
        # "is" returns True is a & b are the same object.
        # print("Is 'self', and 'event.widget' the same? ", self is event.widget)    # TODO: remove this test line.

        # Note: There is a change to the way python 3.7 (for mac)
        # handles the bind/select.  When you select
        # a value in another scroll box, it causes this scroll
        # box's selected value to become unselected, and to
        # generate an event that calls this function, and pass
        # no value selected.  As a result, "curselection()"
        # returns empty.

        # So, we need to test for the unselected condition,
        # and not run the function if so.

        if len(self.curselection()) == 0:
            # This list box was just unselected,
            # and not has nothing selected.  As
            # result, we should not be running this
            # function.  Only run it if we selected
            # an item from the list.
            return
    
        # If you are here, then the function was NOT
        # called due to an "unselect" event happening.
        
        # From the list box, get the presently selected item.
        # Notes:
        # 1) self.curselection() --> will return a list of POSITIONS of all the selected items.
        # 2) As it's possible to select more than 1 item from list box by
        # holding down the shift, or other keys, we use [0] to grab the 1st selected
        # item from the list.
        # 3) self.get(index) --> Once we have the index, get the value at that location.
        # 4) you need the "," after 'self.get(index)' to return a tuple.
        # The SELECT query needs a tuple.
        # 5) 'value' will hold the text of what was selected.
        
        field_index = self.curselection()[0]
        value = self.get(field_index),
        
        # If a value was passed in (that holds the value of
        # the item selected), create a text string that we
        # can add to the sql query.
        # So, for example, if "aerosmith" was the selected artist,
        # then add it the where clause when looking up the album, and
        # all its songs.  This will protect us from times when multiple
        # artists have the same album name like "Greatest Hits".
        if self.link_value:
            sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
            # Also update the "value" tuple variable that is used to plug values into
            # the sqlite statement.
            value = value[0], self.link_value
        else:
            # No artist was select.  So, nothing to add to the 'where' clause.
            sql_where = " WHERE " + self.field + "=?"
            
        # Take the text value, and go to the right DB table to find the "id" value
        # associated with the text name held in "value".
        #
        # fetchone(): If the name returns multiple values, grab just the 1st.
        # fetchone(): returns a tuple.
        
        # "self.sql_select" is a generic select statement, defined in __init__, that will
        # search the table associated with the list box for the value defined.
        # (From init: self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table)
        # It returns the 'field' + the '_id'.  Hence, we want [1] in fetchone()[1].
        
        number_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
        
        self.linked_box.requery(number_id)


#########################
# End Class Definitions #
#########################

# Only run the code below if someone specifically
# run this program.  The below 'if' line keeps the
# code from running if the class is imported as a library.
# This is how the teacher did it.  I think I would have moved
# the class to its own file.
if __name__ == '__main__':

    db_conn = sqlite3.connect("music.sqlite")
    
    # Create the GUI window.
    main_window = tkinter.Tk()
    main_window.title('Music DB Browser')
    main_window.geometry('1024x768')
    
    # Set up the columns:
    
    # - A note about 'weight' with tkinter/grid use from:
    # (http://effbot.org/tkinterbook/grid.htm)
    #
    # weight=
    # A relative weight used to distribute additional space between columns. A
    # column with the weight 2 will grow twice as fast as a column with weight
    # 1. The default is 0, which means that the column will not grow at all.
    
    main_window.columnconfigure(0, weight=2)
    main_window.columnconfigure(1, weight=2)
    main_window.columnconfigure(2, weight=2)
    main_window.columnconfigure(3, weight=1)    # Spacer column on right.
    
    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=5)
    main_window.rowconfigure(2, weight=5)
    main_window.rowconfigure(3, weight=1)
    
    ##########
    # Labels #
    ##########
    
    artists_label = tkinter.Label(main_window, text="Artists")
    artists_label.grid(row=0, column=0)
    
    albums_label = tkinter.Label(main_window, text="Albums")
    albums_label.grid(row=0, column=1)
    
    songs_label = tkinter.Label(main_window, text="Songs")
    songs_label.grid(row=0, column=2)
    
    ###################
    # Artist List Box #
    ###################
    
    # The init method creates the list box, and sqlite query.
    artists_list = DataListBox(main_window, db_conn, "artists", "name")
    
    # padx --> 30 pixels on the left, 0, on the right)
    artists_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artists_list.config(border=2, relief='sunken')
    
    # # Populate the list box with the all the artist:
    # for artist in db_conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    #     # For each artist (in alphabetical order), add the artist to
    #     # the end of the list.  This will keep it in alphabetical order.
    #     # It looks like the "insert" function takes in a location in the
    #     # list box (in this case the end of the box), a list to add.
    #     # Apparently, the select statement returns a tuple of 1 element.
    #     # (Note: the code works fine as "artist" not "artist[0]".  But,
    #     # this the way the teacher wants it done.)
    #     # artists_list.insert(location to insert, what to insert)
    #     artists_list.insert(tkinter.END, artist[0])
    
    # Populate the list box w/ the data from the artists' table:
    artists_list.requery()
    
    ###################
    # Albums List Box #
    ###################
    
    album_lv = tkinter.Variable(main_window)
    album_lv.set(("Choose an artist",))
    # The init method creates the list box, and sqlite query.
    # Note: Below, "sort_order" takes a list.
    albums_list = DataListBox(main_window, db_conn, "albums", "name", sort_order=("name",))

    albums_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albums_list.config(border=2, relief='sunken')
    
    # Make it so that when we select an artist in the 'artists' list box,
    # the 'albums' list box is updated with albums from that artist:
    artists_list.link(albums_list, "artist")
    
    #################
    # Song List Box #
    #################
    
    song_lv = tkinter.Variable(main_window)
    song_lv.set(("Choose a song",))
    # Create the box.
    songs_list = DataListBox(main_window, db_conn, "songs", "title", sort_order=("track", "title"))
    
    songs_list.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songs_list.config(border=2, relief='sunken')
    
    # Make it so that when we select an album in the 'album' list box,
    # the 'songs' list box is updated with songs from that album:
    albums_list.link(songs_list, "album")
    
    #############
    # Main Loop #
    #############
    
    main_window.mainloop()
    
    print("Closing database connection.")
    db_conn.close()

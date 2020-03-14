# jukebox_2.py

# A GUI interface that shows you artists, their albums,
# and the songs in those albums.

# Version 2: Consolidating code into fewer classes to
# make it easier to manage: DRY: Don't Repeat Yourself!

# I've left in all the print statements for debugging purposes.
# They can be removed if you like.

# Lecture: 221. Simple Database Browser

# - Jim

import sqlite3
import tkinter


class Scrollbox(tkinter.Listbox):
    
    # We are creating own class for the listbox + scrolling!
    
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


class DataListBox(Scrollbox):
    
    # This class inherits from "Scrollbox".
    # It consolidates some code into 1 class so that
    # the code is reusable instead of having to write
    # the same code for each different list box: Artist, Album, & Record.
    
    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        
        super().__init__(window, **kwargs)
        
        # Our list box way want to communicate w/ another list
        # box.  For example: selecting an album, in the album
        # list box, should populate the the song list box w/ that
        # album's songs.  So, we need to keep take of what
        # list box (DB table), and field in the DB to link to
        # from this box:
        self.linked_box = None
        self.link_field = None
        
        # The value you get if you go to the DB, and look in
        # "link_field".  Useful for making the sql statements
        # more specific.  (For example: searching for an album
        # by a particular artist (the link_value).
        self.link_value = None
        
        # These are some parameters that we read in to the "init" function.
        # All are referring to the DB in 1 way, or another.
        # Note: we don't pass in to this function a "primary_key" field.
        # We assume all the tables have "_id" was the primary key field.
        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        # When we select an item in our list box, call the " " function.
        # That function call will cause another list box to be populated.
        # For example, selecting an artist in the artist list box will
        # cause the album list box to be populated with all the artist's
        # albums.
        # IMPORTANT: new version of tkinter will cause:
        # When you select another list box, your previously
        # selected list box will get a "deselect" triggered
        # which will call the function, and send, and empty
        # string for the selected item.  The code, in your
        # called function, needs to handle that.
        # Note: you are giving the name of the function only!
        # If you put in self.on_select(), python will execute the
        # function, and assume that the return value has the name
        # of the function to bind to the select condition!
        self.bind("<<ListboxSelect>>", self.on_select)
        
        # Create the sql statement to run:
        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table

        # Any special ordering from the parameter list?
        if sort_order:
            # Yes, the user provided a specific ordering.
            # (We are using "join" in case > 1 sort order was passed
            # in the sort_order tuple.
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            # No special sort order specified.
            # Just order by whatever column we are returning.
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        # Use to clear out a list box's display when we need to.
        
        # ".delete()" is inherited from the "tkinter.Listbox" class.
        # It: deletes items from FIRST to LAST (included).
        self.delete(0, tkinter.END)
    
    def link(self, widget, link_field):
        # Add in the table linkings if they are there.
        # The teacher adds the "link_field" to the linked "widget",
        # and not this object.  I would have written the code differently.
        # However, it's how he did it, and it works.  So, all is good!
        self.linked_box = widget
        widget.link_field = link_field
    
    def requery(self, linked_value=None):
        
        # Can take in an optional parameter "linked_value" which can
        # hold a specific artist to query the records of.  Useful for making the sql statements
        # more specific.  (For example: searching for an album
        # by a particular artist (the link_value).
        self.link_value = linked_value
        
        # Save the linked_value if passed.
        
        # Was an value specified, and
        # do we have another table to link to, and populate:
        if linked_value and self.link_field:
            # Yes.
            
            # Build up an sql statement that can take selected value.
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            print(sql)
            
            # Create an iterable to grab data from a little later.
            # Remember: replacement field needs a tuple: (linked_value,)
            self.cursor.execute(sql, (linked_value,))
        else:
            # No specific artist specified.
            # Just populate w/ all the albums.
    
            print(self.sql_select + self.sql_sort)
            # Create the iterable.
            self.cursor.execute(self.sql_select + self.sql_sort)
            
        # Remove the old data from the list box.
        self.clear()
        
        # Append each piece of sorted data to the end of the list box's list.
        for value in self.cursor:
            # tkinter.END --> Where to put the data.
            # As the data is sorted, we want to keep the order,
            # and append it.
            # value[0] --> Remember that the returned data is in a tuple
            # even though it's only 1 value in the tuple.  So, we need
            # the [0] to grab the 1 field returned.
            self.insert(tkinter.END, value[0])
        
        # Do we have a list box that is linked to this one?
        if self.linked_box:
            # Yes.
            # Clear out any linked data.
            self.linked_box.clear()

    def on_select(self, event):
        # Get the name from the selection.
        
        # Make sure that a 2nd list box was passed:
        if not self.linked_box:
            # No linked box was passed.
            return
        
        # "event.widget" should be "self".
        list_box = event.widget
        
        print("'self' is 'event.widget':", self is event.widget)
        
        # "list_box" is the list box that is calling
        # this function.  It has a function called
        # "curselection()".  It returns a tuple of
        # the currently selected items - their indexes.  (You can
        # have more than 1 selection.)  So, we are
        # just going to take item [0] in the tuple
        # b/c, mostly likely, we only selected 1 item.
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
        
        # Get the data from the correct table, and populate the list box:
        index = list_box.curselection()[0]
        print("index is: '{}', type: '{}'.".format(index, type(index)))
        
        # This will be the actual value at that index aka the
        # value that was populated into it: the string/name you selected.
        
        # Adding a comma at the end to turn this into a tuple.
        # It's needed as a tuple to query the DB.
        value = list_box.get(index),
        print("selected_artist_name is: '{}', type: '{}'.".format(value, type(value)))
        
        # If a "link value" is available, add it to the query as it will make the
        # statement more specific.
        sql_where = None
        
        if self.link_value:
            # Update "value" to hold 2 parameters to pass to the sql query statement.
            value = value[0], self.link_value
            sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
        else:
            # No "link value" specified.
            # Don't make the WHERE clause any more specific:
            sql_where = " WHERE " + self.field + "=?"
            
        # We want the id number (in the DB table) associated w/ the value.
        # This way we can use it to find information from another table
        # (like all the albums by an artist, or all the songs in an album.
        # The ".execute" statement returns an iterable.
        # We want grab the 1st result from it --> .fetchone()
        # This is why we converted "value" a/v into a tuple.
        # "sql_select", which we defined previously, returns the field value, and the _id
        # number associated with it.  For example: if you query "Rolling Stones" in the
        # "artists" table, the return value would be something like: Rolling Stones, 56.
        link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
        
        print(link_id)
        
        # Call the function to populate the linked list box w/ the
        # newly selected data.
        
        self.linked_box.requery(link_id)


##################
# End of Classes #
##################

# Only run the code if this file is NOT imported:
if __name__ == "__main__":
    
    ###########################
    # ===== Main Window ===== #
    ###########################
    
    # Connect to the DB:
    music_db_conn = sqlite3.connect("./music.sqlite")
    
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
    
    # Add the 4 rows.
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
    
    ##################################
    # =====  Artists Scrollbox ===== #
    ##################################
    
    # Remember: the artist listbox spans to 2 rows.
    artist_listbox = DataListBox(main_window, music_db_conn, "artists", "name")
    
    # padx=(30, 0) --> Pad the left side by 30 pixels.
    artist_listbox.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artist_listbox.config(border=2, relief="sunken")
    
    # Populate the list:
    # (Put them in alphabetically.)
    # for artist_name in music_db_conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    #     # You are iterating through a sorted list of the artists.
    #     # Add each 1 to the end of the list.
    #     # Note: The execute statement returns tuples!
    #     # So, you need to do artist_name[0].  Otherwise,
    #     # a tuple is put into the list box.
    #     artist_listbox.insert(tkinter.END, artist_name[0])
    
    # A/v code was moved into the class "DataListBox".
    
    # Initial setup: loading all the artist's names from the DB.
    artist_listbox.requery(0)
    
    ################################
    # ===== Albums Scrollbox ===== #
    ################################
    
    # Initial text to display at the top of the scroll box.
    # Later, it will hold/display a list of albums for the selected artist.
    album_label_var = tkinter.Variable(main_window)
    album_label_var.set(("Choose an artist",))
    
    # "sort_order" expects a tuple.
    album_listbox = DataListBox(main_window, music_db_conn, "albums", "name", sort_order=("name",))
    album_listbox.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
    album_listbox.config(border=2, relief="sunken")
    
    # Below was just for testing code during development.
    # album_listbox.requery(12)
    
    # Now that the album list box is created, make it so that selecting
    # an artist, in the artist list box, will cause the artist's albums
    # to populate the album list box:
    artist_listbox.link(album_listbox, "artist")
    
    ##############################
    # ===== Song Scrollbox ===== #
    ##############################
    
    # Initial text to display at the top of the scroll box.
    # Later, it will hold/display a list of songs for the selected album.
    song_label_var = tkinter.Variable(main_window)
    song_label_var.set(("Choose an album",))
    
    song_listbox = DataListBox(main_window, music_db_conn, "songs", "title", sort_order=("track",))
    song_listbox.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
    song_listbox.config(border=2, relief="sunken")
    
    # Below was just for testing during development:
    # song_listbox.requery()
    
    # Now that the album list box is created, make it so that selecting
    # an artist, in the artist list box, will cause the artist's albums
    # to populate the album list box:
    album_listbox.link(song_listbox, "album")
    
    ##########################
    # ====== Main Loop ===== #
    ##########################
    
    # Run the GUI:
    
    main_window.mainloop()
    
    # Done w/ the GUI.  Close the DB connection:
    print("Closing the DB connection.")
    music_db_conn.close()

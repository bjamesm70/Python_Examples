# Song_V2.py

# 125. Write OOP Version
# Taking "Song.py" from Lesson 119,
# and converting it to OOP.

# - Jim
# (Contact Info)


###########
# Classes #
###########


class Song:
    """ Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (str): Name of the song's creator.
        duration (int): Song length in seconds.  Can be 0.
    """
    
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    # To be used as a get function for the "name"
    # parameter defined below.
    def get_title(self):
        return self.title

    # The "find_object" function searches for a "name".
    # So, we create an alias here.
    # Notes:
    # 1) "property" is a class.  You are creating
    # an object to store in name which can then be
    # used to access the properties.
    # 2) The "fget" needs a function.
    # 3) We are creating an object by calling the
    # "init" function for "property".
    # 4) We pass in the function definitions!
    name = property(fget=get_title)
    

class Album:
    """ Class to represent an album using a track list
    
    Attributes:
        name (str): Name of the album.
        year (int): The year the album was released.
        artist (str): The name of the creator of the album.
            Defaults to "Various Artists" if none specified.
        tracks (Lists[Song]): A list of all the songs on the album.
    
    Methods:
        add_song: Used to add a new song to the track list.
    """
    
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        
        self.tracks = []
    
    def add_song(self, title_of_song, position=None):
        """ Adds a song to the track list if not already present.
        
        Args:
            title_of_song (str): Title of the song to add.
            position (Optional - int): If specified, the song is added to the
                position in the track list - inserting between songs if necessary.
                Otherwise, the song is added to the end.
        """
        
        # The "is" operator checks to see if both
        # operands point to the same object in memory.
        # "==" operator just compares their values.
        
        # Search this album for the title.
        # If found, the Song is returned.
        # If not found, "None" is returned.
        
        song_found = find_object(title_of_song, self.tracks)
        
        if song_found is None:
            # New song.
            # Create it, and add it to the album's track list.
            song_found = Song(title_of_song, self.artist)
            
            if position is None:
                # Add it to the end.
                self.tracks.append(song_found)
            else:
                # Add it to the specified location.
                self.tracks.insert(position, song_found)
        
        if position is None:
            self.tracks.append(song_found)
        else:
            self.tracks.insert(position, song_found)


class Artist:
    """ Basic class to store artist details.
    
    Attributes:
        name (str): Name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            Note: the list only includes albums in this collection.
            
    Methods:
        add_album: Use to add a new album to the artist's albums list.
    """
    
    def __init__(self, name):
        self.name = name
        self.albums = []
    
    def add_album(self, album):
        """ Add a new album to the list.
        
        Args:
            album (Album): Album object to add to the list
                with check to confirm it's not already there
                (although this is yet to be implemented).
        """
        
        self.albums.append(album)
    
    def add_song(self, name_of_album, year, title):
        """Adds a new song to an album.
        
        A new album will be created (and added to
        the artist's list) if it does not already exist.
        
        Args:
            name_of_album (str): Name of the album the song belongs to.
            year (int): Year the album was published.
            title (str): Tile of the song.
        """
        
        # Check the artist's list of currently read in albums
        # for this album's name.
        # If found, it returns the album.
        # If not, it returns "None".
        album_found = find_object(name_of_album, self.albums)
        
        if album_found is None:
            # No album found with that name.
            # Create it, and add it to the artist's list of albums.
            print("'{} not found.  Adding it.".format(name_of_album))
            
            album_found = Album(name_of_album, year, self.name)
            self.add_album(album_found)
        
        album_found.add_song(title)


###############
# End Classes #
###############

#############
# Functions #
#############

def find_object(field_name, object_list):
    """Check if 'object_list' has an object with a name of 'field_name'.
    If so, return the matching object."""
    
    for item in object_list:
        if item.name == field_name:
            return item
    
    # If you are here, then no match was found.
    return None


def load_data():
    # Note: The input file is tab delimited.
    
    artist_list = []
    
    # Note: The input file is tab delimited.
    albums_FH = open("./albums.txt", "r")
    
    for line in albums_FH:
        # Data Format: artist (tab) album (tab) year (tab) song (\n)
        # .strip to remove the "\n".
        # .split to break the line up into fields of strings.
        artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
        
        # Convert the year_field (a string) into an int.
        year_field = int(year_field)
        
        ## print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))
        
        # Look for the artist in the current list.
        # "find_object" returns "None" if not found.
        new_artist = find_object(artist_field, artist_list)
        
        if new_artist is None:
            # We have a new artist.
            # Add him/her/them to the artist list.
            new_artist = Artist(artist_field)
            artist_list.append(new_artist)
        
        # Add the song, from the current line, to the album on the current line.
        new_artist.add_song(album_field, year_field, song_field)
    
    # Done with for loop.
    # Done reading input file.
    # Return the read in list.
    
    return artist_list


def create_checkfile(artist_list):
    """Create a file, from the read in data, to use
    for comparison with the original file."""
    
    checkfile_fh = open("checkfile.txt", "w")
    
    for new_artist in artist_list:
        for new_album in new_artist.albums:
            for new_song in new_album.tracks:
                # Add the song to the file:
                print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist,
                        new_album, new_song), file=checkfile_fh)
    
    checkfile_fh.close()


#################
# End Functions #
#################

########
# Main #
########

# If this python file is called directly
# (not "imported"), then load the data.
if __name__ == "__main__":
    
    # Returns a list of artists
    artists = load_data()
    
    for artist in artists:
        print(artist.name)
    
    print("\nThere are {} artist(s)".format(len(artists)))
    
    # Confirm the data is good by writing it to
    # a file, and then comparing it.
    
    create_checkfile(artists)

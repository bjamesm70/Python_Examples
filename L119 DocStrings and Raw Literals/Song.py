# Song.py

# Lesson 119: DocStrings and Raw Literals

# - Jim
# (Contact Info)


###########
# Classes #
###########


class Song:
    """ Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artist): An Artist class object representing the song's creator.
        duration (int): Song length in seconds.  Can be 0.
    """
    
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an album using a track list
    
    Attributes:
        name (str): Name of the album.
        year (int): The year the album was released.
        artist (Artist): The creator of the album.
            Defaults to "Various Artists" if none specified.
        tracks (Lists[Song]): A list of all the songs on the album.
    
    Methods:
        add_song: Used to add a new song to the track list.
    """
    
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
            
        self.tracks = []
    
    def add_song(self, song, position=None):
        """ Adds a song to the track list
        
        Args:
            song (Song): A song to add.
            position (Optional - int): If specified, the song is added to the
                position in the track list - inserting between songs if necessary.
                Otherwise, the song is added to the end.
        """
        
        # The "is" operator checks to see if both
        # operands point to the same object in memory.
        # "==" operator just compares their values.
        
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


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
    
    new_artist = None
    new_album = None
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
        
        # Look for a new artist.
        if new_artist is None:
            # No artist set yet.
            # Must be the beginning of the file.
            # Create an Artist from the current line read in.
            new_artist = Artist(artist_field)
            artist_list.append(new_artist)
            
        elif new_artist.name != artist_field:
            # Artist on this line is different than
            # last line.  (New Artist!)
        
            # Retrieve the artist object from a new artist.
            # Otherwise, create a new artist object,
            # and add it to the artist list.
            new_artist = find_object(artist_field, artist_list)
            
            if new_artist == None:
                # This artist is not yet save to our list.
                # Save him/her/them.
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
                
            new_album = None
        
        if new_album is None:
            # We have new album.
            # Get the info from the line read in,
            # and save the album.
            new_album = Album(album_field, year_field, new_artist)
            new_artist.add_album(new_album)
        
        elif new_album.name != album_field:
            # We've just read in a new album for the current artist.
            # (If the input list is unsorted, then an album may be
            # listed in a few areas.)
            
            # Look for the album in the artist's list:
            # If not found, it returns "None".
            new_album = find_object(album_field, new_artist.albums)
            
            # Was the album found?
            if new_album is None:
                # Album is not in the artist's list.
                # Add it.
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
        
        # Create a new Song object, and add it to the current album's collection.
        new_song = Song(song_field, new_artist)
    
        new_album.add_song(new_song)
    
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

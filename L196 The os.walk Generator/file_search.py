# file_search.py

# Lesson 197: Searching the Filesystem

#

# - Jim
# (contact info)

import os    # For "os.walk"

# From docs.python.com: fnmatch:
# provides support for Unix shell-style wildcards, which are not the same as regular expressions.
import fnmatch    # "File Name Match"


##############
# Functions: #
##############


def find_albums(root_dir, artist_name):
    # It takes in an artist, and returns a list
    # of albums by that artist.
    # Returns a tuple as: path to album including the album, album name by itself
    # This is a generator!
    
    for current_dir, sub_dirs, files in os.walk(root_dir):
    
        # Search your current directory for the sub dir that
        # matches your artist.
        # for artist in fnmatch.filter(sub_dirs, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in sub_dirs), artist_name.upper()):
        for artist in (d for d in sub_dirs if fnmatch.fnmatch(d.upper(), artist_name.upper())):
            # Get the path to the artist's directory.  It will
            # contain the albums for that artist.
            artist_sub_dir = os.path.join(current_dir, artist)
            
            # Look in the artist's sub dir, and get a list of the albums
            # by that artist.
            
            # Remember this is a generator!
            
            # os.walk returns --> path to current dir, list of subdirs, and list of files.
            # The "artist_sub_dir" should only have subdirectories
            # entitled after the albums.  In each 'album' subdir.
            # will be files entitled after each song.
            # Example: 3 - Chip Away The Stone.emp3
            # As the artist_sub_dir won't have any files, and b/c
            # we don't care about any files anyway, we ignore the
            # files found: "_" for the 3rd parameter.
            for album_path, albums, _ in os.walk(artist_sub_dir):
                
                # "albums" will be the subdirs under the artist's dir.
                # Return (one at a time), the path to the album, and
                # the album name itself.
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(ablum_list):
    # Takes in a list of paths to albums, and returns the songs
    # for each album.
    
    # NOTE: this is a generator!
    
    for album in ablum_list:
        
        # Note: this uses data from "find_albums" which
        # returns path_to_album, album_name.
        # As a result, use "album_list[0]" to get the path only.
        # The directory structure is that artist is directory
        # with album dirs in it with song files in each album dir.
        for song in os.listdir(album[0]):
            
            # This is a generator!
            yield song
            

#################
# End Functions #
#################

# Both functions are generators.
album_list = find_albums("music", "black*")
song_list = find_songs(album_list)

for a in album_list:
    print(a)

for s in song_list:
    print(s)

# file_gen.py

# Lesson 196: The os.walk Generator

# Generate a list of music files in a dir structure.

# - Jim
# (contact info)

import os

root_dir = "music"

for path, subdirs, files in os.walk(root_dir, topdown=True):
    
    if files:
        print(path)
        # os.path.split returns a tuple
        # (From the documentation:
        # https://docs.python.org/3.7/library/os.path.html#os.path.split
        # Split the pathname path into a pair,
        # (head, tail) where tail is the last
        # pathname component and head is everything leading up to that.
        first_split = os.path.split(path)
        print(first_split)
        
        # Print Artist, and album:
        second_split = os.path.split(first_split[0])
        print(second_split)
        
        for f in files:
            # A file name will be in the format:
            # Num - SongName.emp3
            # Example: 1 - Rubber Bullets.emp3
            
            # "split" splits a the string into a tuple
            # based off of the pattern: example: " - ".
            
            # A trick with 'split': if you want to get
            # rid of a beginning, or end part of a string,
            # then use that part as the 'pattern match'.
            # Note, however, that it still returns a tuple, and
            # that you need to do [0] at the end.

            # song_details will have a tuple w/ "num", and "song name".
            song_details = f.split('.emp3')[0].split(' - ')
            print(song_details)
            
        # Divider for next album
        print("*" * 40)

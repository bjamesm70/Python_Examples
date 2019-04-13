# mp3_scan.py

# Lesson 198: Reading Mp3 Tags

# - Jim
# (Contact Info)

import os    # for os.walk()
import fnmatch    # for listing names in a directory.
import id3reader_p3 as id3reader    # For tag info associated w/ the mp3 file.


##############
# Functions: #
##############


def find_music(starting_dir, extension):
    # Finds any file (of type 'extension') w/i the
    # directory structure of 'starting_dir'.
    
    # os_walk returns the current dir, a list of subdirs there,
    # and a list of files there.
    # Note: the "current dir" includes your starting_dir
    for current_dir, sub_dirs, files in os.walk(starting_dir):
        
        # Create the complete pass for each music file that
        # end with the 'extension'.
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            
            # Get the absolute path:
            absolute_path = os.path.abspath(current_dir)
            
            # Return 1 file at a time.
            yield os.path.join(absolute_path, file)


#################
# End Functions #
#################

my_music_files_generator = find_music("music", "emp3")

error_list = []    # List to hold files that are not mp3 compatible.


# for f in find_music("music", 'emp3'):
for f in my_music_files_generator:

    try:    # Run this block of code.
        id3r = id3reader.Reader(f)    # Get the tag info for the mp3 file.
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title'))
        )
    except:    # Rare case where you want to capture all exceptions, and not be specific.
        error_list.append(f)

for error_file in error_list:
    print(error_file)

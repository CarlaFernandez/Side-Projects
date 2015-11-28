#-------------------------------------------------------------------------------
# Name:         Automatic file renaming
# Purpose:      Rename all the files in a folder to new randomly generated
#               strings of 7 characters including all uppercase and lowercase
#               letters and dashes.
#
# Author:       Carla Fernandez
#
# Created:      28/11/2015
#-------------------------------------------------------------------------------
import os
import sys
import random

def main():
    pass

if __name__ == '__main__':
    main()

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-'

# ---------------- methods --------------------

def process_folder(path):
    try:
        for filename in os.listdir(path):
                ext = os.path.splitext(filename)[1]
                print "\t filename: %s" %filename
                new_filename = ''.join(random.choice(chars) for i in range(7)) + ext
                while new_filename in os.listdir(path):
                    new_filename = ''.join(random.choice(chars) for i in range(7)) + ext
                print "\t new filename: %s" %new_filename
                os.rename(path + os.sep + filename, path + os.sep + new_filename)
        return True
    except IOError:
        return False



def main():
    for path in sys.argv[1:]:
        print "Renaming in path: %s..." %path
        result = process_folder(path)
        if result:
            print "Success!"
        else:
            print "An error ocurred.\n Please try again"

# ---------------- application --------------------

main()
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      carla
#
# Created:     28/11/2015
# Copyright:   (c) carla 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys
import random

def main():
    pass

if __name__ == '__main__':
    main()

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-'

def process_folder(path):
    for filename in os.listdir(path):
        ext = os.path.splitext(filename)[1]
        print "\t filename: %s" %filename
        new_filename = ''.join(random.choice(chars) for i in range(7)) + ext
        print "\t new_filename: %s" %new_filename
        os.rename(path+ os.sep+ filename, path + os.sep + new_filename)
    return True


def main():
    for path in sys.argv[1:]:
        print "Renaming in path: %s..." %path
        result = process_folder(path)
        if result:
            print "Success!"

main()
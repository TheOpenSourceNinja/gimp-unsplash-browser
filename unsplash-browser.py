#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath("/usr/lib/gimp/2.0/python/")) #Not needed when running the script from within GIMP; I added this so my IDE won't complain about gimpfu
from gimpfu import *

def popupWindow():
    print("Function got called")
    pdb.gimp_message("Function got called")

register(
    proc_name = "BrowseUnsplash",
    blurb = "Lets you browse photos from Unsplash",
    help = "help message",
    author = "James Dearing",
    copyright = "Public domain/CC0 1.0 Universal",
    date = "2016-11",
    label = "Import from Unsplash",
    imagetypes = "*",
    params = [],
    results = [],
    function = popupWindow,
    menu = "<Image>/File/"
)

main(); #"...and finally a call to main to get the plugin started." http://www.gimp.org/docs/python/index.html

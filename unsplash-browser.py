#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath("/usr/lib/gimp/2.0/python/")) #Not needed when running the script from within GIMP; I added this so my IDE won't complain about gimpfu
from gimpfu import *

#We want GTK so we can create windows; my current GIMP (2.8) relies on GTK 2 and PyGTK but I don't want to assume that will always be the case.
try:
	from gi import pygtkcompat
except ImportError:
	pygtkcompat = None

if pygtkcompat is not None:
	pygtkcompat.enable()
	pygtkcompat.enable_gtk(version='2.0')

import gtk

def popupWindow():
	print("Function got called")
	pdb.gimp_message("Function got called")
	
	window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	window.set_border_width(10)
	window.show()
	gtk.main()

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

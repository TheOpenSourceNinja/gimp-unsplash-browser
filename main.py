#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath("/usr/lib/gimp/2.0/python/"))
from gimpfu import *

def plugin_func():
    print("Function got called")

register(
    "BrowseUnsplash",
    "Lets you browse photos from Unsplash",
    "help message",
    "James Dearing",
    "Public domain/CC0 1.0 Universal",
    "2015",
    "My plugin!!",
    "*",
    [],
    [],
    plugin_func
)

main();

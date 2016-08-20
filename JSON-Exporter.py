#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

* File Name : JSON-Exporter.py

* Purpose : Writing JSON output by checking the chapters and images for the
            "https://gitlab.com/greatdeveloper/kitab" project.

* Creation Date : 15-08-2016 (Independence Day Special Hackathon)

* Copyright (c) 2016 Mandeep Singh <mandeeps708@gmail.com>

"""

from __future__ import print_function
import os
import re
import json


def sort_nicely(targetList):
    """ Sorts the given list with natural sort.
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(targetList, key=alphanum_key)

# Directory in which chapters are added.
directory = "/home/mandeep/work/json-export/book"

# Declaration.
bookName = "Design Aids"
totalPages = 0
storage = {}

# Get total number of chapters and pages available.
for root, dirs, files in os.walk(directory):
    # print root, dirs, files
    if root == directory:
        chapters = sorted(dirs, key=str)
    else:
        storage[root] = sort_nicely(files)

    """if root != directory:
        print("Files:", root, files)
    """
    # Calculates total number of pages available.
    totalPages = totalPages + len(files)

print("\nTotal number of Pages:", totalPages)
print("\nTotal number of chapters:", chapters)
print("\nStorage:", storage)

# Basic list structure to be exported as json.
data = {"Book": {"Name": bookName, "totalPages": totalPages,
                 "info": {}}}

# Updating the json list to contain the images.
for item in chapters:
    data['Book']['info'][item] = storage[os.path.join(directory, item)]

print("\nFinal Output:", data)

# Writing data as json format to a file.
with open(os.path.join(directory, "output.json"), 'w') as outputfile:
    json.dump(data, outputfile)

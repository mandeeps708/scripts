#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

* File Name : wikimacro.py

* Purpose : Fetch macros list from FreeCAD wiki, macro URL and author.

* Creation Date : 18-06-2016

* Copyright (c) 2016 Mandeep Singh <mandeeps708@gmail.com>

"""

import requests, bs4

# FreeCAD Macro page.
link = "http://www.freecadweb.org/wiki/index.php?title=Macros_recipes"

req = requests.get(link)

soup = bs4.BeautifulSoup(req.text, 'html.parser')

# Selects the spans with class MacroLink enclosing the macro links.
output = soup.select("span.MacroLink")

for x in output:
    # Prints macro name
    print x.a.getText()

    # Macro URL.
    url = "http://freecadweb.org" + x.a.get("href")
    print url

    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    
    # Use the same URL to fetch macro desciption and macro author
    desc = soup.select(".macro-description")[0].getText()
    author = soup.select(".macro-author")[0].getText()
    print desc, author

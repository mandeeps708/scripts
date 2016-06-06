#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

* File Name : fcmacro2.py

* Purpose : Getting macro code from wiki

* Creation Date : 07-06-2016

* Copyright (c) 2016 Mandeep Singh <mandeeps708@gmail.com>

"""

from __future__ import print_function
import requests, bs4

#macro_link = 'http://www.freecadweb.org/wiki/index.php?title=Macro_Global_Variable_Watcher'
# Some other links for testing:
#macro_link = 'http://www.freecadweb.org/wiki/index.php?title=Macro_Solid_Sweep'
macro_link = 'http://www.freecadweb.org/wiki/index.php?title=Macro_Image_Scaling'


req = requests.get(macro_link)

soup = bs4.BeautifulSoup(req.text, 'html.parser')

output = soup.select(".mw-highlight.mw-content-ltr")[0].getText()

print(output)

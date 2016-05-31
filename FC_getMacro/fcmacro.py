import urllib.request

from pyquery import PyQuery as pq
from lxml import etree

"""This script fetches the macro code from FreeCAD wiki.
"""
# macro_link = 'http://www.freecadweb.org/wiki/index.php?title=Macro_Solid_Sweep'
# macro_link = 'http://www.freecadweb.org/wiki/index.php?title=Macro_Image_Scaling'
macro_link = 'http://www.freecadweb.org/wiki/index.php?title=Macro_Global_Variable_Watcher'

html = urllib.request.urlopen(macro_link).read()
d = pq(html)

# print(html)
# print('Macro link:',macro_link)
# print('d:',d)

# Parsed Macro code.
macro_code = d('.mw-highlight.mw-content-ltr > pre').html()
print('link:',macro_code)

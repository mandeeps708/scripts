from __future__ import print_function
from pyquery import PyQuery as pq

"""This script fetches the macro code from FreeCAD wiki.
"""

macro_link = 'http://www.freecadweb.org/wiki/index.php?title=Macro_Global_Variable_Watcher'
# Some other links for testing:
# macro_link = 'http://www.freecadweb.org/wiki/index.php?title=Macro_Solid_Sweep'
# macro_link = 'http://www.freecadweb.org/wiki/index.php?title=Macro_Image_Scaling'

jQuery = pq(url=macro_link)
# print('jQuery: ', jQuery)

# Parsed Macro code.
macro_code = jQuery('.mw-highlight.mw-content-ltr > pre').html()
print(macro_code)

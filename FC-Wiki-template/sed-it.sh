#!/bin/sh

# Modifying template of FreeCAD macro recipes page
# at http://www.freecadweb.org/wiki/index.php?title=Macros_recipes

# Converting something like [[Macro makeCube|Macro MakeCube]] 
# to {{MacroLink|Macro makeCube}}

# Removing content after the pipe and replacing ending braces.
sed 's/|Macro.*\]\]/\}\}/i' input.txt > wikinew.txt

# Replacing starting braces and add "MacroLink" template tag.
sed -i.bak 's/\[\[Macro/\{\{MacroLink|Macro/' wikinew.txt

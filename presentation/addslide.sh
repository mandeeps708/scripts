#!/bin/bash

while read line
do
echo "">> presentation.md
echo "---">>presentation.md
echo "">>presentation.md
echo "<section data-background=images/$line></section>">>presentation.md
done <list

#let count=1; for i in {1..20}; do grep -q "variable("$count")" variable; [ $? -eq 0 ] ; sed -i -e s/'variable('$count')'/'variable(a '$i')'/ variable; ((count++)); done

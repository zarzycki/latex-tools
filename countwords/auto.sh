#!/bin/bash

set -e

TEXFILE=$1

# Use sed to delete the line containing '\statement' and the next line
gsed -i '/\\statement/{N; d;}' "$TEXFILE.tex"
gsed -i 's#\\bibliography{#\\nobibliography{#g' "$TEXFILE.tex"

htlatex ${TEXFILE}
bibtex ${TEXFILE}
htlatex ${TEXFILE}
htlatex ${TEXFILE}
echo "DONE"

#npm init -y
#npm install puppeteer
#node countwords.js ${TEXFILE}.html

python countWords.py ${PWD}/${TEXFILE}.html

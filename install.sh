#!/bin/sh

CURRENT_DIR=`pwd`
GEANY_DIR=~/.config/geany

cd "${GEANY_DIR}"

if test -d "colorschemes"; then
  TIMESTAMP=`date +%s`
  mv colorschemes "colorschemes_${TIMESTAMP}"
fi

git clone git://github.com/codebrainz/geany-themes.git

cd "${CURRENT_DIR}"

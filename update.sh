#!/bin/sh

CURRENT_DIR=`pwd`
COLOR_SCHEMES_DIR=~/.config/geany/colorschemes

cd "${COLOR_SCHEMES_DIR}"

git pull origin master

cd "${CURRENT_DIR}"

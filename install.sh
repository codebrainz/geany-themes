#!/bin/sh

CSDIR="${XDG_CONFIG_HOME:-$HOME/.config}/geany/colorschemes/"
echo "Installing themes into '$CSDIR'..."
mkdir -p "$CSDIR"

for SCHEME in colorschemes/*.conf; do
  BNAME="${SCHEME##*/}"
  echo " => $BNAME"
  cp "$SCHEME" "$CSDIR"
done

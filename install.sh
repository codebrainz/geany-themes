#!/bin/sh
CSDIR="$HOME/.config/geany/colorschemes/"
echo "Installing themes into \`$CSDIR'..."
mkdir -p "$CSDIR"
for SCHEME in `ls colorschemes/*.conf`
do
  BNAME=`basename "$SCHEME"`
  echo " => $BNAME"
  cp "$SCHEME" "$CSDIR"
done

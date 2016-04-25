#!/bin/sh
SCRIPTDIR=$(dirname $(readlink -f "$0"))
CSDIR="$HOME/.config/geany/colorschemes/"
echo "Installing themes into \`$CSDIR'..."
mkdir -p "$CSDIR"
for SCHEME in `ls ${SCRIPTDIR}/colorschemes/*.conf`
do
  BNAME=`basename "$SCHEME"`
  echo " => $BNAME"
  cp "$SCHEME" "$CSDIR"
done

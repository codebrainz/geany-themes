Geany Themes Index File README
==============================

The `index.json` file is auto-generated using the `make index` command.
The `index` rule of the Makefile runs the `scripts/mkindex.py` script
which reads the colour schemes' info, generates screenshot and download
URLs, base64 encoded 64x64 thumbnails and stores it all into a JSON
formatted text file.

File Format
-----------

The JSON file consists of a top-level dictionary where the keys are
the theme "identifiers" (ie. name used in filenames and code). The
identifiers are not necessarily useful to humans.

### Theme Info Fields

#### author

The author field contains a name and usually an email address, although
the value may be an empty string as well (ie. unknown author). This
string is meant to be human-readable.

#### colorscheme

This is the download URL of the color scheme `.conf` file. If the file
this URL points to is downloaded into the user's colour scheme directory,
the colour scheme will be available in Geany for user once it's restarted.
This field will never be empty.

#### description

A short description of the theme or an empty string. The string is meant
to be displayed to human beings.

#### md5hash

An MD5 hash of the colour scheme `.conf` file from the last time it was
changed. This value can be used to check if a local scheme needs updating
and/or to verify the integrity of the file that could be downloaded using
the `colorscheme` URL field. This field will never be empty.

#### name

A human-readable name of the colour scheme meant to be display for example
in a GUI label/widget. This field will never be empty.

#### screenshot

This is the download URL for a preview image of the colour scheme. The
image will always be in PNG format and the resolution, although not
guaranteed, will be large enough to give an idea of what the colour
scheme looks like. This may be an empty string if the color scheme
doesn't have a screenshot or it may be a generic "screenshot missing"
image.

#### thumbnail

This is a thumbnail image, 64 pixels wide and 64 pixels high, in PNG
format, base64 encoded (for storing in text file). This is a small icon
of the preview screenshot suitable for displaying for example in a GUI
list of schemes. This maybe be an empty string if the colour scheme
doesn't have a screenshot or it maybe be a generic "screenshit missing"
icon that is 64 pixels wide and tall.

#### version

This field contains a whole number that is incremented each time the
theme is changed. You can compare this against installed color scheme
versions to see if an update is available.

<s>The version number is a sequence of one or more digits, optionally
separated by periods/decimal points. The string will always contain
only 0-9 and optional decimal points in between any of the numbers,
for example "1.2.3", "123", "12.3", but never "..2", ".2.", "....", etc.
The result of splitting the string on the decimal point and converting
each component into an integer will always succeed and the string will
never be empty. One or more of the numbers in the string will move in
the upward direction when the colour scheme is modified.</s>

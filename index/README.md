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

#### compat

This field contains a list of Geany version number strings. Each version
number represents a release (or next) version of Geany that should
support the scheme. If this field is empty, missing or contains an
empty list, the scheme should be assumed to work with all versions of
Geany.

#### description

A short description of the theme or an empty string. The string is meant
to be displayed to human beings.

#### scheme_hash

An MD5 hash of the colour scheme `.conf` file from the last time it was
changed. This value can be used to check if a local scheme needs updating
and/or to verify the integrity of the file that could be downloaded using
the `colorscheme` URL field. This field will never be empty.

#### screen_hash

An MD5 hash of the colour scheme preview/screenshot image the last time
it was changed. This value can be used to check if a cached screenshot
needs to be updated locally and/or to verify the integrity of a the
downloaded screenshot. This field may be empty if a screenshot does
not exist.

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

Geany Themes Index Files README
===============================

The files here are auto-generated using the `indices` rule to the main
`Makefile`. Like `make indices` should result in these index files being
regenerated (if needed).

Whenever a color scheme changes it's supposed to increment its `version`
key in the `theme_info` group. This changing version number, output into
the destination index files, will allow clients to detect newer versions
of the color schemes.

There are 3 output formats: [GKeyFile][gkf], [XML][xml] and [JSON][json].
Looking at the generated files should make it obvious how to parse them. The
canonical source if these files is:

* [index.conf][gkfidx]
* [index.xml][xmlidx]
* [index.json][jsonidx]

Barring some Github outtage or them banning these links, they point to where
clients can find the index files.

If you have updated one or more color scheme `.conf` files, change into the
root Geany-Themes directory and run:

    $ make indices

The generated index files are checked into the Geany-Themes Git repository
so there will be a bit of noise whenever updating color scheme files. It
might be beneficial to make one commit for the real changes and one for
updating the generated files.

[gkf]: http://developer.gnome.org/glib/stable/glib-Key-value-file-parser.html
[xml]: http://www.w3.org/XML
[json]: http://www.json.org
[gkfidx]: https://raw.github.com/codebrainz/geany-themes/master/index/index.conf
[xmlidx]: https://raw.github.com/codebrainz/geany-themes/master/index/index.xml
[jsonidx]: https://raw.github.com/codebrainz/geany-themes/master/index/index.json
